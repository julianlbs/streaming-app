import React from 'react'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'

function Header() {
  return (
    <header className='border-b shadow-sm p-4 flex justify-between items-center'>
      <p className='text-lime-800'>&copy; Streaming App</p>
      <Avatar>
        <AvatarImage src="https://picsum.photos/200/300" />
        <AvatarFallback>UN</AvatarFallback>
      </Avatar>
    </header>
  )
}

export default Header