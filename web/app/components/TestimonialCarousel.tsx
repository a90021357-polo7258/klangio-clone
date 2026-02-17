'use client'

import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { ChevronLeft, ChevronRight, Quote } from 'lucide-react'

interface Testimonial {
    quote: string
    name: string
    title: string
    image?: string
    credit?: string
}

const testimonials: Testimonial[] = [
    {
        quote: "30년 이상 현대 작곡과 기타와 베이스의 정통 연주 기법에 대한 기초 연구를 해온 저는 전문 표기법 소프트웨어에 대한 높은 기준을 가지고 있습니다. Klangio, 마침내 저와 저의 특정 용도에 가장 적합한 소프트웨어를 찾았고, 이를 통해 창의력을 자유롭게 발휘할 수 있게 되었습니다.",
        name: "얀 헤닝",
        title: "기타 마법사",
        credit: "사진: 엘렌 슈마우스"
    },
    {
        quote: "Klangio는 제 음악 작업 흐름을 완전히 바꿔놓았습니다. 이제 아이디어를 즉시 악보로 변환할 수 있어 창작 과정이 훨씬 빨라졌습니다.",
        name: "김민준",
        title: "작곡가 겸 프로듀서"
    },
    {
        quote: "학생들에게 음악을 가르칠 때 Klangio는 필수 도구가 되었습니다. 복잡한 곡도 쉽게 악보로 만들 수 있어 수업 준비 시간이 크게 줄었습니다.",
        name: "이서연",
        title: "음악 교사"
    },
    {
        quote: "피아니스트로서 YouTube에서 들은 곡을 연습하고 싶을 때가 많은데, Klangio 덕분에 이제 어떤 곡이든 악보로 만들 수 있습니다.",
        name: "박지훈",
        title: "피아니스트"
    }
]

export default function TestimonialCarousel() {
    const [current, setCurrent] = useState(0)

    const next = () => setCurrent((current + 1) % testimonials.length)
    const prev = () => setCurrent((current - 1 + testimonials.length) % testimonials.length)

    return (
        <section className="py-20 bg-gradient-to-br from-gray-50 to-blue-50">
            <div className="container mx-auto px-6">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6 }}
                    className="text-center mb-16"
                >
                    <h2 className="text-4xl font-bold mb-4 text-gray-900">
                        전문가들의 평가
                    </h2>
                    <p className="text-xl text-gray-600">
                        아티스트 커뮤니티의 피드백입니다.
                    </p>
                </motion.div>

                <div className="relative max-w-4xl mx-auto">
                    {/* 후기 카드 */}
                    <AnimatePresence mode="wait">
                        <motion.div
                            key={current}
                            initial={{ opacity: 0, x: 100 }}
                            animate={{ opacity: 1, x: 0 }}
                            exit={{ opacity: 0, x: -100 }}
                            transition={{ duration: 0.5 }}
                            className="bg-white rounded-2xl p-12 shadow-xl"
                        >
                            {/* 인용 부호 */}
                            <Quote className="w-16 h-16 text-cyan-500 mb-6" />

                            {/* 인용문 */}
                            <p className="text-xl text-gray-700 mb-8 italic leading-relaxed">
                                {testimonials[current].quote}
                            </p>

                            {/* 프로필 */}
                            <div className="flex items-center gap-4">
                                <div className="w-16 h-16 bg-gradient-to-br from-cyan-400 to-blue-500 rounded-full flex items-center justify-center text-white text-2xl font-bold">
                                    {testimonials[current].name.charAt(0)}
                                </div>
                                <div>
                                    <p className="font-bold text-lg text-gray-900">{testimonials[current].name}</p>
                                    <p className="text-gray-600">{testimonials[current].title}</p>
                                    {testimonials[current].credit && (
                                        <p className="text-sm text-gray-400">{testimonials[current].credit}</p>
                                    )}
                                </div>
                            </div>
                        </motion.div>
                    </AnimatePresence>

                    {/* 네비게이션 버튼 */}
                    <button
                        onClick={prev}
                        className="absolute left-0 top-1/2 -translate-y-1/2 -translate-x-16 w-12 h-12 bg-white rounded-full shadow-lg flex items-center justify-center hover:bg-gray-100 transition-colors"
                        aria-label="이전 후기"
                    >
                        <ChevronLeft className="w-6 h-6 text-gray-700" />
                    </button>
                    <button
                        onClick={next}
                        className="absolute right-0 top-1/2 -translate-y-1/2 translate-x-16 w-12 h-12 bg-white rounded-full shadow-lg flex items-center justify-center hover:bg-gray-100 transition-colors"
                        aria-label="다음 후기"
                    >
                        <ChevronRight className="w-6 h-6 text-gray-700" />
                    </button>

                    {/* 인디케이터 */}
                    <div className="flex justify-center gap-2 mt-8">
                        {testimonials.map((_, index) => (
                            <button
                                key={index}
                                onClick={() => setCurrent(index)}
                                className={`w-3 h-3 rounded-full transition-all ${index === current ? 'bg-cyan-500 w-8' : 'bg-gray-300'
                                    }`}
                                aria-label={`후기 ${index + 1}로 이동`}
                            />
                        ))}
                    </div>
                </div>
            </div>
        </section>
    )
}
