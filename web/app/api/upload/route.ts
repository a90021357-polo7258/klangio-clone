import { NextRequest, NextResponse } from 'next/server'

// 허용된 오디오 파일 MIME 타입
const ALLOWED_TYPES = [
    'audio/mpeg',      // MP3
    'audio/wav',       // WAV
    'audio/ogg',       // OGG
    'audio/mp4',       // M4A
    'audio/x-m4a',     // M4A (alternative)
]

// 최대 파일 크기 (50MB)
const MAX_FILE_SIZE = 50 * 1024 * 1024

export async function POST(request: NextRequest) {
    try {
        const formData = await request.formData()
        const file = formData.get('file') as File

        if (!file) {
            return NextResponse.json(
                {
                    success: false,
                    error: '파일이 업로드되지 않았습니다.'
                },
                { status: 400 }
            )
        }

        // 파일 타입 검증
        if (!ALLOWED_TYPES.includes(file.type)) {
            return NextResponse.json(
                {
                    success: false,
                    error: '지원하지 않는 파일 형식입니다. MP3, WAV, OGG, M4A만 가능합니다.'
                },
                { status: 400 }
            )
        }

        // 파일 크기 검증
        if (file.size > MAX_FILE_SIZE) {
            return NextResponse.json(
                {
                    success: false,
                    error: '파일 크기는 50MB를 초과할 수 없습니다.'
                },
                { status: 400 }
            )
        }

        // UUID 생성 (간단한 버전)
        const fileId = `${Date.now()}-${Math.random().toString(36).substr(2, 9)}`

        // FastAPI AI 서버로 전달
        try {
            const aiServerUrl = process.env.AI_SERVER_URL || 'http://127.0.0.1:8000'

            const aiFormData = new FormData()
            aiFormData.append('file', file)

            const aiResponse = await fetch(`${aiServerUrl}/api/analyze`, {
                method: 'POST',
                body: aiFormData,
            })

            if (!aiResponse.ok) {
                const errorData = await aiResponse.json().catch(() => ({ detail: null }));
                throw new Error(errorData.detail || `AI 서버 오류: ${aiResponse.status}`);
            }

            const aiResult = await aiResponse.json()

            // AI 분석 결과 반환
            return NextResponse.json({
                success: true,
                data: {
                    fileId,
                    fileName: file.name,
                    fileSize: file.size,
                    fileType: file.type,
                    ...aiResult.data,
                    message: 'AI 분석이 완료되었습니다!'
                }
            })

        } catch (aiError) {
            console.error('AI 서버 연결 실패:', aiError)

            // AI 서버 실패 시 Mock 응답 반환
            return NextResponse.json({
                success: true,
                data: {
                    fileId,
                    fileName: file.name,
                    fileSize: file.size,
                    fileType: file.type,
                    duration: 180,
                    status: 'processing',
                    message: `AI 서버 연결 실패 (${(aiError as Error).message}). Mock 데이터를 반환합니다.`
                }
            })
        }


    } catch (error) {
        console.error('파일 업로드 에러:', error)
        return NextResponse.json(
            {
                success: false,
                error: '서버 오류가 발생했습니다.'
            },
            { status: 500 }
        )
    }
}

// OPTIONS 요청 처리 (CORS preflight)
export async function OPTIONS() {
    return new NextResponse(null, {
        status: 200,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
        },
    })
}
