import ViewHeader from '../components/ViewHeader';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import { ReactComponent as CurveArrowDown } from '../images/CurveArrowDown.svg';
import { ReactComponent as InvoiceUpload } from '../images/uploadFile.svg';
import { ReactComponent as UploadButton } from '../images/upload.svg';
import { useState } from 'react';
import './Upload.css';

const Upload = () => {
    const [selectedFile, setFile] = useState(null)

    // States for checking the errors
    const [submitted, setSubmitted] = useState(false);

    // Showing success message
    const successMessage = () => {
        return (
        <div
            className="successMSG"
            style={{
            display: submitted ? '' : 'none',
            }}>
            <Typography className='centerise'variant="subtitle2" style={{color: '#525252'}}>
                Successfully uploaded invoice
            </Typography>
        </div>
        );
    };

    return (
    <>
        <ViewHeader /> 
        <h1> Upload Invoice </h1>		
        <div className="upload">
            <InvoiceUpload className='upload'/>
    
        </div>
        <div className="arrowDown">
            <CurveArrowDown className='arrowDown'/>
    
        </div>
        <div className="uploadBar">
            <Box sx={{ width: 850, height: 50, background:'#B2C3FF'}} className='uploadText flexUpload' >
                <div className='uploadPic'>
                    <UploadButton className='uploadButton'/>
                </div>
                <div className='barText'>
                    <Typography variant="h5" >
                        Upload your E-Invoice here
                    </Typography>
                </div>
    
            </Box>        
        </div>

        <div className='fileUpload'>
            <input type="file" onChange={e => {
                setFile(e.target.files[0]);

            }} accept = '.xml' id='input'/>
        </div>

        <Button variant='contained' size='large' sx={{ width:180, color: '#ffffff', background: '#4760ff', marginLeft:151, marginTop: 4}} 
        onClick={() => 
            {                
                // Retrieve api key from local storage
                let api_key = localStorage.getItem('API_key')

                const myHeaders = new Headers();
                myHeaders.append("x-api-key", api_key);
                
                const formdata = new FormData();
                formdata.append("xml_file", selectedFile, selectedFile.name);
                
                const requestOptions = {
                    method: 'POST',
                    headers: myHeaders,
                    body: formdata,
                    redirect: 'follow'
                };
                
                fetch("https://invoice-rendering-api.herokuapp.com/render/html", requestOptions)
                .then(response => response.json())
                .then(result => {
                    setSubmitted(true);
                    console.log(result)
                    successMessage()
                    
                })
                .catch(error => console.log(error));

            }
        } >
            <Typography variant="h4" component="div" sx={{color: "white", fontSize: "1.25rem"}}>
                Upload
            </Typography>
        </Button>
        <Grid container justifyContent="flex-end">
            <Grid item>
                <div className="messages">
                    {successMessage()}
                </div>
            </Grid>
        </Grid>
    </>
    )
}

export default Upload