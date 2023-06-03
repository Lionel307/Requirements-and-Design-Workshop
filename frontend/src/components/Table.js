import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import Pdf from './invoice_render.pdf';

function createData(name, file) {
  return { name, file};
}

const rows = [
  createData('Stationary Warehouse 24/5/2018', 'pdf'),
  createData('Monthly Sales 31/5/2018', 'pdf'),
  createData('Stationary Warehouse 7/6/2018', 'pdf'),
  createData('Stationary Warehouse 21/6/2018', 'pdf'),
  createData('Monthly Sales 30/6/2018', 'pdf'),
];

export default function BasicTable() {

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 700 }} aria-label="simple table">
        <TableHead>
          <TableRow 
            sx={{
              backgroundColor: '#4760ff',
              border: "2px solid black",
              borderBottom: "2px solid black",
              "& th": {
                fontSize: "1.25rem",
                color: '#ffffff'
              }
            }}>
            <TableCell >Name</TableCell>
            <TableCell align="right">File Type</TableCell>
            <TableCell align="right"></TableCell>
            <TableCell align="right"></TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row" style={{ maxWidth:  600}}> {row.name}</TableCell>
              <TableCell align="right" style={{ minWidth:  200}}>{row.file}</TableCell>
              <TableCell align="right" style={{ maxWidth:  100}}>{<Button variant="contained" className="button"> <a className="Button" href={Pdf} download = "invoice_render.pdf"> View</a></Button>}  </TableCell>
              <TableCell align="right" style={{ maxWidth:  10}}>{<Button variant="outlined" color="error">Delete</Button>}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}