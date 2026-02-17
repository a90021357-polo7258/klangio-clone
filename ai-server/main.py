from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import librosa
import numpy as np
import tempfile
import os
from pathlib import Path
import yt_dlp

app = FastAPI(
    title="Melodify AI Server",
    description="AI-powered audio to sheet music conversion for Melodify",
    version="1.0.0"
)

import shutil
import glob

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

def configure_ffmpeg():
    """Find FFmpeg in Winget packages and add to PATH if not found"""
    if shutil.which("ffmpeg"):
        return None

    print("FFmpeg not found in PATH. Searching in Winget directory...")
    user_home = os.path.expanduser("~")
    winget_path = os.path.join(user_home, "AppData", "Local", "Microsoft", "WinGet", "Packages")
    
    # Search patterns for generic version matching
    patterns = [
        os.path.join(winget_path, "Gyan.FFmpeg*", "ffmpeg*", "bin"),
        os.path.join(winget_path, "Gyan.FFmpeg*", "bin"),
    ]
    
    for pattern in patterns:
        found = glob.glob(pattern)
        if found:
            ffmpeg_dir = found[0]
            print(f"Found FFmpeg at: {ffmpeg_dir}")
            
            # Add to PATH for librosa/audioread
            os.environ["PATH"] += os.pathsep + ffmpeg_dir
            return ffmpeg_dir
            
    print("FFmpeg not found in Winget directory either.")
    return None

# Configure FFmpeg on startup
FFMPEG_DIR = configure_ffmpeg()

class YoutubeRequest(BaseModel):
    url: str

@app.get("/")
async def root():
    """서버 상태 확인"""
    return {
        "message": "Melodify AI Server",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    """헬스 체크"""
    return {"status": "healthy"}

async def process_audio_file(file_path: str, original_filename: str):
    """
    공통 오디오 분석 로직
    """
    try:
        # 오디오 로드
        # duration=30: 처음 30초만 분석 (무료 티어 제한 시뮬레이션)
        y, sr = librosa.load(file_path, sr=22050, duration=30)
        
        # 템포 감지
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        
        # 피치 감지
        pitches, magnitudes = librosa.piptrack(
            y=y,
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
                "fileName": original_filename,
                "duration": float(len(y) / sr),
                "tempo": float(tempo),
                "notes_count": len(unique_notes),
                "notes": unique_notes[:50],  # 처음 50개만 반환
                "sample_rate": sr,
                "message": "오디오 분석이 완료되었습니다."
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Audio analysis failed: {str(e)}")

@app.post("/api/analyze")
async def analyze_audio(file: UploadFile = File(...)):
    """오디오 파일 업로드 및 분석"""
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
        return await process_audio_file(tmp_path, file.filename)
    finally:
        # 임시 파일 삭제
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

@app.post("/api/process-youtube")
async def process_youtube(request: YoutubeRequest):
    """YouTube URL 다운로드 및 분석"""
    url = request.url
    
    # yt-dlp 설정
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(id)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
    }
    
    if FFMPEG_DIR:
        ydl_opts['ffmpeg_location'] = FFMPEG_DIR
    
    with tempfile.TemporaryDirectory() as temp_dir:
        ydl_opts['outtmpl'] = os.path.join(temp_dir, '%(id)s.%(ext)s')
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                video_title = info.get('title', 'YouTube Video')
                video_id = info.get('id', 'unknown')
                filename = f"{video_id}.mp3"
                file_path = os.path.join(temp_dir, filename)
                
                # 오디오 분석 수행
                result = await process_audio_file(file_path, video_title)
                
                # 메타데이터 추가
                result['data']['videoId'] = video_id
                result['data']['title'] = video_title
                
                return result
                
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"YouTube processing failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
