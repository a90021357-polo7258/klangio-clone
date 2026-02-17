'use client'

import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { ChevronDown } from 'lucide-react'

interface FAQItem {
    question: string
    answer: string
}

const faqs: FAQItem[] = [
    {
        question: "음악을 변환한다는 것은 무엇을 의미하나요?",
        answer: "음악 변환(Transcription)은 오디오 파일(MP3, WAV 등)이나 YouTube 동영상의 음악을 악보, MIDI, 또는 MusicXML 형식으로 변환하는 것을 의미합니다. AI가 자동으로 음높이, 리듬, 코드를 분석하여 악보를 생성합니다."
    },
    {
        question: "어떤 악기를 지원하나요?",
        answer: "피아노, 기타, 베이스, 드럼, 바이올린, 첼로, 보컬, 트럼펫, 색소폰 등 대부분의 악기를 지원합니다. 각 악기에 최적화된 AI 모델을 사용하여 더욱 정확한 변환을 제공합니다."
    },
    {
        question: "정확도는 어떤가요?",
        answer: "AI 모델의 정확도는 음악의 복잡도와 녹음 품질에 따라 다릅니다. 일반적으로 단일 악기 연주는 85-95%의 정확도를 보이며, 복잡한 다중 악기 곡은 70-85% 정도입니다. 변환 후 내장 편집기로 쉽게 수정할 수 있습니다."
    },
    {
        question: "가격은 얼마인가요?",
        answer: "무료 플랜으로 처음 20초를 변환할 수 있습니다. Pro 플랜은 월 $9.99로 무제한 변환이 가능하며, Studio 플랜은 월 $29.99로 다중 악기 변환과 DAW 플러그인을 제공합니다. 모든 유료 플랜은 14일 환불 보장이 적용됩니다."
    },
    {
        question: "어떤 파일 형식을 지원하나요?",
        answer: "입력: MP3, WAV, OGG, M4A, FLAC 등 대부분의 오디오 형식과 YouTube URL을 지원합니다. 출력: PDF 악보, MIDI, MusicXML, Guitar Pro 형식으로 내보낼 수 있습니다."
    },
    {
        question: "모바일에서도 사용할 수 있나요?",
        answer: "네! iOS와 Android용 전용 앱을 제공합니다. 모바일 앱에서는 직접 녹음하거나 기기의 음악 파일을 변환할 수 있으며, 클라우드 동기화로 모든 기기에서 작업을 이어갈 수 있습니다."
    }
]

function FAQItemComponent({ item, index }: { item: FAQItem; index: number }) {
    const [isOpen, setIsOpen] = useState(false)

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5, delay: index * 0.1 }}
            className="border-b border-gray-200 last:border-0"
        >
            <button
                onClick={() => setIsOpen(!isOpen)}
                className="w-full py-6 flex items-center justify-between text-left hover:text-cyan-600 transition-colors group"
            >
                <span className="text-lg font-semibold text-gray-900 group-hover:text-cyan-600 pr-8">
                    {item.question}
                </span>
                <ChevronDown
                    className={`w-6 h-6 text-gray-500 group-hover:text-cyan-600 transition-transform flex-shrink-0 ${isOpen ? 'rotate-180' : ''
                        }`}
                />
            </button>

            <AnimatePresence>
                {isOpen && (
                    <motion.div
                        initial={{ height: 0, opacity: 0 }}
                        animate={{ height: 'auto', opacity: 1 }}
                        exit={{ height: 0, opacity: 0 }}
                        transition={{ duration: 0.3 }}
                        className="overflow-hidden"
                    >
                        <p className="pb-6 text-gray-600 leading-relaxed">
                            {item.answer}
                        </p>
                    </motion.div>
                )}
            </AnimatePresence>
        </motion.div>
    )
}

export default function FAQ() {
    return (
        <section className="py-20 bg-white">
            <div className="container mx-auto px-6">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6 }}
                    className="text-center mb-16"
                >
                    <h2 className="text-4xl font-bold mb-4 text-gray-900">
                        자주 묻는 질문
                    </h2>
                    <p className="text-xl text-gray-600">
                        궁금하신 점이 있으신가요? 여기에서 답을 찾아보세요.
                    </p>
                </motion.div>

                <div className="max-w-3xl mx-auto bg-white rounded-2xl shadow-lg p-8">
                    {faqs.map((faq, index) => (
                        <FAQItemComponent key={index} item={faq} index={index} />
                    ))}
                </div>
            </div>
        </section>
    )
}
