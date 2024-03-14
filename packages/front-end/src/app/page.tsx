"use client"

import DataPointTable from '@/components/modules/DataPointTable';
import { useStreamData } from '../presentation/hooks/useStreamData';

export default function Home() {

  const { dataPointItems } = useStreamData(process.env.WS_URL)

  return (
    <main className="flex min-h-screen flex-col items-center justify-between md:px-8 bg-white">
      <div className='flex flex-col gap-4 w-full'
      >
        <DataPointTable dataPoints={dataPointItems.length > 0 ? dataPointItems.slice(0, 100) : []} />
      </div>
    </main>
  );
}
