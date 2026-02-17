import { Music, Mail, Github, Twitter, Facebook, Instagram } from 'lucide-react'

export default function Footer() {
    return (
        <footer className="bg-slate-900 text-gray-300">
            <div className="container mx-auto px-6 py-12">
                <div className="grid md:grid-cols-4 gap-8 mb-8">
                    {/* 브랜드 */}
                    <div>
                        <div className="flex items-center gap-2 mb-4">
                            <Music className="w-8 h-8 text-cyan-400" />
                            <span className="text-2xl font-bold text-white">Melodify</span>
                        </div>
                        <p className="text-gray-400 leading-relaxed">
                            AI 기반 음악 악보 변환의 선도적인 플랫폼
                        </p>
                    </div>

                    {/* 제품 */}
                    <div>
                        <h3 className="text-white font-semibold mb-4">제품</h3>
                        <ul className="space-y-2">
                            <li><a href="#" className="hover:text-cyan-400 transition-colors">Piano2Notes</a></li>
                            <li><a href="#" className="hover:text-cyan-400 transition-colors">Guitar2Tabs</a></li>
                            <li><a href="#" className="hover:text-cyan-400 transition-colors">Sing2Notes</a></li>
                            <li><a href="#" className="hover:text-cyan-400 transition-colors">모든 앱 보기</a></li>
                        </ul>
                    </div>

                    {/* 회사 */}
                    <div>
                        <h3 className="text-white font-semibold mb-4">회사</h3>
                        <ul className="space-y-2">
                            <li><a href="#" className="hover:text-cyan-400 transition-colors">소개</a></li>
                            <li><a href="#" className="hover:text-cyan-400 transition-colors">블로그</a></li>
                            <li><a href="#" className="hover:text-cyan-400 transition-colors">채용</a></li>
                            <li><a href="#" className="hover:text-cyan-400 transition-colors">문의하기</a></li>
                        </ul>
                    </div>

                    {/* 지원 */}
                    <div>
                        <h3 className="text-white font-semibold mb-4">지원</h3>
                        <ul className="space-y-2">
                            <li><a href="#" className="hover:text-cyan-400 transition-colors">도움말 센터</a></li>
                            <li><a href="#" className="hover:text-cyan-400 transition-colors">가격</a></li>
                            <li><a href="#" className="hover:text-cyan-400 transition-colors">API 문서</a></li>
                            <li><a href="#" className="hover:text-cyan-400 transition-colors">개인정보 처리방침</a></li>
                        </ul>
                    </div>
                </div>

                {/* 구분선 */}
                <div className="border-t border-gray-700 pt-8">
                    <div className="flex flex-col md:flex-row justify-between items-center gap-4">
                        {/* 저작권 */}
                        <p className="text-gray-400 text-sm text-center md:text-left">
                            © 2026 Melodify. All rights reserved.
                            <br />
                            <span className="text-xs text-cyan-500 font-bold">v2.1 (Live Check: Melodify)</span>
                        </p>

                        {/* 소셜 미디어 */}
                        <div className="flex gap-4">
                            <a href="#" className="w-10 h-10 bg-gray-800 rounded-full flex items-center justify-center hover:bg-cyan-600 transition-colors">
                                <Twitter className="w-5 h-5" />
                            </a>
                            <a href="#" className="w-10 h-10 bg-gray-800 rounded-full flex items-center justify-center hover:bg-cyan-600 transition-colors">
                                <Facebook className="w-5 h-5" />
                            </a>
                            <a href="#" className="w-10 h-10 bg-gray-800 rounded-full flex items-center justify-center hover:bg-cyan-600 transition-colors">
                                <Instagram className="w-5 h-5" />
                            </a>
                            <a href="#" className="w-10 h-10 bg-gray-800 rounded-full flex items-center justify-center hover:bg-cyan-600 transition-colors">
                                <Github className="w-5 h-5" />
                            </a>
                            <a href="#" className="w-10 h-10 bg-gray-800 rounded-full flex items-center justify-center hover:bg-cyan-600 transition-colors">
                                <Mail className="w-5 h-5" />
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    )
}
