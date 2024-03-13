"use client"

import { useEffect, useState } from 'react';
import io from 'socket.io-client'
import useSWR from 'swr'

const socket = io('http://localhost:5001');

export default function Home() {
  const [data, setData] = useState([])

  const swr = useSWR('socketConnection', () => {
    const connection = socket.connect()
    return connection
  })

  useSWR(swr.data && 'dummy_data', () => {
    swr.data?.emit('create', (data: any) => {
      // setData(prev => prev.concat(data))
      console.log(data)
    })
    swr.data?.on('data_point', (data) => {
      console.log(data)
    })
  })
  console.log('test')
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24 bg-white">
      <div className='flex flex-col gap-4'
      >
        {/* {data.map((item, i) => (
          <div key={i}>{JSON.stringify(item)}</div>
        ))} */}
      </div>
    </main>
  );
}
