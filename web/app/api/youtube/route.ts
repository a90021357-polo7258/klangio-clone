import { NextRequest, NextResponse } from 'next/server'
import { z } from 'zod'

// YouTube URL 검증 스키마
const youtubeSchema = z.object({
    url: z.string().url().refine((url) => {
        const youtubeRegex = /^(https?:\/\/)?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/)[\w-]+/
        return youtubeRegex.test(url)
    }, {
        message: '유효한 YouTube URL이 아닙니다.'
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
                    error: validation.error.errors[0].message
                },
                { status: 400 }
            )
        }

        const { url } = validation.data

        // YouTube 비디오 ID 추출
        const videoIdMatch = url.match(/(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&]+)/)
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

        // Mock 응답 데이터
        const mockResponse = {
            success: true,
            data: {
                videoId,
                title: '샘플 YouTube 비디오',
                duration: 240,
                thumbnail: `https://img.youtube.com/vi/${videoId}/maxresdefault.jpg`,
                status: 'processing',
                message: '곧 AI 변환이 시작됩니다. 현재는 Mock 데이터입니다.'
            }
        }

        // 실제 구현에서는 여기서 YouTube 오디오 추출 및 AI 처리 시작
        return NextResponse.json(mockResponse)

    } catch (error) {
        console.error('YouTube API 에러:', error)
        return NextResponse.json(
            {
                success: false,
                error: '서버 오류가 발생했습니다.'
            },
            { status: 500 }
        )
    }
}
