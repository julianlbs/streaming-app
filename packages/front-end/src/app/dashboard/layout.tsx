"use client"

interface Props {
  children: React.ReactNode
}

export default function DashboardLayout({ children }: Props) {

  return (
    <>
      {children}
    </>
  )
}