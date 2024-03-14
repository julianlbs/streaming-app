import React from 'react'

interface Props {
  isConnected: boolean
}

function ConnectionBadge(props: Props) {
  const { isConnected } = props


  return (
    <div className='flex gap-2 items-center'>
      {isConnected ? <ConnectedComponent /> : null}
      {!isConnected ? <DisconnectedComponent /> : null}
    </div>
  )
}

export default ConnectionBadge

const ConnectedComponent = () => (
  <>
    <div className='w-[10px] h-[10px] rounded-full bg-green-500' />
    <p>Connected</p>
  </>
)

const DisconnectedComponent = () => (
  <>
    <div className='w-[10px] h-[10px] rounded-full bg-red-500' />
    <p>Disconnected</p>
  </>
)