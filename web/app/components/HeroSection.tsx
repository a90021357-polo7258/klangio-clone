'use client'

import { motion } from 'framer-motion'
import { Play, Upload, Music } from 'lucide-react'

import { useState, useEffect } from 'react'

export default function HeroSection() {
    const [notes, setNotes] = useState<any[]>([])

    useEffect(() => {
        setNotes([...Array(20)].map(() => ({
            x: Math.random() * 100,
            y: Math.random() * 100,
            scale: Math.random() * 0.5 + 0.5,
            yTarget: Math.random() * -20 - 10,
            duration: Math.random() * 10 + 10,
            size: Math.random() * 30 + 20
        })))
    }, [])

    return (
        <section className="relative min-h-screen bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900 overflow-hidden">
            {/* 배경 애니메이션 - 음악 노트 */}
            <div className="absolute inset-0 overflow-hidden">
                {notes.map((note, i) => (
                    <motion.div
                        key={i}
                        className="absolute text-cyan-500/20"
                        initial={{
                            x: `${note.x}%`,
                            y: `${note.y}%`,
                            scale: note.scale
                        }}
                        animate={{
                            y: [null, `${note.yTarget}%`],
                            opacity: [0.2, 0.5, 0.2]
                        }}
                        transition={{
                            duration: note.duration,
                            repeat: Infinity,
                            ease: "linear"
                        }}
                    >
                        <Music size={note.size} />
                    </motion.div>
                ))}
            </div>


            <div className="container mx-auto px-6 pt-32 pb-20 relative z-10">
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
                        <p className="text-xl text-gray-300 mb-8 leading-relaxed">
                            음악, MP3, YouTube에서 악보, TAB, MIDI, MusicXML로.
                            <br />
                            <strong className="text-white">klang.io</strong>로 음악을 악보로 변환하세요.
                            <br />
                            <span className="text-cyan-400">AI 음악 악보 변환</span>을 위한 선도적인 도구.
                        </p>
                        <div className="flex gap-4">
                            <button className="px-8 py-4 bg-cyan-500 hover:bg-cyan-600 text-white font-semibold rounded-lg transition-all transform hover:scale-105 flex items-center gap-2">
                                <Play size={20} />
                                작동 방식
                            </button>
                            <button className="px-8 py-4 bg-white/10 hover:bg-white/20 text-white font-semibold rounded-lg transition-all backdrop-blur-sm flex items-center gap-2">
                                <Upload size={20} />
                                무료 체험
                            </button>
                        </div>
                    </motion.div>

                    {/* 우측: 제품 스크린샷 */}
                    <motion.div
                        initial={{ opacity: 0, x: 50 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ duration: 0.8, delay: 0.2 }}
                        className="relative"
                    >
                        <div className="relative">
                            {/* 3D 회전 효과를 위한 컨테이너 */}
                            <motion.div
                                animate={{
                                    rotateY: [0, 5, 0, -5, 0],
                                }}
                                transition={{
                                    duration: 10,
                                    repeat: Infinity,
                                    ease: "easeInOut"
                                }}
                                className="relative rounded-2xl overflow-hidden shadow-2xl border border-cyan-500/20"
                                style={{ transformStyle: 'preserve-3d' }}
                            >
                                {/* 플레이스홀더 이미지 - 실제 제품 스크린샷으로 교체 */}
                                <div className="bg-gradient-to-br from-slate-800 to-slate-900 p-8 aspect-video flex items-center justify-center">
                                    <div className="text-center">
                                        <Music className="w-24 h-24 text-cyan-500 mx-auto mb-4" />
                                        <p className="text-gray-400">제품 스크린샷 영역</p>
                                    </div>
                                </div>
                            </motion.div>

                            {/* 글로우 효과 */}
                            <div className="absolute -inset-4 bg-cyan-500/20 blur-3xl -z-10 rounded-full"></div>
                        </div>
                    </motion.div>
                </div>
            </div>

            {/* 하단 통계 배너 */}
            <StatsBar />
        </section>
    )
}

function StatsBar() {
    const stats = [
        { label: '악보 변환', value: '>1천만' },
        { label: '앱 평점', value: '4.2/5' },
        { label: '독일에서 제작', value: '🇩🇪' },
        { label: '환불 보장', value: '14일' },
    ]

    return (
        <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
            className="absolute bottom-0 left-0 right-0 bg-white/5 backdrop-blur-md border-t border-white/10"
        >
            <div className="container mx-auto px-6 py-6">
                <div className="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
                    {stats.map((stat, index) => (
                        <div key={index} className="space-y-1">
                            <div className="text-2xl font-bold text-cyan-400">{stat.value}</div>
                            <div className="text-sm text-gray-400">{stat.label}</div>
                        </div>
                    ))}
                </div>
            </div>
        </motion.div>
    )
}
