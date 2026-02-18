import LiveDemo from "../components/LiveDemo";

export default function GuitarPage() {
    return (
        <main className="min-h-screen bg-slate-900 text-white">
            <div className="pt-24">
                <LiveDemo
                    instrument="guitar"
                    title="기타 연주를 TAB 악보로 변환하세요"
                    subtitle="AI가 연주를 분석하여 Guitar Pro 호환 TAB 악보를 생성합니다."
                />
            </div>

            {/* Guitar Specific Features Section */}
            <section className="py-16 bg-white text-slate-900">
                <div className="container mx-auto px-6">
                    <h2 className="text-3xl font-bold text-center mb-12">Guitar2Tabs의 특별한 기능</h2>
                    <div className="grid md:grid-cols-3 gap-8">
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-orange-600">🎸 6현 TAB 변환</h3>
                            <p>기타의 6줄(EADGBE)을 자동으로 인식하여 연주하기 가장 편한 핑거링을 찾아줍니다.</p>
                        </div>
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-orange-600">🎼 리듬 & 코드 분석</h3>
                            <p>단음 솔로 연주뿐만 아니라 스트럼과 코드 진행까지 분석하여 악보에 표기합니다.</p>
                        </div>
                        <div className="p-6 bg-slate-50 rounded-xl">
                            <h3 className="text-xl font-bold mb-3 text-orange-600">📥 Guitar Pro 호환</h3>
                            <p>생성된 MusicXML 파일은 Guitar Pro, TuxGuitar 등에서 열어보고 수정할 수 있습니다.</p>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    );
}
