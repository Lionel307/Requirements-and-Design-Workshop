import ViewHeader from '../components/ViewHeader';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import { ReactComponent as FileError } from '../images/fileError.svg';
import { useNavigate } from "react-router-dom";

import './UploadError.css';

const Upload = () => {

    let navigate = useNavigate(); 
    const routeChange = (ref) =>{ 
      let path = ref; 
      navigate(path);
    }
    
    return (
    <>
        <ViewHeader /> 
        <div className="errorMsg">
            <Box sx={{ width: 1000, height: 400, background:'#EEEFF0'}}>
                <FileError class='fileError'/>

                <Typography class='malformText' variant="h1" >
                    Invoice Malformed
                </Typography>

                <Typography class='malformMsg' variant="h4" >
                    The invoice you uploaded was malformed. Please try a different invoice.
                </Typography>

                <Button variant='contained' size='large' sx={{ width:180, color: '#ffffff', background: 'white', marginLeft:150, marginLeft: 50}} onClick={() => routeChange('../upload')} >
                    <Typography variant="h4" component="div" sx={{color: "black", fontSize: "1.25rem"}}>
                        OK
                    </Typography>
                </Button>
            </Box>        
        </div>

    </>
    )
}

export default Upload