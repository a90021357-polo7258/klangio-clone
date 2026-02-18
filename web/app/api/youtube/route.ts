import { NextRequest, NextResponse } from 'next/server'
import { z } from 'zod'

// YouTube URL 검증 스키마 (Shorts 지원 포함)
const youtubeSchema = z.object({
    url: z.string().refine((url) => {
        // 간단한 검증: youtube.com 또는 youtu.be 포함 여부
        return url.includes('youtube.com/') || url.includes('youtu.be/')
    }, {
        message: '유효한 YouTube URL이 아닙니다. (youtube.com 또는 youtu.be 포함 필수)'
    })
})

export async function POST(request: NextRequest) {
    try {
        const body = await request.json()

        // URL 검증
        const validation = youtubeSchema.safeParse(body)
        if (!validation.success) {
            return NextResponse.json(
                {
                    success: false,
                    error: validation.error.issues[0].message
                },
                { status: 400 }
            )
        }

        const { url } = validation.data

        // YouTube 비디오 ID 추출 (다양한 형식 지원)
        // 지원 형식:
        // - youtube.com/watch?v=ID
        // - youtube.com/shorts/ID
        // - youtu.be/ID
        // - youtube.com/embed/ID
        const videoIdMatch = url.match(/(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|shorts\/|watch\?.+&v=))([^#&?]*)/)
        const videoId = videoIdMatch ? videoIdMatch[1] : null

        if (!videoId) {
            return NextResponse.json(
                {
                    success: false,
                    error: 'YouTube 비디오 ID를 추출할 수 없습니다.'
                },
                { status: 400 }
            )
        }

        // AI 서버로 요청 전달
        const aiServerUrl = process.env.AI_SERVER_URL || 'http://127.0.0.1:8000'

        // instrument 파라미터 추출 (기본값: piano)
        const instrument = body.instrument || 'piano'

        const aiResponse = await fetch(`${aiServerUrl}/api/process-youtube`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url, instrument }),
        })

        if (!aiResponse.ok) {
            const errorData = await aiResponse.json().catch(() => ({ detail: null }));
            throw new Error(errorData.detail || `AI 서버 오류: ${aiResponse.status}`);
        }

        const aiResult = await aiResponse.json()

        return NextResponse.json(aiResult)

    } catch (error) {
        console.error('YouTube API 에러:', error)
        return NextResponse.json(
            {
                success: false,
                error: (error as Error).message || '서버 오류가 발생했습니다.'
            },
            { status: 500 }
        )
    }
}
