"use client"

import Image from 'next/image';
import ShimmerButton from '../presentation/components/ui/shimmer-button';
import { useRouter } from 'next/navigation';

export default function Home() {
  const router = useRouter()

  const handleEnterDashboard = () => {
    router.push('/dashboard')
  }

  return (
    <main className="min-h-screen max-h-screen overflow-hidden grid grid-cols-12">
      <div className='hidden lg:block lg:col-span-6 bg-white'>
        <Image src="/trading-image.jpg" alt="Trading image" width={1920} height={3413} priority className='object-cover' />
      </div>
      <div className='col-span-12 lg:col-span-6 bg-lime-300 flex flex-col justify-center items-center gap-8 h-screen'>
        <h1 className='text-6xl text-center'>Trading for the professionals</h1>
        <ShimmerButton onClick={handleEnterDashboard}>Enter dashboard</ShimmerButton>
      </div>
    </main>
  );
}
