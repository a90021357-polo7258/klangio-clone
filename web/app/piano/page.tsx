import LiveDemo from "../components/LiveDemo";

export default function PianoPage() {
    return (
        <main className="min-h-screen bg-slate-900 text-white">
            {/* Header Helper (Same as Layout or just blank for now) */}
            <div className="pt-24">
                <LiveDemo
                    instrument="piano"
                    title="피아노 연주를 악보로 변환하세요"
                    subtitle="다성(Polyphonic) 인식 AI가 양손 악보를 만들어드립니다."
                />
            </div>

            {/* Piano Specific Features Section */}
            <section className="py-16 bg-white text-slate-900">
                <div className="container mx-auto px-6">
                    <h2 className="text-3xl font-bold text-center mb-12">Piano2Notes의 특별한 기능</h2>
                    <div className="grid md:grid-cols-3 gap-8">
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-cyan-600">🎹 다성(Polyphonic) 인식</h3>
                            <p>한 번에 여러 건반을 누르는 화음까지 정확하게 분석하여 악보로 옮겨줍니다.</p>
                        </div>
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-cyan-600">👐 양손 분리 (Beta)</h3>
                            <p>오른손(높은음자리표)과 왼손(낮은음자리표)을 지능적으로 분리하여 피아노 악보 표준을 따릅니다.</p>
                        </div>
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-cyan-600">🎼 Grand Staff 뷰어</h3>
                            <p>피아노 전용 큰보표(Grand Staff) 뷰어를 통해 변환된 악보를 즉시 확인하고 재생할 수 있습니다.</p>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    );
}
