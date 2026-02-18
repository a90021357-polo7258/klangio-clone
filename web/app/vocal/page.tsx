import LiveDemo from "../components/LiveDemo";

export default function VocalPage() {
    return (
        <main className="min-h-screen bg-slate-900 text-white">
            <div className="pt-24">
                <LiveDemo
                    instrument="vocal"
                    title="보컬 멜로디를 악보로 변환하세요"
                    subtitle="흥얼거림이나 노래를 AI가 분석하여 단선율 악보(Lead Sheet)로 만들어줍니다."
                />
            </div>

            {/* Vocal Specific Features Section */}
            <section className="py-16 bg-white text-slate-900">
                <div className="container mx-auto px-6">
                    <h2 className="text-3xl font-bold text-center mb-12">Sing2Notes의 특별한 기능</h2>
                    <div className="grid md:grid-cols-3 gap-8">
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-pink-600">🎤 단선율 추출</h3>
                            <p>목소리의 음정을 정밀하게 추적(Pitch Tracking)하여 멜로디 라인을 자동으로 생성합니다.</p>
                        </div>
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-pink-600">🎵 허밍 & 노래</h3>
                            <p>가사가 있는 노래뿐만 아니라, 아이디어가 떠오를 때 흥얼거린 멜로디도 악보로 변환해줍니다.</p>
                        </div>
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-pink-600">🎼 쉬운 편곡 시작</h3>
                            <p>생성된 MIDI 파일을 DAW로 가져와서 본격적인 편곡 작업을 시작해보세요.</p>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    );
}
