import { create } from 'zustand';

interface StoreProps {
  socketStream?: WebSocket,
  connectWebSocket: (url: string) => WebSocket
}

export const useSocketStore = create<StoreProps>((set) => ({
  connectWebSocket(url) {
    const socket = new WebSocket(url)
    set({ socketStream: socket })
    return socket
  },
}))