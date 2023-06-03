import ViewHeader from '../components/ViewHeader';
import Box from '@mui/material/Box';
import BasicTable from '../components/DashboardTable1';
import CircularProgress from '@mui/material/CircularProgress';
import { useState } from 'react';
import { useEffect } from 'react';

import './DashboardBusiness.css';

const DashboardBusiness = () => {

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

    return (
    <>
        <ViewHeader/> 
        {
            data ? 
            <>
                <div className='container1 flexCenter'>
                    <div className="circle2">
                        Top Seller This Month
                    </div>
                    <div className='bigCircle'>
                        <div className="circle1"> 
                            This Month's Income
                        </div>
                    </div>
                    <div className="circle3">
                        <div className='biggestPurchase'>
                            Biggest Purchase <br/> This Month
                        </div>
                    </div>
                </div>

                <div className="money" >
                        <h2 style={{ color: 'black',  fontSize: "4rem" }}>${data['monthly_earnings']}</h2>
                </div>	

                <div className="seller" >
                    {
                        data['top_seller'] === 'None' ?
                        <h2 style={{ color: 'black',  fontSize: "2.5rem" }}>none</h2>
                        :
                        <h2 style={{ color: 'black',  fontSize: "2.5rem" }}>{data['top_seller']['product']}</h2>
                    }
                </div>

                <div className="purchase" > 
                    {
                        data['biggest_purchase'] === 'None' ?
                        <h2 style={{ color: 'black',  fontSize: "2.5rem" }}>none</h2>
                        :
                        <h2 style={{ color: 'black',  fontSize: "2.5rem" }}>{data['biggest_purchase']['product']}</h2>
                    }
                </div>

                <div className="ttitle1" >
                    <h2 style={{ color: 'black',  fontSize: "1.5rem" }}>This month you've sold:</h2>
                </div>

                <div className="ttitle2" >
                    <h2 style={{ color: 'black',  fontSize: "1.5rem" }}>This month you've spent:</h2>
                </div>
                
                <div className='flex'>
                    <div className="table1">
                        <BasicTable productList={data['earnings']}></BasicTable>
                    </div>

                    <div className="table2">
                        <BasicTable productList={data['expenses']}></BasicTable>
                    </div> 
                </div>

                <div className="earnings" >
                        <h2 style={{ color: 'black',  fontSize: "2rem" }}>Monthly Earnings: ${data['sum_earnings']}</h2>
                </div>
            
                <div className="spendings" >
                        <h2 style={{ color: 'black',  fontSize: "2rem" }}>Monthly Spending: ${data['sum_expenses']}</h2>
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

export default DashboardBusiness