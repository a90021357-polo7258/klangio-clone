import LiveDemo from "../components/LiveDemo";

export default function DrumPage() {
    return (
        <main className="min-h-screen bg-slate-900 text-white">
            <div className="pt-24">
                <LiveDemo
                    instrument="drum"
                    title="드럼 비트를 악보로 변환하세요"
                    subtitle="AI가 리듬을 분석하여 드럼 악보(Drum Tab)를 생성합니다."
                />
            </div>

            {/* Drum Specific Features Section */}
            <section className="py-16 bg-white text-slate-900">
                <div className="container mx-auto px-6">
                    <h2 className="text-3xl font-bold text-center mb-12">Drum2Notes의 특별한 기능</h2>
                    <div className="grid md:grid-cols-3 gap-8">
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-purple-600">🥁 리듬 분석</h3>
                            <p>복잡한 비트와 리듬 패턴을 정밀하게 분석하여 드럼 악보로 옮겨줍니다.</p>
                        </div>
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-purple-600">🎧 3-Part 분리 (Beta)</h3>
                            <p>Kick, Snare, Hi-hat을 주파수별로 구분하여 기본적인 드럼 구성을 표현합니다.</p>
                        </div>
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-purple-600">🎼 Drum MIDI 생성</h3>
                            <p>표준 General MIDI 포맷으로 저장되어 시퀀서나 가상악기에서 바로 사용할 수 있습니다.</p>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    );
}
