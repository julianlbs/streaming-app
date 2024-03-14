"use client"

import React, { type ChangeEvent, type FormEvent, type SetStateAction } from 'react'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { useSocketStore } from '@/presentation/store/useSocketStore'

interface Props {
  connectWebSocket: () => void
  setTicker: (value: SetStateAction<string>) => void
}

function FilterBar(props: Props) {
  const { connectWebSocket } = props

  const { socketStream } = useSocketStore()

  const handleChangeTicker = (e: ChangeEvent<HTMLInputElement>) => {
    props.setTicker(e.target.value)
  }

  const handleStartStream = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    if (socketStream) socketStream.close()
    connectWebSocket()
  }

  return (
    <div className='px-2 md:px-8 py-4 w-full'>
      <div className='border w-full h-full p-2 md:p-4 py-4 rounded-md bg-lime-100 flex flex-col md:flex-row md:items-center gap-3 justify-between'>
        <p className='inline-block w-[15%]'>Dashboard &copy;</p>
        <form className='flex gap-4' onSubmit={handleStartStream}>
          <Input placeholder='Search ticker' className='w-full md:w-[175px]' onChange={handleChangeTicker} />
          <Button type='submit'>Stream</Button>
        </form>
      </div>
    </div>
  )
}

export default FilterBar