import HeroSection from './components/HeroSection'
import ProcessSteps from './components/ProcessSteps'
import LiveDemo from './components/LiveDemo'
import ProductCards from './components/ProductCards'
import TestimonialCarousel from './components/TestimonialCarousel'
import FAQ from './components/FAQ'
import Footer from './components/Footer'

export default function Home() {
  return (
    <div className="min-h-screen">
      <HeroSection />
      <ProcessSteps />
      <LiveDemo />
      <ProductCards />
      <TestimonialCarousel />
      <FAQ />
      <Footer />
    </div>
  )
}

