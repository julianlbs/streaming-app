"use client"

import DataPointTable from '@/components/modules/DataPointTable';
import { useStreamData } from '@/presentation/hooks/useStreamData';
import FilterBar from '../../presentation/components/modules/FilterBar';
import { useState } from 'react';

export default function DashboardPage() {

  const [ticker, setTicker] = useState("")

  const { connect, dataPointItems, webSocket } = useStreamData(process.env.WS_URL, ticker)

  return (
    <div className='bg-gradient-to-b bg-slate-50'>
      <FilterBar connectWebSocket={connect} setTicker={setTicker} isSocketConnected={Boolean(webSocket?.OPEN)} />
      <main className="flex min-h-screen flex-col items-center justify-between md:px-8">
        <div className='flex flex-col gap-4 w-full pb-6'
        >
          <div className='flex justify-end px-2 md:px-0'>
            <p>Lastest {dataPointItems.length >= 100 ? 100 : 0} of {dataPointItems.length}</p>
          </div>
          <DataPointTable dataPoints={dataPointItems} />
        </div>
      </main>
    </div>
  );
}
