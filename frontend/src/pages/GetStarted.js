import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Chip from '@mui/material/Chip';
import Stack from '@mui/material/Stack';
import { useNavigate } from "react-router-dom";
import { Background } from '../components/Background';
import * as React from 'react';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import { ReactComponent as Business } from '../images/business.svg';
import { ReactComponent as Individual } from '../images/individual.svg';

// some code is used from https://www.geeksforgeeks.org/how-to-develop-user-registration-form-in-reactjs/
// and combined with a free template from https://github.com/mui/material-ui/blob/v5.5.2/docs/data/material/getting-started/templates/sign-up/SignUp.js

const GetStarted = () => {

    let navigate = useNavigate(); 
    const routeChange = (ref) =>{ 
      let path = ref; 
      navigate(path);
    }

    return (
    <>
        
        <Container component="main" maxWidth="md">
            <CssBaseline />
            <Background/>
            <div>
                <h1>DashTracker</h1>
            </div>
            
            <Typography component="h1" variant="h3">
                Choose an account
            </Typography>
            <br/>
            <Grid container spacing={1}>
                <Grid item xs={12}>
                        <Card variant='outlined' sx={{ minWidth: 275, borderRadius: 4.5, boxShadow: 5}} style={{background: 'linear-gradient(to right top, #4760ff, #22e0e0)'}}>
                            <Grid container spacing={2} className='indivCard'>
                                <Grid item xs={6}>
                                    <Card variant='outlined' sx={{ minWidth: 275, borderRadius: 4.5, boxShadow: 5}} style={{backgroundColor: "#ffffff"}}>
                                        <CardContent>
                                            <div class='centerise'>
                                                <Business className="receiveLogo"/>
                                            </div>
                                    
                                            <Stack direction="row" spacing={1} className="serviceTitle">
                                                <Chip label="Business" style={{color: '#ffffff', backgroundColor: '#4760ff'}}/>
                                            </Stack>
                                        </CardContent>
                                        <CardActions className="centerise">
                                            <Button size="medium" endIcon={<ArrowForwardIosIcon/>} onClick={() => routeChange('../Register')}>Next</Button>
                                        </CardActions>
                                    </Card>
                                </Grid>

                                <Grid item xs={6}>
                                    <Card variant='outlined' sx={{ minWidth: 275, borderRadius: 4.5, boxShadow: 5}} style={{backgroundColor: "#ffffff"}}>
                                        <CardContent>
                                            <div class='centerise'>
                                                <Individual className="valLogo"/>
                                            </div>
                                    
                                            <Stack direction="row" spacing={1} className="serviceTitle">
                                                <Chip label="Individual" style={{color: '#ffffff', backgroundColor: '#4760ff'}}/>
                                            </Stack>
                                        </CardContent>
                                        <CardActions className="centerise">
                                            <Button size="medium" endIcon={<ArrowForwardIosIcon/>} onClick={() => routeChange('../Registerindiv')}>Next</Button>
                                        </CardActions>
                                    </Card>
                                </Grid>
                            </Grid>
                        </Card>
                </Grid>
            </Grid>
      </Container>
    </>
    )
}

export default GetStarted