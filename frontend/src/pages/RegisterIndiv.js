import { useState } from 'react';
import Typography from '@mui/material/Typography';
import AutoGraphIcon from '@mui/icons-material/AutoGraph';
import Container from '@mui/material/Container';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Link from '@mui/material/Link';
import Button from '@mui/material/Button';
import { useNavigate } from "react-router-dom";
import { Background } from '../components/Background';
import './Register.css';

// some code is used from https://www.geeksforgeeks.org/how-to-develop-user-registration-form-in-reactjs/
// and combined with a free template from https://github.com/mui/material-ui/blob/v5.5.2/docs/data/material/getting-started/templates/sign-up/SignUp.js

const RegisterIndiv = () => {
    // States for registration
    const [bname, setBname] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    // States for checking the errors
    const [error, setError] = useState(false);

    let navigate = useNavigate(); 
    const routeChange = (ref) =>{ 
      let path = ref; 
      navigate(path);
    }

    // Showing error message if error is true
    const errorMessage = () => {
        return (
            <div
                className="error"
                style={{
                    display: error ? '' : 'none',
                }}>
                <Typography className='centerise'variant="subtitle2" style={{color: '#f00'}}>
                    *Invalid Input
                </Typography>
            </div>
        );
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        
        let formdata = new FormData();
        formdata.append("email", email);
        formdata.append("password", password);
        formdata.append("name", bname);
        formdata.append("account", "individual");
    
        const requestOptions = {
            method: 'POST',
            body: formdata,
            redirect: 'follow'
        };
        fetch("https://invoice-rendering-api.herokuapp.com/auth/register", requestOptions)
        .then(response => response.json())
        .then(result => {
            setError(false)
            localStorage.setItem('API_key', result['api_key'])
            localStorage.setItem('account_type', 'individual')
            routeChange('/Upload')
        })
        .catch(() => setError(true));
    };

    return (
    <>
        
        <Container component="main" maxWidth="md">
        <CssBaseline/>
        <Background/>
        
        <div>
            <h1>DashTracker</h1>
        </div>
        <div className="centerise">
            <Grid size="Large">
            <div className="centerise">
                <AutoGraphIcon className="mainLogo" fontSize="large" sx={{color: '#4760ff'}}/>
            </div>
            </Grid>
        </div>
        
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}    
        >
            <Typography component="h1" variant="h3">
                Create an individual account
            </Typography>
            <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
                <Grid container spacing={3}>
                    <Grid item xs={12}>
                        <TextField
                            required
                            fullWidth
                            id="name"
                            label="Name"
                            name="name"
                            onChange={e => setBname(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={12}>
                        <TextField
                            required
                            fullWidth
                            id="email"
                            label="Email Address"
                            name="email"
                            autoComplete="email"
                            onChange={e => setEmail(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={12}>
                        <TextField
                            required
                            fullWidth
                            name="password"
                            label="Password"
                            type="password"
                            id="password"
                            autoComplete="new-password"
                            onChange={e => setPassword(e.target.value)}
                        />
                    </Grid>
                </Grid>
                    <Button type="submit" fullWidth variant="contained"sx={{ mt: 3, mb: 2 }}>
                        Register
                    </Button>
                <Grid container justifyContent="flex-end">
                    <Grid item>
                        <div className="messages">
                            {errorMessage()}
                        </div>
                        <Link href="#" variant="body2" onClick={() => routeChange('/Login')}>
                            Already have an account? Sign in here
                        </Link>
                    </Grid>
                </Grid>
            </Box>
        </Box>
      </Container>
    </>
    )
}

export default RegisterIndiv