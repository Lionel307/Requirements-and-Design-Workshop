import * as React from 'react';
import { useState, useEffect } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function createData(name, quantity, price) {
  return { name, quantity, price};
}

function itemData(productList) {
  const rows = []
  for (let i = 0; i < productList.length; i++) {
    let data = createData(
      productList[i]['product'],
      productList[i]['quantity'],
      productList[i]['cost'],
    )
    rows.push(data)
  }
  return rows
}

export default function BasicTable({ productList }) {
  const [rows, setRows] = useState([])

  useEffect(() => {
    if (productList) {
      setRows(itemData(productList))
    }
  }, [productList])

  return (
    <TableContainer component={Paper} sx={{ maxHeight: 290 }}>
      <Table stickyHeader sx={{ minWidth: 700 }} aria-label="sticky table">
        <TableHead>
          <TableRow 
            sx={{
              "& th": {
                fontSize: "1.25rem",
                color: '#000000'
              }
            }}>
            <TableCell sx={{backgroundColor: '#EEEFF0'}}>Name</TableCell>
            <TableCell sx={{backgroundColor: '#EEEFF0'}} align="right">Quantity</TableCell>
            <TableCell sx={{backgroundColor: '#EEEFF0'}} align="right">Price</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row" style={{ maxWidth:  700}}> {row.name}</TableCell>
              <TableCell align="right" style={{ minWidth:  200}}>{row.quantity}</TableCell>
              <TableCell align="right" style={{ maxWidth:  100}}> {row.price} </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}