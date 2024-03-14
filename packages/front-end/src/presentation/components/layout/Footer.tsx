import React from 'react'

function Footer() {
  return (
    <footer className='px-16 pt-16 border-t bg-gradient-to-bl from-slate-200 to-lime-100'>
      <p className="text-center py-11 text-lime-950">
        &copy; {new Date().getFullYear()} Streaming App &copy; All Rights Reserved
      </p>
    </footer>
  )
}

export default Footer