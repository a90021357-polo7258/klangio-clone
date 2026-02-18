import LiveDemo from "../components/LiveDemo";

export default function WindPage() {
    return (
        <main className="min-h-screen bg-slate-900 text-white">
            <div className="pt-24">
                <LiveDemo
                    instrument="wind"
                    title="관악기 연주를 악보로 변환하세요"
                    subtitle="플루트, 색소폰, 클라리넷 등 관악기의 단선율을 정밀하게 분석합니다."
                />
            </div>

            <section className="py-16 bg-white text-slate-900">
                <div className="container mx-auto px-6">
                    <h2 className="text-3xl font-bold text-center mb-12">Wind2Notes의 특별한 기능</h2>
                    <div className="grid md:grid-cols-3 gap-8">
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-cyan-600">🎷 관악기 호흡 인식</h3>
                            <p>연주자의 호흡과 프레이징을 고려하여 자연스러운 멜로디 라인을 생성합니다.</p>
                        </div>
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-cyan-600">🎵 단선율(Monophonic) 최적화</h3>
                            <p>pYIN 알고리즘을 사용하여 단선율 악기의 정확한 피치를 추적합니다.</p>
                        </div>
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-cyan-600">🎺 다양한 관악기 지원</h3>
                            <p>목관악기(Woodwinds)와 금관악기(Brass)의 다양한 음색을 모두 지원합니다.</p>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    );
}
