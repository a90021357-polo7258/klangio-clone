'use client'

import { useState } from 'react'
import { motion } from 'framer-motion'
import { Upload, Link as LinkIcon, Loader2, CheckCircle, XCircle } from 'lucide-react'

interface UploadResult {
    success: boolean
    data?: {
        fileId?: string
        fileName?: string
        videoId?: string
        title?: string
        status?: string
        message?: string
    }
    error?: string
}

export default function LiveDemo() {
    const [uploading, setUploading] = useState(false)
    const [youtubeUrl, setYoutubeUrl] = useState('')
    const [dragActive, setDragActive] = useState(false)
    const [result, setResult] = useState<UploadResult | null>(null)

    const handleDrag = (e: React.DragEvent) => {
        e.preventDefault()
        e.stopPropagation()
        if (e.type === "dragenter" || e.type === "dragover") {
            setDragActive(true)
        } else if (e.type === "dragleave") {
            setDragActive(false)
        }
    }

    const handleDrop = (e: React.DragEvent) => {
        e.preventDefault()
        e.stopPropagation()
        setDragActive(false)

        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
            handleUpload(e.dataTransfer.files[0])
        }
    }

    const handleUpload = async (file: File) => {
        setUploading(true)
        setResult(null)

        try {
            const formData = new FormData()
            formData.append('file', file)

            const response = await fetch('/api/upload', {
                method: 'POST',
                body: formData,
            })

            const data = await response.json()
            setResult(data)
        } catch (error) {
            setResult({
                success: false,
                error: '업로드 중 오류가 발생했습니다.'
            })
        } finally {
            setUploading(false)
        }
    }

    const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files[0]) {
            handleUpload(e.target.files[0])
        }
    }

    const handleYoutubeSubmit = async () => {
        if (!youtubeUrl) return

        // 클라이언트 사이드 검증
        if (!youtubeUrl.includes('youtube.com/') && !youtubeUrl.includes('youtu.be/')) {
            setResult({
                success: false,
                error: '올바른 YouTube 주소를 입력해주세요. (예: https://youtube.com/shorts/...)'
            })
            return
        }

        setUploading(true)
        setResult(null)

        try {
            const response = await fetch('/api/youtube', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url: youtubeUrl }),
            })

            const data = await response.json()
            setResult(data)
        } catch (error) {
            setResult({
                success: false,
                error: 'YouTube URL 처리 중 오류가 발생했습니다.'
            })
        } finally {
            setUploading(false)
        }
    }

    return (
        <section className="py-20 bg-gradient-to-br from-blue-900 to-slate-900">
            <div className="container mx-auto px-6">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6 }}
                >
                    <h2 className="text-4xl font-bold text-white text-center mb-4">
                        음악을 악보로 변환하세요 - 직접 경험해보세요
                    </h2>
                    <p className="text-xl text-cyan-300 text-center mb-12">
                        처음 20초는 무료로 변환하세요!
                    </p>
                </motion.div>

                <motion.div
                    initial={{ opacity: 0, scale: 0.95 }}
                    whileInView={{ opacity: 1, scale: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6, delay: 0.2 }}
                    className="max-w-3xl mx-auto bg-white rounded-2xl p-8 shadow-2xl"
                >
                    {/* 드래그 앤 드롭 영역 */}
                    <div
                        className={`border-4 border-dashed rounded-xl p-12 text-center mb-6 transition-all ${dragActive
                            ? 'border-cyan-500 bg-cyan-50'
                            : 'border-gray-300 hover:border-cyan-400 hover:bg-gray-50'
                            }`}
                        onDragEnter={handleDrag}
                        onDragLeave={handleDrag}
                        onDragOver={handleDrag}
                        onDrop={handleDrop}
                    >
                        <Upload className="w-16 h-16 mx-auto mb-4 text-gray-400" />
                        <p className="text-xl font-semibold mb-2 text-gray-700">
                            오디오 파일을 드래그하거나 클릭하여 업로드
                        </p>
                        <p className="text-gray-500 mb-4">MP3, WAV, OGG, M4A 지원</p>
                        <input
                            type="file"
                            accept="audio/*"
                            onChange={handleFileInput}
                            className="hidden"
                            id="audio-upload"
                            disabled={uploading}
                        />
                        <label
                            htmlFor="audio-upload"
                            className={`inline-block px-6 py-3 bg-cyan-500 text-white rounded-lg cursor-pointer hover:bg-cyan-600 transition-colors font-semibold ${uploading ? 'opacity-50 cursor-not-allowed' : ''
                                }`}
                        >
                            파일 선택
                        </label>
                    </div>

                    {/* 구분선 */}
                    <div className="flex items-center gap-4 my-6">
                        <div className="flex-1 h-px bg-gray-300"></div>
                        <span className="text-gray-500 font-medium">또는</span>
                        <div className="flex-1 h-px bg-gray-300"></div>
                    </div>

                    {/* YouTube URL 입력 */}
                    <div className="flex gap-3 mb-6">
                        <div className="flex-1 relative">
                            <LinkIcon className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" />
                            <input
                                type="url"
                                placeholder="YouTube URL 붙여넣기"
                                value={youtubeUrl}
                                onChange={(e) => setYoutubeUrl(e.target.value)}
                                onKeyDown={(e) => e.key === 'Enter' && handleYoutubeSubmit()}
                                disabled={uploading}
                                className="w-full pl-12 pr-4 py-4 border-2 border-gray-300 rounded-lg focus:border-cyan-500 outline-none transition-colors text-gray-700 disabled:bg-gray-100"
                            />
                        </div>
                        <button
                            onClick={handleYoutubeSubmit}
                            disabled={uploading || !youtubeUrl}
                            className="px-8 py-4 bg-cyan-500 text-white font-semibold rounded-lg hover:bg-cyan-600 transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed flex items-center gap-2"
                        >
                            {uploading ? (
                                <>
                                    <Loader2 className="animate-spin" />
                                    처리중...
                                </>
                            ) : (
                                "변환 시작"
                            )}
                        </button>
                    </div>

                    {/* 결과 표시 */}
                    {result && (
                        <motion.div
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            className={`p-6 rounded-lg ${result.success ? 'bg-green-50 border-2 border-green-200' : 'bg-red-50 border-2 border-red-200'
                                }`}
                        >
                            <div className="flex items-start gap-3">
                                {result.success ? (
                                    <CheckCircle className="w-6 h-6 text-green-600 flex-shrink-0 mt-1" />
                                ) : (
                                    <XCircle className="w-6 h-6 text-red-600 flex-shrink-0 mt-1" />
                                )}
                                <div className="flex-1">
                                    <h3 className={`font-bold mb-2 ${result.success ? 'text-green-900' : 'text-red-900'}`}>
                                        {result.success ? '✅ 업로드 성공!' : '❌ 오류 발생'}
                                    </h3>
                                    {result.success && result.data ? (
                                        <div className="text-sm text-gray-700 space-y-1">
                                            {result.data.fileName && <p>파일명: {result.data.fileName}</p>}
                                            {result.data.title && <p>제목: {result.data.title}</p>}
                                            {result.data.status && <p>상태: {result.data.status}</p>}
                                            {result.data.message && <p className="mt-2 text-cyan-700 font-semibold">{result.data.message}</p>}
                                        </div>
                                    ) : (
                                        <p className="text-sm text-red-700">{result.error}</p>
                                    )}
                                </div>
                            </div>
                        </motion.div>
                    )}
                </motion.div>
            </div>
        </section>
    )
}
