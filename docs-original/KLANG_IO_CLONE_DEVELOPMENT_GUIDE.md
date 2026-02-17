# 🎵 Klang.io 클론 개발 가이드
## Anti-Gravity로 동일한 웹사이트 구축하기

---

## 📊 사이트 분석 결과

### 🎯 비즈니스 모델
**Klang.io = AI 음악 악보 변환 SaaS 플랫폼**

#### 핵심 가치 제안
- **문제**: 음악을 악보로 수동 변환 (몇 시간 소요)
- **솔루션**: AI로 자동 변환 (몇 초 완료)
- **타겟**: 음악가, 작곡가, 음악 교사, 학생

#### 수익 모델
- Freemium (무료: 처음 20초, 유료: 전체 곡)
- 악기별 전문 앱 (Piano2Notes, Guitar2Tabs 등)
- DAW 플러그인 판매

#### 주요 통계
- 1,000만+ 변환
- 앱 평점 4.2/5
- 독일 제작 (신뢰성 강조)
- 14일 환불 보장

---

## 🎨 UI/UX 분석

### 1. 히어로 섹션 (첫 화면)

**구성 요소**:
```
[좌측 50%]
- 메인 헤드라인: "AI 음악 전사"
- 부제: "klang.io로 오디오를 악보로 변환"
- 설명: "음악, MP3, YouTube에서 악보, TAB, MIDI, MusicXML로"
- CTA 버튼: "작동 방식" (보조)

[우측 50%]
- 제품 스크린샷 (데스크톱 + 모바일)
- 3D 회전 효과
- 음악 노트 애니메이션 배경

[하단 통계 배너]
- "악보 변환 >1천만"
- "앱 평점 4.2"
- "추천" (언론사 로고)
- "독일에서 제작"
- "14일 환불 보장"
```

**디자인 특징**:
- 다크 네이비 그라디언트 배경
- 형광 청록색 액센트 (음악 노트)
- 화이트/연청색 텍스트
- 클린한 San-serif 폰트

---

### 2. "몇 초 만에 악보를 만드세요" 섹션

**3단계 프로세스**:
```
[Step 1] 음악 업로드
- 아이콘: 마이크/파일
- 설명: "연주 녹음, MP3 업로드, YouTube 링크 사용"

[Step 2] AI가 음표 식별
- 아이콘: AI 뇌/분석
- 설명: "멜로디, 코드, 리듬 자동 분석"

[Step 3] 보기, 편집, 다운로드
- 아이콘: 악보/다운로드
- 설명: "악보, MIDI, MusicXML, Guitar Pro 형식 내보내기"
```

**레이아웃**: 수평 3개 카드, 숫자 배지 (1-2-3)

---

### 3. 라이브 데모 섹션

**특징**:
```
제목: "음악을 악보로 변환하세요 - 직접 경험해보세요"
부제: "처음 20초는 무료로 변환하세요!"

[인터랙티브 업로드 박스]
- 드래그 앤 드롭 영역
- 파일 브라우저 버튼
- YouTube URL 입력 필드
- "변환 시작" 버튼 (밝은 청록색)
```

---

### 4. 제품 라인업 섹션

**2가지 카테고리**:

#### A. Klangio Transcription Studio & 플러그인
```
[왼쪽: 설명]
제목: "Klangio Transcription Studio & 플러그인"
부제: "빠르고, 정확하며, 다중 악기 지원"
설명: "여러 악기의 악보와 MIDI로 한 번에 변환"
타겟: "밴드 음악가, 작곡가, 프로듀서"
플랫폼: "브라우저 및 DAW 플러그인"

[오른쪽: 스크린샷]
- 프로 인터페이스 이미지
- 다중 트랙 악보 보기
```

#### B. 악기별 변환 앱 (6개)
```
[그리드 레이아웃 3x2]
1. Piano2Notes - 피아노 음악을 악보로
2. Guitar2Tabs - 기타/베이스를 TAB로
3. Sing2Notes - 노래를 악보로
4. Drum2Notes - 드럼을 악보로
5. Violin2Notes - 현악기를 악보로
6. Wind2Notes - 금관/목관악기를 악보로

각 카드:
- 악기 일러스트 아이콘
- 앱 이름
- 짧은 설명
- "자세히 보기" 링크
```

---

### 5. 통계 섹션

**대형 카운터**:
```
"10,000,000"
"Klangio의 AI 마법으로 생성된 변환 ✨"
"지금 무료로 사용해 보고 악보를 악보로 변환하세요!"
```

---

### 6. 추가 도구 섹션

**3개 도구 카드**:
```
1. Scan2Notes - 인쇄된 악보 스캔/재생/편집
2. 멜로디 스캐너 - 전체 노래를 피아노 편곡으로
3. 노래 검색 - 무료 노래 분석
```

---

### 7. 고객 후기 섹션

**캐러셀 형태**:
```
[각 후기 카드]
- 인용문 (3-5줄)
- 고객 사진 (원형)
- 이름
- 직함/경력 (예: "피아니스트 겸 프로듀서")
- 사진 크레딧

유명 고객:
- 얀 헤닝 (기타 마법사)
- 틸 잠 (Silbermond 프로듀서)
- 플로리안 지츠만 교수
- 한린 윤 (피아니스트)
```

---

### 8. 기능 상세 섹션

**4개 주요 섹션**:

#### 1. 입력 선택
```
[3개 카드 - 세로 레이아웃]
- 음악 녹음
- 오디오 파일 업로드
- YouTube 동영상 가져오기

각 카드: 아이콘 + 제목 + 설명
```

#### 2. AI 엔진 특징
```
[좌측: 텍스트]
- "무거운 일은 Klangio AI에게 맡기세요"
- 6개 특징 리스트 (체크마크)
  ✓ 빠르고 사용하기 쉬움
  ✓ 다중 악기 지원
  ✓ 다성 음표 감지
  ✓ 악기별 AI 모델
  ✓ 유연한 모드 & 설정
  ✓ 데모 변환

[우측: AI 시각화 이미지]
- 파형 + 악보 변환 과정
```

#### 3. 악보 보기/편집
```
[좌측: 스크린샷]
- 악보 편집기 인터페이스

[우측: 3가지 보기 모드]
- 악보 보기
- 피아노 롤 보기
- 기타 탭
```

#### 4. 다운로드 형식
```
[4개 아이콘 + 설명 가로 배열]
- PDF (악보 & 기타 탭)
- MusicXML
- MIDI
- Guitar Pro
```

---

### 9. 통합 파트너 섹션

**로고 그리드**:
```
[8개 유명 음악 소프트웨어 로고]
- MuseScore
- Guitar Pro
- Sibelius
- Finale
- Cubase
- FL Studio
- Logic Pro
- Ableton

설명: "MusicXML, MIDI, Guitar Pro로 내보내기"
```

---

### 10. 가치 제안 섹션

**6개 박스 (2행 x 3열)**:
```
1. AI 정확성 - 최첨단 AI & 음표 감지
2. 시간 절약 - 몇 초 만에 변환
3. 언제 어디서나 - Klangio Songbook 동기화
4. 다양한 악기 - 다중 악기 감지
5. 활발한 소프트웨어 개발 - 지속 개선
6. 쉬운 워크플로우 통합 - DAW 내보내기
```

---

### 11. 언론 섹션

**로고 벽**:
```
[15+ 언론사/파트너 로고 그리드]
- Professional Audio
- SWR (독일 방송)
- Keyboard Magazine
- Sound & Recording
- 각종 독일 미디어
```

---

### 12. 사용 사례 섹션

**제목**: "음악가를 위한 변환"
**콘텐츠**: 다양한 활용 예시 (비디오/이미지)

---

### 13. FAQ 섹션

**아코디언 형식**:
```
Q: 음악을 변환한다는 것은 무엇을 의미하나요?
A: 오디오를 악보로 변환... (상세 설명)

Q: 어떤 악기를 지원하나요?
A: ...

Q: 정확도는 어떤가요?
A: ...

Q: 가격은 얼마인가요?
A: ...
```

---

## 🛠 기술 스택 제안

### Frontend
```yaml
Framework: Next.js 14 (App Router)
Language: TypeScript
Styling: TailwindCSS + Shadcn/ui
Animation: Framer Motion
3D: Three.js (제품 스크린샷 회전)
Icons: Lucide Icons
Font: Inter (Sans-serif)
```

### Backend
```yaml
API: Next.js API Routes / tRPC
Database: Supabase (PostgreSQL)
File Storage: AWS S3 / Supabase Storage
Auth: Supabase Auth (Google, Apple)
Payment: Stripe
Email: Resend / SendGrid
```

### AI/ML (핵심 기능)
```yaml
음악 변환 AI:
- Python: librosa, Essentia (음악 분석)
- TensorFlow/PyTorch (AI 모델)
- Flask/FastAPI (AI API 서버)

오디오 처리:
- FFmpeg (오디오 변환)
- youtube-dl / yt-dlp (YouTube 다운로드)

악보 생성:
- music21 (MIDI → MusicXML)
- Lilypond (악보 렌더링)
- Verovio (웹 악보 표시)
```

### DevOps
```yaml
Hosting: Vercel (프론트) + AWS EC2 (AI 서버)
CDN: Cloudflare
Monitoring: Sentry
Analytics: Mixpanel / Google Analytics
CI/CD: GitHub Actions
```

---

## 📐 컴포넌트 구조

### 1. 히어로 섹션 컴포넌트

```typescript
// components/HeroSection.tsx
import { motion } from 'framer-motion'
import ProductScreenshot from './ProductScreenshot'

export default function HeroSection() {
  return (
    <section className="relative min-h-screen bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900 overflow-hidden">
      {/* 배경 애니메이션 */}
      <MusicNotesAnimation />
      
      <div className="container mx-auto px-6 pt-32 pb-20">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* 좌측: 텍스트 */}
          <motion.div
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
          >
            <h1 className="text-5xl lg:text-7xl font-bold text-white mb-6">
              AI 음악 전사
            </h1>
            <h2 className="text-3xl lg:text-4xl text-cyan-300 mb-6">
              klang.io로 오디오를 악보로 변환
            </h2>
            <p className="text-xl text-gray-300 mb-8">
              음악, MP3, YouTube에서 악보, TAB, MIDI, MusicXML로.
              <br />
              <strong className="text-white">klang.io</strong>로 음악을 악보로 변환하세요.
              <br />
              <span className="text-cyan-400">AI 음악 악보 변환</span>을 위한 선도적인 도구.
            </p>
            <button className="px-8 py-4 bg-cyan-500 hover:bg-cyan-600 text-white font-semibold rounded-lg transition">
              작동 방식
            </button>
          </motion.div>

          {/* 우측: 제품 스크린샷 */}
          <motion.div
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
          >
            <ProductScreenshot />
          </motion.div>
        </div>
      </div>

      {/* 하단 통계 배너 */}
      <StatsBar />
    </section>
  )
}
```

---

### 2. 3단계 프로세스 컴포넌트

```typescript
// components/ProcessSteps.tsx
const steps = [
  {
    number: 1,
    title: "음악 업로드",
    description: "연주를 녹음하거나, 오디오 파일(예: MP3)을 업로드하거나, YouTube 링크의 오디오를 사용하세요.",
    icon: "microphone"
  },
  {
    number: 2,
    title: "Klangio AI가 음표를 식별",
    description: "Klangio AI는 멜로디, 코드, 리듬을 자동으로 분석하고 음표를 감지합니다.",
    icon: "brain"
  },
  {
    number: 3,
    title: "보기, 편집 및 다운로드",
    description: "변환된 악보를 악보, MIDI, MusicXML 또는 Guitar Pro 형식으로 내보내고 통합된 편집 모드를 사용하세요.",
    icon: "download"
  }
]

export default function ProcessSteps() {
  return (
    <section className="py-20 bg-gray-50">
      <div className="container mx-auto px-6">
        <h2 className="text-4xl font-bold text-center mb-4">
          몇 초 만에 악보를 만드세요!
        </h2>
        <p className="text-xl text-gray-600 text-center mb-16 max-w-4xl mx-auto">
          YouTube 동영상을 악보로 변환하고, 음표를 감지하며, 
          리드 시트나 악보를 순식간에 만드는 데 이상적입니다.
        </p>

        <div className="grid md:grid-cols-3 gap-8">
          {steps.map((step) => (
            <motion.div
              key={step.number}
              className="relative bg-white p-8 rounded-2xl shadow-lg hover:shadow-xl transition"
              whileHover={{ y: -10 }}
            >
              {/* 숫자 배지 */}
              <div className="absolute -top-6 left-8 w-12 h-12 bg-cyan-500 text-white rounded-full flex items-center justify-center text-2xl font-bold">
                {step.number}
              </div>

              {/* 아이콘 */}
              <div className="mt-4 mb-6">
                <StepIcon name={step.icon} />
              </div>

              <h3 className="text-2xl font-bold mb-4">{step.title}</h3>
              <p className="text-gray-600">{step.description}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
```

---

### 3. 라이브 데모 컴포넌트

```typescript
// components/LiveDemo.tsx
'use client'
import { useState } from 'react'
import { Upload, Link as LinkIcon, Loader2 } from 'lucide-react'

export default function LiveDemo() {
  const [uploading, setUploading] = useState(false)
  const [youtubeUrl, setYoutubeUrl] = useState('')

  const handleUpload = async (file: File) => {
    setUploading(true)
    // API 호출 로직
    await convertAudioToSheet(file)
    setUploading(false)
  }

  return (
    <section className="py-20 bg-gradient-to-br from-blue-900 to-slate-900">
      <div className="container mx-auto px-6">
        <h2 className="text-4xl font-bold text-white text-center mb-4">
          음악을 악보로 변환하세요 - 직접 경험해보세요
        </h2>
        <p className="text-xl text-cyan-300 text-center mb-12">
          처음 20초는 무료로 변환하세요!
        </p>

        <div className="max-w-3xl mx-auto bg-white rounded-2xl p-8 shadow-2xl">
          {/* 드래그 앤 드롭 영역 */}
          <div className="border-4 border-dashed border-gray-300 rounded-xl p-12 text-center mb-6 hover:border-cyan-500 transition">
            <Upload className="w-16 h-16 mx-auto mb-4 text-gray-400" />
            <p className="text-xl font-semibold mb-2">
              오디오 파일을 드래그하거나 클릭하여 업로드
            </p>
            <p className="text-gray-500">MP3, WAV, OGG, M4A 지원</p>
            <input
              type="file"
              accept="audio/*"
              onChange={(e) => e.target.files && handleUpload(e.target.files[0])}
              className="hidden"
              id="audio-upload"
            />
            <label
              htmlFor="audio-upload"
              className="mt-4 inline-block px-6 py-3 bg-cyan-500 text-white rounded-lg cursor-pointer hover:bg-cyan-600 transition"
            >
              파일 선택
            </label>
          </div>

          {/* 구분선 */}
          <div className="flex items-center gap-4 my-6">
            <div className="flex-1 h-px bg-gray-300"></div>
            <span className="text-gray-500">또는</span>
            <div className="flex-1 h-px bg-gray-300"></div>
          </div>

          {/* YouTube URL 입력 */}
          <div className="flex gap-3">
            <div className="flex-1 relative">
              <LinkIcon className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" />
              <input
                type="url"
                placeholder="YouTube URL 붙여넣기"
                value={youtubeUrl}
                onChange={(e) => setYoutubeUrl(e.target.value)}
                className="w-full pl-12 pr-4 py-4 border-2 border-gray-300 rounded-lg focus:border-cyan-500 outline-none"
              />
            </div>
            <button
              disabled={uploading}
              className="px-8 py-4 bg-cyan-500 text-white font-semibold rounded-lg hover:bg-cyan-600 transition disabled:bg-gray-400"
            >
              {uploading ? (
                <Loader2 className="animate-spin" />
              ) : (
                "변환 시작"
              )}
            </button>
          </div>
        </div>
      </div>
    </section>
  )
}
```

---

### 4. 제품 카드 컴포넌트

```typescript
// components/ProductCard.tsx
interface ProductCardProps {
  icon: string
  name: string
  description: string
  link: string
}

export default function ProductCard({ icon, name, description, link }: ProductCardProps) {
  return (
    <motion.div
      className="bg-white rounded-xl p-6 shadow-lg hover:shadow-2xl transition group"
      whileHover={{ y: -5 }}
    >
      {/* 아이콘 */}
      <div className="mb-4">
        <img src={icon} alt={name} className="w-16 h-16" />
      </div>

      {/* 제목 */}
      <h3 className="text-2xl font-bold mb-3 group-hover:text-cyan-600 transition">
        {name}
      </h3>

      {/* 설명 */}
      <p className="text-gray-600 mb-4">{description}</p>

      {/* 링크 */}
      <a
        href={link}
        className="inline-flex items-center text-cyan-600 font-semibold hover:text-cyan-700 transition"
      >
        자세히 보기
        <ArrowRight className="ml-2 w-4 h-4" />
      </a>
    </motion.div>
  )
}

// 사용 예시
const products = [
  {
    icon: "/icons/piano.svg",
    name: "Piano2Notes",
    description: "피아노 음악을 악보로 변환합니다.",
    link: "/piano2notes"
  },
  {
    icon: "/icons/guitar.svg",
    name: "Guitar2Tabs",
    description: "기타와 베이스를 TAB로 변환합니다.",
    link: "/guitar2tabs"
  },
  // ... 나머지 제품들
]

<div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
  {products.map((product) => (
    <ProductCard key={product.name} {...product} />
  ))}
</div>
```

---

### 5. 고객 후기 캐러셀

```typescript
// components/TestimonialCarousel.tsx
'use client'
import { useState } from 'react'
import { ChevronLeft, ChevronRight } from 'lucide-react'

const testimonials = [
  {
    quote: "30년 이상 현대 작곡과 기타와 베이스의 정통 연주 기법에 대한 기초 연구를 해온 저는 전문 표기법 소프트웨어에 대한 높은 기준을 가지고 있습니다. Klangio, 마침내 저와 저의 특정 용도에 가장 적합한 소프트웨어를 찾았고, 이를 통해 창의력을 자유롭게 발휘할 수 있게 되었습니다.",
    name: "얀 헤닝",
    title: "기타 마법사",
    image: "/testimonials/jan.jpg",
    credit: "사진: 엘렌 슈마우스"
  },
  // ... 더 많은 후기
]

export default function TestimonialCarousel() {
  const [current, setCurrent] = useState(0)

  const next = () => setCurrent((current + 1) % testimonials.length)
  const prev = () => setCurrent((current - 1 + testimonials.length) % testimonials.length)

  return (
    <section className="py-20 bg-gray-50">
      <div className="container mx-auto px-6">
        <h2 className="text-4xl font-bold text-center mb-4">
          전문가들의 평가
        </h2>
        <p className="text-xl text-gray-600 text-center mb-16">
          아티스트 커뮤니티의 피드백입니다.
        </p>

        <div className="relative max-w-4xl mx-auto">
          {/* 후기 카드 */}
          <motion.div
            key={current}
            initial={{ opacity: 0, x: 100 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -100 }}
            className="bg-white rounded-2xl p-12 shadow-xl"
          >
            {/* 인용 부호 */}
            <div className="text-6xl text-cyan-500 mb-4">"</div>

            {/* 인용문 */}
            <p className="text-xl text-gray-700 mb-8 italic">
              {testimonials[current].quote}
            </p>

            {/* 프로필 */}
            <div className="flex items-center gap-4">
              <img
                src={testimonials[current].image}
                alt={testimonials[current].name}
                className="w-16 h-16 rounded-full object-cover"
              />
              <div>
                <p className="font-bold text-lg">{testimonials[current].name}</p>
                <p className="text-gray-600">{testimonials[current].title}</p>
                <p className="text-sm text-gray-400">{testimonials[current].credit}</p>
              </div>
            </div>
          </motion.div>

          {/* 네비게이션 버튼 */}
          <button
            onClick={prev}
            className="absolute left-0 top-1/2 -translate-y-1/2 -translate-x-12 w-10 h-10 bg-white rounded-full shadow-lg flex items-center justify-center hover:bg-gray-100 transition"
          >
            <ChevronLeft />
          </button>
          <button
            onClick={next}
            className="absolute right-0 top-1/2 -translate-y-1/2 translate-x-12 w-10 h-10 bg-white rounded-full shadow-lg flex items-center justify-center hover:bg-gray-100 transition"
          >
            <ChevronRight />
          </button>

          {/* 인디케이터 */}
          <div className="flex justify-center gap-2 mt-8">
            {testimonials.map((_, index) => (
              <button
                key={index}
                onClick={() => setCurrent(index)}
                className={`w-3 h-3 rounded-full transition ${
                  index === current ? 'bg-cyan-500' : 'bg-gray-300'
                }`}
              />
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}
```

---

## 🔧 핵심 기능 구현

### 1. AI 음악 변환 API

```python
# backend/api/convert.py (Python FastAPI)
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import librosa
import numpy as np
from music21 import stream, note, chord
import tensorflow as tf

app = FastAPI()

# AI 모델 로드
model = tf.keras.models.load_model('./models/audio_to_midi_model.h5')

@app.post("/api/convert")
async def convert_audio(
    file: UploadFile,
    instrument: str = "piano",
    format: str = "musicxml"
):
    try:
        # 1. 오디오 파일 읽기
        audio_data, sr = librosa.load(file.file, sr=22050)
        
        # 2. 특징 추출 (Mel-spectrogram, Chroma, etc.)
        mel_spec = librosa.feature.melspectrogram(y=audio_data, sr=sr)
        chroma = librosa.feature.chroma_cqt(y=audio_data, sr=sr)
        
        # 3. AI 모델로 음표 예측
        predictions = model.predict(prepare_features(mel_spec, chroma))
        
        # 4. 음표 → MIDI/MusicXML 변환
        music_stream = create_music_stream(predictions)
        
        # 5. 출력 형식 변환
        if format == "musicxml":
            output = music_stream.write('musicxml')
        elif format == "midi":
            output = music_stream.write('midi')
        elif format == "pdf":
            output = music_stream.write('lily.pdf')  # Lilypond 사용
        
        return {
            "success": True,
            "file_url": upload_to_s3(output),
            "duration": len(audio_data) / sr,
            "notes_detected": len(music_stream.flatten().notes)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def create_music_stream(predictions):
    """AI 예측 결과를 music21 스트림으로 변환"""
    s = stream.Stream()
    
    for pred in predictions:
        pitch, duration, velocity = pred
        
        if pitch > 0:  # 음표 존재
            n = note.Note(pitch)
            n.duration.quarterLength = duration
            n.volume.velocity = velocity
            s.append(n)
    
    return s
```

---

### 2. YouTube 오디오 추출

```typescript
// app/api/youtube/route.ts
import ytdl from 'ytdl-core'
import { NextRequest, NextResponse } from 'next/server'
import { writeFile } from 'fs/promises'
import { v4 as uuidv4 } from 'uuid'

export async function POST(req: NextRequest) {
  const { url } = await req.json()

  if (!ytdl.validateURL(url)) {
    return NextResponse.json({ error: 'Invalid YouTube URL' }, { status: 400 })
  }

  try {
    const info = await ytdl.getInfo(url)
    const audioFormat = ytdl.chooseFormat(info.formats, {
      quality: 'highestaudio',
      filter: 'audioonly'
    })

    const filename = `${uuidv4()}.mp3`
    const filepath = `/tmp/${filename}`

    // 오디오 스트림 다운로드
    const stream = ytdl(url, { format: audioFormat })
    const chunks: any[] = []

    stream.on('data', (chunk) => chunks.push(chunk))
    stream.on('end', async () => {
      const buffer = Buffer.concat(chunks)
      await writeFile(filepath, buffer)

      // S3 업로드
      const s3Url = await uploadToS3(filepath, filename)

      return NextResponse.json({
        success: true,
        audioUrl: s3Url,
        title: info.videoDetails.title,
        duration: info.videoDetails.lengthSeconds
      })
    })
  } catch (error) {
    return NextResponse.json({ error: 'Failed to extract audio' }, { status: 500 })
  }
}
```

---

### 3. 악보 뷰어 컴포넌트

```typescript
// components/SheetMusicViewer.tsx
'use client'
import { useEffect, useRef } from 'react'
import Verovio from 'verovio'

interface SheetMusicViewerProps {
  musicXML: string
  width?: number
}

export default function SheetMusicViewer({ musicXML, width = 1200 }: SheetMusicViewerProps) {
  const containerRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!containerRef.current) return

    // Verovio 초기화
    const vrvToolkit = new Verovio.toolkit()

    // MusicXML → SVG 렌더링
    vrvToolkit.setOptions({
      scale: 50,
      pageWidth: width,
      pageHeight: 2000,
      adjustPageHeight: true
    })

    vrvToolkit.loadData(musicXML)
    const svg = vrvToolkit.renderToSVG(1)

    containerRef.current.innerHTML = svg

    // 클린업
    return () => {
      containerRef.current!.innerHTML = ''
    }
  }, [musicXML, width])

  return (
    <div className="bg-white rounded-lg shadow-lg p-8 overflow-x-auto">
      <div ref={containerRef} />
    </div>
  )
}
```

---

### 4. 피아노 롤 뷰어

```typescript
// components/PianoRollViewer.tsx
'use client'
import { useEffect, useRef } from 'react'

interface Note {
  pitch: number // MIDI 음높이 (0-127)
  start: number // 시작 시간 (초)
  duration: number // 길이 (초)
  velocity: number // 세기 (0-127)
}

interface PianoRollViewerProps {
  notes: Note[]
  width?: number
  height?: number
}

export default function PianoRollViewer({ notes, width = 1200, height = 600 }: PianoRollViewerProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null)

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return

    const ctx = canvas.getContext('2d')
    if (!ctx) return

    // 캔버스 초기화
    ctx.fillStyle = '#1a1a1a'
    ctx.fillRect(0, 0, width, height)

    // 피아노 건반 그리기 (왼쪽)
    drawPianoKeys(ctx, height)

    // 그리드 그리기
    drawGrid(ctx, width, height)

    // 음표 그리기
    notes.forEach((note) => {
      drawNote(ctx, note, width, height)
    })
  }, [notes, width, height])

  const drawNote = (ctx: CanvasRenderingContext2D, note: Note, w: number, h: number) => {
    const keyboardWidth = 80
    const x = keyboardWidth + (note.start * 100) // 100px = 1초
    const y = h - ((note.pitch / 127) * h)
    const noteWidth = note.duration * 100
    const noteHeight = 8

    // 색상 (벨로시티 기반)
    const alpha = note.velocity / 127
    ctx.fillStyle = `rgba(59, 130, 246, ${alpha})` // 파란색

    ctx.fillRect(x, y, noteWidth, noteHeight)
  }

  const drawPianoKeys = (ctx: CanvasRenderingContext2D, h: number) => {
    const keyWidth = 80
    const whiteKeyHeight = h / 52 // 52 white keys

    for (let i = 0; i < 88; i++) {
      const isBlack = [1, 3, 6, 8, 10].includes(i % 12)
      const y = h - ((i / 88) * h)

      ctx.fillStyle = isBlack ? '#000' : '#fff'
      ctx.fillRect(0, y, keyWidth - 10, whiteKeyHeight)
      ctx.strokeRect(0, y, keyWidth - 10, whiteKeyHeight)
    }
  }

  const drawGrid = (ctx: CanvasRenderingContext2D, w: number, h: number) => {
    ctx.strokeStyle = '#333'
    ctx.lineWidth = 1

    // 수평선 (음높이)
    for (let i = 0; i < 128; i++) {
      const y = h - ((i / 127) * h)
      ctx.beginPath()
      ctx.moveTo(80, y)
      ctx.lineTo(w, y)
      ctx.stroke()
    }

    // 수직선 (시간)
    for (let i = 0; i < 60; i++) {
      const x = 80 + (i * 100)
      ctx.beginPath()
      ctx.moveTo(x, 0)
      ctx.lineTo(x, h)
      ctx.stroke()
    }
  }

  return (
    <div className="bg-gray-900 rounded-lg p-4 overflow-x-auto">
      <canvas
        ref={canvasRef}
        width={width}
        height={height}
        className="border border-gray-700"
      />
    </div>
  )
}
```

---

## 🎨 디자인 시스템

### 색상 팔레트

```typescript
// tailwind.config.ts
export default {
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#e0f2fe',
          100: '#bae6fd',
          200: '#7dd3fc',
          300: '#38bdf8',
          400: '#0ea5e9',
          500: '#0284c7', // 메인 청록색
          600: '#0369a1',
          700: '#075985',
          800: '#0c4a6e',
          900: '#082f49',
        },
        dark: {
          900: '#0f172a', // 네이비
          800: '#1e293b',
          700: '#334155',
        }
      },
      animation: {
        'float': 'float 3s ease-in-out infinite',
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-20px)' },
        }
      }
    }
  }
}
```

---

### 타이포그래피

```css
/* globals.css */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

h1, h2, h3, h4, h5, h6 {
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  line-height: 1.2;
}

p {
  font-family: 'Inter', sans-serif;
  line-height: 1.6;
}
```

---

## 📱 모바일 반응형

```typescript
// 반응형 브레이크포인트
{
  sm: '640px',   // 모바일
  md: '768px',   // 태블릿
  lg: '1024px',  // 데스크톱
  xl: '1280px',  // 대형 화면
  '2xl': '1536px'
}

// 사용 예시
<div className="
  grid 
  grid-cols-1 
  md:grid-cols-2 
  lg:grid-cols-3 
  gap-6
">
  {/* 모바일: 1열, 태블릿: 2열, 데스크톱: 3열 */}
</div>
```

---

## 🚀 배포 가이드

### 1. Vercel 배포 (프론트엔드)

```bash
# 1. Vercel CLI 설치
npm i -g vercel

# 2. 프로젝트 배포
vercel

# 3. 환경 변수 설정
vercel env add NEXT_PUBLIC_AI_API_URL
vercel env add STRIPE_SECRET_KEY
vercel env add SUPABASE_URL
vercel env add SUPABASE_ANON_KEY

# 4. 프로덕션 배포
vercel --prod
```

---

### 2. AI 서버 배포 (AWS EC2)

```bash
# 1. EC2 인스턴스 생성 (Ubuntu 22.04, g4dn.xlarge)
# 2. GPU 드라이버 설치
sudo apt-get update
sudo apt-get install nvidia-driver-525

# 3. Docker 설치
sudo apt-get install docker.io

# 4. AI 서버 Dockerfile
cat > Dockerfile <<EOF
FROM python:3.10-slim

RUN apt-get update && apt-get install -y ffmpeg libsndfile1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EOF

# 5. 빌드 & 실행
docker build -t klang-ai-server .
docker run -d -p 8000:8000 --gpus all klang-ai-server

# 6. Nginx 리버스 프록시 설정
sudo apt-get install nginx
sudo nano /etc/nginx/sites-available/api.klang.io
```

---

## 💰 수익화 전략

### 1. 가격 모델 (Klang.io 참고)

```typescript
// 무료 플랜
{
  name: "Free",
  price: 0,
  features: [
    "처음 20초 무료 변환",
    "데모 변환 무제한",
    "워터마크 포함"
  ]
}

// 프로 플랜
{
  name: "Pro",
  price: "$9.99/월",
  features: [
    "무제한 변환",
    "모든 악기 지원",
    "고품질 PDF 내보내기",
    "MIDI, MusicXML, Guitar Pro 형식",
    "워터마크 제거",
    "우선 지원"
  ]
}

// 스튜디오 플랜
{
  name: "Studio",
  price: "$29.99/월",
  features: [
    "Pro 모든 기능 +",
    "다중 악기 동시 변환",
    "DAW 플러그인 액세스",
    "API 액세스",
    "팀 협업 (5명)"
  ]
}
```

---

### 2. Stripe 구독 통합

```typescript
// app/api/subscribe/route.ts
import Stripe from 'stripe'

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!)

export async function POST(req: Request) {
  const { priceId, userId } = await req.json()

  const session = await stripe.checkout.sessions.create({
    mode: 'subscription',
    payment_method_types: ['card'],
    line_items: [
      {
        price: priceId,
        quantity: 1,
      },
    ],
    success_url: `${process.env.NEXT_PUBLIC_URL}/dashboard?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${process.env.NEXT_PUBLIC_URL}/pricing`,
    client_reference_id: userId,
  })

  return Response.json({ url: session.url })
}
```

---

## 📊 성능 최적화

### 1. 이미지 최적화

```typescript
// Next.js Image 컴포넌트 사용
import Image from 'next/image'

<Image
  src="/screenshots/app.png"
  alt="Product screenshot"
  width={1200}
  height={800}
  priority // 히어로 이미지는 우선 로드
  placeholder="blur" // 블러 효과
/>
```

---

### 2. 코드 스플리팅

```typescript
// 동적 임포트 (큰 컴포넌트)
const PianoRollViewer = dynamic(() => import('@/components/PianoRollViewer'), {
  ssr: false,
  loading: () => <Skeleton />
})
```

---

### 3. API 캐싱

```typescript
// app/api/convert/route.ts
import { Redis } from '@upstash/redis'

const redis = Redis.fromEnv()

export async function POST(req: Request) {
  const { audioUrl } = await req.json()
  
  // 캐시 확인
  const cached = await redis.get(`convert:${audioUrl}`)
  if (cached) {
    return Response.json(cached)
  }

  // 변환 수행
  const result = await convertAudio(audioUrl)

  // 캐시 저장 (1일)
  await redis.set(`convert:${audioUrl}`, result, { ex: 86400 })

  return Response.json(result)
}
```

---

## 🧪 테스트

```typescript
// __tests__/HeroSection.test.tsx
import { render, screen } from '@testing-library/react'
import HeroSection from '@/components/HeroSection'

describe('HeroSection', () => {
  it('renders headline', () => {
    render(<HeroSection />)
    expect(screen.getByText('AI 음악 전사')).toBeInTheDocument()
  })

  it('renders CTA button', () => {
    render(<HeroSection />)
    const button = screen.getByRole('button', { name: /작동 방식/i })
    expect(button).toBeInTheDocument()
  })
})
```

---

## 📈 분석 & 추적

```typescript
// lib/analytics.ts
import mixpanel from 'mixpanel-browser'

mixpanel.init(process.env.NEXT_PUBLIC_MIXPANEL_TOKEN!)

export const trackEvent = (eventName: string, properties?: object) => {
  mixpanel.track(eventName, properties)
}

// 사용 예시
trackEvent('Conversion Started', {
  audioSource: 'upload',
  instrument: 'piano',
  duration: 30
})
```

---

## 🎯 Anti-Gravity 개발 워크플로우

### Phase 1: 기획 & 디자인 (1주)
```
Day 1-2: 기획 에이전트
- Klang.io 상세 분석
- 차별화 포인트 정의
- PRD 작성

Day 3-5: 디자인 에이전트
- Figma 디자인 시스템
- 주요 화면 12개 디자인
- 프로토타입 제작

Day 6-7: 총괄부장 승인
- 디자인 리뷰
- 기술 스택 확정
```

---

### Phase 2: Frontend 개발 (2주)
```
Week 1:
- 프로젝트 설정 (Next.js + TypeScript)
- 공통 컴포넌트 제작
- 히어로 섹션
- 프로세스 단계 섹션
- 제품 카드 섹션

Week 2:
- 라이브 데모 (파일 업로드 UI)
- 고객 후기 캐러셀
- FAQ 아코디언
- 푸터
- 반응형 최적화
```

---

### Phase 3: AI Backend 개발 (3주)
```
Week 1: 오디오 처리
- FFmpeg 통합
- YouTube 다운로더
- 오디오 특징 추출 (librosa)

Week 2: AI 모델
- MIDI 변환 모델 훈련/통합
- 음표 감지 알고리즘
- 악기별 모델 최적화

Week 3: API 구축
- FastAPI 엔드포인트
- S3 파일 업로드
- WebSocket (실시간 진행률)
```

---

### Phase 4: 통합 & 테스트 (1주)
```
Day 1-3: 통합
- Frontend ↔ Backend 연결
- 결제 시스템 (Stripe)
- 이메일 알림

Day 4-5: 테스트
- 유닛 테스트
- E2E 테스트
- 성능 테스트 (대용량 파일)

Day 6-7: 버그 수정
```

---

### Phase 5: 배포 & 마케팅 (1주)
```
Day 1-2: 배포
- Vercel (프론트)
- AWS EC2 (AI 서버)
- DNS 설정

Day 3-7: 마케팅
- Product Hunt 런칭
- 블로그 포스트 3개
- 소셜 미디어 캠페인
```

---

## 📋 Anti-Gravity 에이전트 활용

### 총괄부장 프롬프트
```
"Klang.io 클론 개발 프로젝트를 관리합니다.

목표:
- 8주 내 MVP 출시
- Klang.io 핵심 기능 80% 구현
- 최소 1,000명 베타 사용자 확보

당신의 역할:
- 13개 에이전트 작업 조율
- 일일 진행률 점검
- 블로킹 이슈 해결
- 우선순위 결정

오늘의 질문:
Week 3, Day 2 - AI 모델 통합 중 음표 감지 정확도가 70%입니다. 
목표는 85%입니다. 다음 조치를 추천하세요."
```

---

### 개발 에이전트 프롬프트
```
"Next.js 14로 Klang.io 프론트엔드를 개발합니다.

현재 작업: 라이브 데모 섹션 - 파일 업로드 UI

요구사항:
1. 드래그 앤 드롭 지원
2. MP3, WAV, OGG, M4A 형식 검증
3. 파일 크기 제한 100MB
4. 업로드 진행률 표시 (Progress Bar)
5. 에러 처리 (형식 불일치, 크기 초과)

기술 스택:
- React Dropzone
- Axios (멀티파트 업로드)
- React Query (캐싱)

출력:
- LiveDemo.tsx 컴포넌트 전체 코드
- 유닛 테스트 파일
```

---

### AI 개발 에이전트 프롬프트
```
"Python FastAPI로 음악 → 악보 변환 AI API를 개발합니다.

입력:
- 오디오 파일 (MP3/WAV, 최대 100MB, 최대 10분)

처리:
1. Librosa로 오디오 로드
2. Mel-spectrogram 추출
3. TensorFlow 모델로 음표 예측
4. music21로 MusicXML 생성

출력:
- MusicXML 파일 URL (S3)
- 메타데이터 (BPM, 키, 감지된 음표 수)

성능 요구사항:
- 1분 오디오 → 30초 내 변환
- GPU 사용 (CUDA)
- 배치 처리 지원

코드:
- /api/convert 엔드포인트 구현
- 에러 핸들링
- 로깅 (CloudWatch)
```

---

## 🎉 완성 체크리스트

### Frontend ✅
- [ ] 히어로 섹션 (애니메이션 포함)
- [ ] 3단계 프로세스 섹션
- [ ] 라이브 데모 (파일 업로드 + YouTube)
- [ ] 제품 라인업 (6개 악기 앱)
- [ ] 고객 후기 캐러셀
- [ ] 기능 상세 섹션 (4개)
- [ ] 파트너 로고 그리드
- [ ] 가치 제안 박스
- [ ] 언론 섹션
- [ ] FAQ 아코디언
- [ ] 푸터

### Backend ✅
- [ ] 오디오 업로드 API
- [ ] YouTube 다운로더 API
- [ ] AI 변환 API (MIDI/MusicXML)
- [ ] 악보 렌더링 (PDF)
- [ ] 사용자 인증 (Supabase)
- [ ] 구독 시스템 (Stripe)
- [ ] 파일 저장 (S3)

### 기능 ✅
- [ ] 악보 뷰어 (Verovio)
- [ ] 피아노 롤 뷰어
- [ ] 기타 탭 뷰어
- [ ] 악보 편집기
- [ ] 다운로드 (PDF, MIDI, MusicXML)

### 최적화 ✅
- [ ] 이미지 최적화 (Next.js Image)
- [ ] 코드 스플리팅
- [ ] API 캐싱 (Redis)
- [ ] SEO 최적화
- [ ] Lighthouse 점수 > 90

### 배포 ✅
- [ ] Vercel 배포
- [ ] AWS EC2 (AI 서버)
- [ ] Cloudflare CDN
- [ ] 도메인 연결
- [ ] SSL 인증서

---

## 📚 추가 리소스

### 음악 처리 라이브러리
- **Librosa**: https://librosa.org/ (오디오 분석)
- **music21**: https://web.mit.edu/music21/ (MIDI/MusicXML)
- **Essentia**: https://essentia.upf.edu/ (음악 정보 검색)
- **Verovio**: https://www.verovio.org/ (악보 렌더링)

### AI/ML 리소스
- **Magenta**: https://magenta.tensorflow.org/ (구글 음악 AI)
- **Onsets and Frames**: https://github.com/jongwook/onsets-and-frames (피아노 변환)
- **Basic Pitch**: https://github.com/spotify/basic-pitch (Spotify 오픈소스)

### 디자인 영감
- **Dribbble**: Music AI, Sheet Music 태그
- **Behance**: Audio Transcription 프로젝트

---

## 🚀 다음 단계

1. ✅ **문서 리뷰**: 전체 가이드 숙지
2. 📋 **프로젝트 설정**: GitHub 레포, Notion 워크스페이스
3. 🎨 **디자인 시작**: Figma로 화면 복제
4. 💻 **개발 착수**: Next.js 프로젝트 초기화
5. 🤖 **AI 모델 선택**: Basic Pitch 또는 자체 모델 결정

---

**문의사항이나 추가 가이드가 필요하면 언제든 요청하세요!** 🎵🚀

---

## 📎 첨부 파일

- [Klang.io 스크린샷](https://www.genspark.ai/api/files/s/5viW54Ao)
- [제품 데모 이미지](https://www.genspark.ai/api/files/s/ELGnvbKI)
