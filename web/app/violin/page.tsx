import LiveDemo from "../components/LiveDemo";

export default function ViolinPage() {
    return (
        <main className="min-h-screen bg-slate-900 text-white">
            <div className="pt-24">
                <LiveDemo
                    instrument="violin"
                    title="바이올린 연주를 악보로 변환하세요"
                    subtitle="현악기의 섬세한 떨림과 더블 스탑(Double Stops)까지 인식합니다."
                />
            </div>

            <section className="py-16 bg-white text-slate-900">
                <div className="container mx-auto px-6">
                    <h2 className="text-3xl font-bold text-center mb-12">Violin2Notes의 특별한 기능</h2>
                    <div className="grid md:grid-cols-3 gap-8">
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-cyan-600">🎻 현악기 특화 분석</h3>
                            <p>바이올린, 비올라, 첼로 등 현악기의 주파수 특성에 맞춰진 AI 모델을 사용합니다.</p>
                        </div>
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-cyan-600">🎼 더블 스탑 지원</h3>
                            <p>Basic Pitch 기술을 통해 두 줄을 동시에 연주하는 화음(Double Stops)도 악보로 표기합니다.</p>
                        </div>
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-cyan-600">✨ 비브라토 보정</h3>
                            <p>연주자의 비브라토로 인한 미세한 음정 변화를 안정적인 노트로 변환합니다.</p>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    );
}
