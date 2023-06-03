import ViewHeader from '../components/ViewHeader';
import Box from '@mui/material/Box';
import BasicTable from '../components/DashboardTable1';
import CircularProgress from '@mui/material/CircularProgress';
import { useState } from 'react';
import { useEffect } from 'react';

import './DashboardCustomer.css';

const DashboardCustomer = () => {
    const [data, setData] = useState(null)
    
    // Retrieve data before page is loaded and displayed
        useEffect(() => {
        // Retrieve api key from local storage
        let api_key = localStorage.getItem('API_key')

        // Set up api key authorisation header for request
        const myHeaders = new Headers();
        myHeaders.append("x-api-key", api_key);

        // Config for request
        const requestOptions = {
            method: 'GET',
            headers: myHeaders,
            redirect: 'follow'
        };

        // Send request to retrieve data
        fetch("https://invoice-rendering-api.herokuapp.com/data/get", requestOptions)
        .then(response => response.json())
        .then(result => setData(result))
        .catch(error => console.log('error', error));
    }, [])
    console.log(data)
    return (
        <>
            <ViewHeader/> 
            {
                data ? 
                <>
                    <div className='container1 flexCenter'>
                        <div className='bigCircle'>
                            <div className="circle1C"> 
                                This Month's Spending
                            </div>
                        </div>
                    </div>
    
                    <div className="money" >
                            <h2 style={{ color: 'black',  fontSize: "4rem" }}>${data['sum_expenses']}</h2>
                    </div>	
    
                    <div className="ttitle1C" >
                        <h2 style={{ color: 'black',  fontSize: "1.5rem" }}>This month you've purchased:</h2>
                    </div>
                    
                    <div className='tableContainer flex'>
                        <div className="table1C">
                            <BasicTable productList={data['expenses']}></BasicTable>
                        </div>
                    </div>
                </>
                :
                <Box sx={{width: '100vw', height: '90vh', display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
                    <CircularProgress/>
                </Box>
            }
        </>
        )
}

export default DashboardCustomer