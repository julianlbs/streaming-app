export interface FilterProps {
  ticker: string
}

interface Props {
  socket: WebSocket
  filters: FilterProps
}

export const emitToStreamDataChannel = (props: Props) => {
  const { socket, filters } = props
  const socketJsonData = JSON.stringify({ channel: 'stream_data', filters })
  socket.send(socketJsonData);
}