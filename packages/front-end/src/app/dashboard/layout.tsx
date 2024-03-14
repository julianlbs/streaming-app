"use client"

import Header from '@/presentation/components/layout/Header'
import Footer from '@/presentation/components/layout/Footer'

interface Props {
  children: React.ReactNode
}

export default function DashboardLayout({ children }: Props) {

  return (
    <>
      <Header />
      {children}
      <Footer />
    </>
  )
}