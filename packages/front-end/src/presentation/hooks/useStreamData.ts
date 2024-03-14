import { useEffect, useState, type SetStateAction } from 'react';
import type { DataPoint } from '@/domain/_index';
import { useSocketStore } from '@/presentation/store/useSocketStore';
import { emitToStreamDataChannel } from '@/infra/stream/emit-event';

export const useStreamData = (url = 'ws://localhost:8765', ticker = "") => {
  const [dataPointItems, setDataPointItems] = useState<DataPoint[]>([])
  const [webSocket, setWebSocket] = useState<WebSocket | undefined>(undefined)

  const { connectWebSocket } = useSocketStore()

  const connect = () => {
    setWebSocket(connectWebSocket(url))
  }

  useEffect(() => {
    if (webSocket) {
      try {
        webSocket.onopen = () => { onSocketOpen(webSocket, ticker) };
        webSocket.onmessage = (event) => { onSocketMessage(event, setDataPointItems) };
        webSocket.onclose = () => { onSocketClose() };
      } catch (err) {
        console.error(err)
      }
    }

    return () => {
      webSocket && webSocket.close();
    };
  }, [url, webSocket, ticker]);

  return {
    connect,
    dataPointItems,
    webSocket
  }
}

const onSocketOpen = (socket: WebSocket, tickerSearch: string) => {
  console.info('WebSocket client connected');
  emitToStreamDataChannel({ socket, filters: { ticker: tickerSearch } })
}

const onSocketMessage = (event: MessageEvent<any>, setDataPointItems: (value: SetStateAction<DataPoint[]>) => void) => {
  const resData: { data: DataPoint, req_num: number }[] = JSON.parse(event.data)
  if (typeof resData === 'object') {
    const dataPoints = resData?.map(item => ({ ...item.data, timestamp: new Date(item.data.timestamp) }))
    Array.isArray(dataPoints) && setDataPointItems(prev => dataPoints.concat(prev))
  }
}

const onSocketClose = () => {
  console.info('WebSocket client disconnected');
}