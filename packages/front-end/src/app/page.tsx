"use client"

import { useEffect, useState } from 'react';
import type { DataPoint } from '../domain/_index';
import DataPointTable from '../components/modules/DataPointTable';

export default function Home() {
  const [dataPointItems, setDataPointItems] = useState<DataPoint[]>([])

  useEffect(() => {
    const socket = new WebSocket('ws://localhost:8765');
    socket.onopen = () => {
      console.log('WebSocket client connected');
      socket.send('stream_data');
    };

    socket.onmessage = (event) => {
      try {
        const resData: { data: DataPoint, req_num: number }[] = JSON.parse(event.data)
        const dataPoints = resData.map(item => ({ ...item.data, timestamp: new Date(item.data.timestamp) }))
        setDataPointItems(prev => dataPoints.concat(prev))
      } catch (err) {
        console.error(err)
      }
    };

    socket.onclose = () => {
      console.log('WebSocket client disconnected');
    };

    return () => {
      socket.close();
    };
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-between md:px-8 bg-white">
      <div className='flex flex-col gap-4 w-full'
      >
        <DataPointTable dataPoints={dataPointItems.length > 0 ? dataPointItems.slice(0, 100) : []} />
      </div>
    </main>
  );
}
