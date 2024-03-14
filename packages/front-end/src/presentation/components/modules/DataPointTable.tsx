"use client"

import React, { useCallback } from 'react'
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import type { DataPoint } from '@/domain/_index'

interface Props {
  dataPoints: DataPoint[]
  quantityPerPage?: number
}

function DataPointTable(props: Props) {
  const { dataPoints, quantityPerPage } = props

  const getDataPointsSlice = useCallback((quantity = 100) => dataPoints.slice(0, quantity), [dataPoints])

  return (
    <Table className='w-full'>
      <TableHeader>
        <TableRow>
          <TableHead className='md:w-[300px]'>Time</TableHead>
          <TableHead className=''>Ticker</TableHead>
          <TableHead className=''>Price</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody className='w-full'>
        {getDataPointsSlice(quantityPerPage).map((item, i) => (
          <TableRow key={i + ' - ' + item.timestamp.toISOString()}>
            <TableCell className=''>{item.timestamp.toLocaleString()}</TableCell>
            <TableCell>{item.ticker}</TableCell>
            <TableCell className='font-medium'>{item.price}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  )
}

export default DataPointTable