'use client'

import { motion } from 'framer-motion'
import { Mic, Brain, Download } from 'lucide-react'

const steps = [
    {
        number: 1,
        title: "음악 업로드",
        description: "연주를 녹음하거나, 오디오 파일(예: MP3)을 업로드하거나, YouTube 링크의 오디오를 사용하세요.",
        icon: Mic
    },
    {
        number: 2,
        title: "Klangio AI가 음표를 식별",
        description: "Klangio AI는 멜로디, 코드, 리듬을 자동으로 분석하고 음표를 감지합니다.",
        icon: Brain
    },
    {
        number: 3,
        title: "보기, 편집 및 다운로드",
        description: "변환된 악보를 악보, MIDI, MusicXML 또는 Guitar Pro 형식으로 내보내고 통합된 편집 모드를 사용하세요.",
        icon: Download
    }
]

export default function ProcessSteps() {
    return (
        <section className="py-20 bg-gray-50">
            <div className="container mx-auto px-6">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6 }}
                >
                    <h2 className="text-4xl font-bold text-center mb-4 text-gray-900">
                        몇 초 만에 악보를 만드세요!
                    </h2>
                    <p className="text-xl text-gray-600 text-center mb-16 max-w-4xl mx-auto">
                        YouTube 동영상을 악보로 변환하고, 음표를 감지하며,
                        리드 시트나 악보를 순식간에 만드는 데 이상적입니다.
                    </p>
                </motion.div>

                <div className="grid md:grid-cols-3 gap-8">
                    {steps.map((step, index) => (
                        <motion.div
                            key={step.number}
                            className="relative bg-white p-8 rounded-2xl shadow-lg hover:shadow-xl transition-shadow"
                            initial={{ opacity: 0, y: 50 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                            transition={{ duration: 0.6, delay: index * 0.2 }}
                            whileHover={{ y: -10 }}
                        >
                            {/* 숫자 배지 */}
                            <div className="absolute -top-6 left-8 w-12 h-12 bg-cyan-500 text-white rounded-full flex items-center justify-center text-2xl font-bold shadow-lg">
                                {step.number}
                            </div>

                            {/* 아이콘 */}
                            <div className="mt-4 mb-6 flex justify-center">
                                <div className="w-20 h-20 bg-cyan-50 rounded-full flex items-center justify-center">
                                    <step.icon className="w-10 h-10 text-cyan-600" />
                                </div>
                            </div>

                            <h3 className="text-2xl font-bold mb-4 text-gray-900 text-center">{step.title}</h3>
                            <p className="text-gray-600 text-center leading-relaxed">{step.description}</p>
                        </motion.div>
                    ))}
                </div>
            </div>
        </section>
    )
}
