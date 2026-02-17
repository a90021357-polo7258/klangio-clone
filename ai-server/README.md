# Klangio AI Server

Python FastAPI 서버 - 오디오를 악보로 변환하는 AI 파이프라인

## 기능

- 오디오 파일 분석 (피치, 템포 감지)
- 음표 추출
- MIDI 파일 생성
- MusicXML 생성
- PDF 악보 생성 (Lilypond 필요)

## 설치

### 1. Python 가상 환경 생성

```bash
python -m venv venv
```

### 2. 가상 환경 활성화

**Windows**:
```bash
venv\Scripts\activate
```

**Mac/Linux**:
```bash
source venv/bin/activate
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python main.py
```

또는

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

서버가 `http://localhost:8000`에서 실행됩니다.

## API 엔드포인트

### GET `/`
서버 상태 확인

### GET `/health`
헬스 체크

### POST `/api/analyze`
오디오 파일 분석

**요청**:
- Content-Type: `multipart/form-data`
- Body: `file` (오디오 파일)

**응답**:
```json
{
  "success": true,
  "data": {
    "duration": 30.0,
    "tempo": 120.5,
    "notes_count": 45,
    "notes": [
      {
        "time": 0.5,
        "note": "C4",
        "frequency": 261.63
      }
    ]
  }
}
```

## 기술 스택

- **FastAPI**: 웹 프레임워크
- **Librosa**: 오디오 분석
- **Music21**: MIDI/MusicXML 생성
- **NumPy**: 수치 계산

## 개발

### 테스트

```bash
pytest
```

### 코드 포맷팅

```bash
black .
```

## 배포

Railway, Render, AWS EC2 등에 배포 가능

### Render 배포 예시

1. `render.yaml` 파일 생성
2. Render 대시보드에서 연결
3. 자동 배포

## 라이선스

MIT
