import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import AutoGraphIcon from '@mui/icons-material/AutoGraph';
import Typography from '@mui/material/Typography';
import { useNavigate } from "react-router-dom";


const Header = () => {

    let navigate = useNavigate(); 
    const routeChange = (ref) =>{ 
      let path = ref; 
      navigate(path);
    }

    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position="fixed" style={{ background: '#ffffff' }}>
                <Toolbar sx={{ marginLeft: 37, marginRight: 37, display: 'flex', justifyContent: 'space-between'}}>
                    <Box display='flex' alignItems={'center'}>
                        <AutoGraphIcon sx={{color: '#4760ff', paddingRight: 1}}/>
                        <Typography variant="h6" component="div" sx={{color: "#4760ff"}}>
                            DashTracker
                        </Typography>
                    </Box>
                    <Box>
                        <Button color="inherit" size='large' sx={{ color: '#4760ff'}} onClick={() => routeChange('Login')}>Login</Button>
                        <Button color="inherit" variant='contained' size='large' sx={{ color: '#ffffff', background: '#4760ff'}} onClick={() => routeChange('GetStarted')} >Sign Up</Button>
                    </Box>
                </Toolbar>
            </AppBar>
        </Box>
    )
}

export default Header