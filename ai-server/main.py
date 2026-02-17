from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import librosa
import numpy as np
import tempfile
import os
from pathlib import Path

app = FastAPI(
    title="Klangio AI Server",
    description="AI-powered audio to sheet music conversion",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://klangio-clone.vercel.app",
        "https://klangio-clone-*.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """서버 상태 확인"""
    return {
        "message": "Klangio AI Server",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    """헬스 체크"""
    return {"status": "healthy"}

@app.post("/api/analyze")
async def analyze_audio(file: UploadFile = File(...)):
    """
    오디오 파일 분석
    
    - 피치(음높이) 감지
    - 템포(BPM) 감지
    - 음표 추출
    """
    try:
        # 파일 타입 검증
        allowed_types = ["audio/mpeg", "audio/wav", "audio/ogg", "audio/mp4", "audio/x-m4a"]
        if file.content_type not in allowed_types:
            raise HTTPException(
                status_code=400,
                detail=f"지원하지 않는 파일 형식입니다. 허용: {', '.join(allowed_types)}"
            )
        
        # 임시 파일로 저장
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(file.filename).suffix) as tmp_file:
            content = await file.read()
            tmp_file.write(content)
            tmp_path = tmp_file.name
        
        try:
            # 오디오 로드
            audio, sr = librosa.load(tmp_path, sr=22050, duration=30)  # 처음 30초만
            
            # 템포 감지
            tempo, beats = librosa.beat.beat_track(y=audio, sr=sr)
            
            # 피치 감지
            pitches, magnitudes = librosa.piptrack(
                y=audio,
                sr=sr,
                fmin=librosa.note_to_hz('C2'),
                fmax=librosa.note_to_hz('C7')
            )
            
            # 음표 추출 (간단한 버전)
            notes = []
            hop_length = 512
            
            for t in range(0, pitches.shape[1], 10):  # 10프레임마다 샘플링
                index = magnitudes[:, t].argmax()
                pitch = pitches[index, t]
                
                if pitch > 0 and magnitudes[index, t] > 0.1:  # 임계값
                    note_name = librosa.hz_to_note(pitch)
                    time = librosa.frames_to_time(t, sr=sr, hop_length=hop_length)
                    
                    notes.append({
                        'time': float(time),
                        'note': note_name,
                        'frequency': float(pitch)
                    })
            
            # 중복 제거 (연속된 같은 음표)
            unique_notes = []
            prev_note = None
            for note in notes:
                if note['note'] != prev_note:
                    unique_notes.append(note)
                    prev_note = note['note']
            
            return {
                "success": True,
                "data": {
                    "duration": float(len(audio) / sr),
                    "tempo": float(tempo),
                    "notes_count": len(unique_notes),
                    "notes": unique_notes[:50],  # 처음 50개만 반환
                    "sample_rate": sr,
                    "message": "오디오 분석이 완료되었습니다."
                }
            }
            
        finally:
            # 임시 파일 삭제
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"오디오 분석 중 오류가 발생했습니다: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
