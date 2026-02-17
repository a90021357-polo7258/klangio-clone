# Klang.io Clone

AI 기반 음악 악보 변환 플랫폼 - Klang.io 클론 프로젝트

## 🎵 프로젝트 소개

Klang.io의 핵심 기능을 재현한 웹 애플리케이션입니다. 사용자가 오디오 파일이나 YouTube URL을 업로드하면 AI가 자동으로 악보로 변환합니다.

## ✨ 주요 기능

- 🎹 **6가지 악기별 전문 앱**: Piano, Guitar, Vocal, Drum, Violin, Wind
- 📤 **파일 업로드**: 드래그 앤 드롭으로 MP3, WAV, OGG, M4A 지원
- 🎬 **YouTube 통합**: URL만으로 음악 변환
- 🎨 **현대적인 UI**: TailwindCSS + Framer Motion 애니메이션
- 📱 **반응형 디자인**: 모바일, 태블릿, 데스크톱 지원

## 🛠️ 기술 스택

- **Frontend**: Next.js 14, TypeScript, TailwindCSS
- **Animation**: Framer Motion
- **Icons**: Lucide React
- **Validation**: Zod
- **Deployment**: Vercel

## 🚀 시작하기

### 설치

```bash
cd web
npm install
```

### 개발 서버 실행

```bash
npm run dev
```

http://localhost:3000 에서 확인하세요.

### 빌드

```bash
npm run build
npm start
```

## 📁 프로젝트 구조

```
klangio-clone/
├── web/                    # Next.js 애플리케이션
│   ├── app/
│   │   ├── api/           # API 라우트
│   │   │   ├── upload/    # 파일 업로드 API
│   │   │   └── youtube/   # YouTube 처리 API
│   │   ├── components/    # React 컴포넌트
│   │   └── globals.css    # 전역 스타일
│   └── package.json
└── docs-original/         # 개발 가이드 문서
```

## 🎯 구현된 기능

### 프론트엔드
- ✅ 히어로 섹션 (애니메이션 배경)
- ✅ 3단계 프로세스 설명
- ✅ 라이브 데모 (파일 업로드 + YouTube)
- ✅ 6개 제품 카드
- ✅ 고객 후기 캐러셀
- ✅ FAQ 아코디언
- ✅ 푸터

### 백엔드 API
- ✅ `/api/upload` - 파일 업로드 및 검증
- ✅ `/api/youtube` - YouTube URL 처리
- ✅ Mock 응답 (실제 AI 처리는 향후 구현)

## 🔜 향후 계획

- [ ] Python FastAPI 서버 구축
- [ ] Librosa를 사용한 실제 오디오 분석
- [ ] MIDI 변환 로직
- [ ] PDF 악보 생성

## 📝 라이선스

이 프로젝트는 학습 목적으로 제작되었습니다.

## 👨‍💻 개발자

개발 가이드: `docs-original/KLANG_IO_CLONE_DEVELOPMENT_GUIDE.md`
