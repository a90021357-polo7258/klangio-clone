'use client'

import { motion } from 'framer-motion'
import { ArrowRight, Piano, Guitar, Mic2, Drum, Music2 } from 'lucide-react'


interface ProductCardProps {
    icon: React.ElementType
    name: string
    description: string
    link: string
    index: number
}

function ProductCard({ icon: Icon, name, description, link, index }: ProductCardProps) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: index * 0.1 }}
            whileHover={{ y: -5 }}
            className="bg-white rounded-xl p-6 shadow-lg hover:shadow-2xl transition-all group cursor-pointer"
        >
            {/* 아이콘 */}
            <div className="mb-4 flex justify-center">
                <div className="w-20 h-20 bg-gradient-to-br from-cyan-50 to-blue-50 rounded-full flex items-center justify-center group-hover:scale-110 transition-transform">
                    <Icon className="w-10 h-10 text-cyan-600" />
                </div>
            </div>

            {/* 제목 */}
            <h3 className="text-2xl font-bold mb-3 text-gray-900 group-hover:text-cyan-600 transition-colors text-center">
                {name}
            </h3>

            {/* 설명 */}
            <p className="text-gray-600 mb-4 text-center leading-relaxed">{description}</p>

            {/* 링크 */}
            <a
                href={link}
                className="inline-flex items-center justify-center w-full text-cyan-600 font-semibold hover:text-cyan-700 transition-colors"
            >
                자세히 보기
                <ArrowRight className="ml-2 w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </a>
        </motion.div>
    )
}

const products = [
    {
        icon: Piano,
        name: "Piano2Notes",
        description: "피아노 음악을 악보로 변환합니다.",
        link: "/piano"
    },
    {
        icon: Guitar,
        name: "Guitar2Tabs",
        description: "기타와 베이스를 TAB로 변환합니다.",
        link: "/guitar"
    },
    {
        icon: Mic2,
        name: "Sing2Notes",
        description: "노래를 악보로 변환합니다.",
        link: "/vocal"
    },
    {
        icon: Drum,
        name: "Drum2Notes",
        description: "드럼을 악보로 변환합니다.",
        link: "/drum"
    },
    {
        icon: Music2,
        name: "Violin2Notes",
        description: "현악기를 악보로 변환합니다.",
        link: "/violin"
    },
    {
        icon: Music2,
        name: "Wind2Notes",
        description: "금관/목관악기를 악보로 변환합니다.",
        link: "/wind"
    }
]


export default function ProductCards() {
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
                        악기별 전문 변환 앱
                    </h2>
                    <p className="text-xl text-gray-600 max-w-3xl mx-auto">
                        각 악기에 최적화된 AI 모델로 더욱 정확한 악보 변환을 경험하세요.
                    </p>
                </motion.div>

                <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                    {products.map((product, index) => (
                        <ProductCard key={product.name} {...product} index={index} />
                    ))}
                </div>
            </div>
        </section>
    )
}
