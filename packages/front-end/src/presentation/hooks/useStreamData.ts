import { useEffect, useState, type SetStateAction } from 'react';
import type { DataPoint } from '@/domain/_index';

export const useStreamData = (url = 'ws://localhost:8765') => {
  const [dataPointItems, setDataPointItems] = useState<DataPoint[]>([])
  const [webSocket, setWebSocket] = useState<WebSocket | undefined>(undefined)

  useEffect(() => {
    const socket = new WebSocket(url);
    setWebSocket(socket)

    if (socket) {
      try {
        socket.onopen = () => { onSocketOpen(socket) };
        socket.onmessage = (event) => { onSocketMessage(event, setDataPointItems) };
        socket.onclose = () => { onSocketClose() };
      } catch (err) {
        console.error(err)
      }
    }

    return () => {
      socket && socket.close();
    };
  }, [url]);

  return {
    dataPointItems,
    webSocket
  }
}

const onSocketOpen = (socket: WebSocket) => {
  console.info('WebSocket client connected');
  const socketJsonData = JSON.stringify({ channel: 'stream_data', filters: { tickers: ["TICKER_1"] } })
  socket.send(socketJsonData);
}

const onSocketMessage = (event: MessageEvent<any>, setDataPointItems: (value: SetStateAction<DataPoint[]>) => void) => {
  const resData: { data: DataPoint, req_num: number }[] = JSON.parse(event.data)
  if (typeof resData === 'object') {
    const dataPoints = resData?.map(item => ({ ...item.data, timestamp: new Date(item.data.timestamp) }))
    setDataPointItems(prev => dataPoints.concat(prev))
  }
}

const onSocketClose = () => {
  console.info('WebSocket client disconnected');
}