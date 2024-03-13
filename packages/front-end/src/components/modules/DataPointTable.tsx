"use client"

import React from 'react'
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import type { DataPoint } from '../../domain/_index'

interface Props {
  dataPoints: DataPoint[]
}

function DataPointTable(props: Props) {
  const { dataPoints } = props
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
        {dataPoints.map((item, i) => (
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