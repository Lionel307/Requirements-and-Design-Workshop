import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import AutoGraphIcon from '@mui/icons-material/AutoGraph';
import Typography from '@mui/material/Typography';
import { useNavigate } from "react-router-dom";


const ViewHeader = () => {

    let navigate = useNavigate(); 
    const routeChange = (ref) =>{ 
      let path = ref; 
      navigate(path);
    }

    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position="fixed" style={{ background: '#ffffff' }}>
                <Toolbar sx={{ marginLeft: 36, display: 'flex'}}>
                    <Box display='flex' alignItems={'center'}>
                        <AutoGraphIcon sx={{color: '#4760ff', paddingRight: 1}}/>
                        <Typography variant="h6" component="div" sx={{color: "#4760ff"}}>
                            DashTracker
                        </Typography>
                    </Box>
                    <Box sx={{ marginLeft: 5, display: 'flex' }}>
                        <Button size='large' sx={{ marginLeft: 3, color: "#4760ff"}} onClick={() => {
                            if (localStorage.getItem('account_type') === 'business') {
                                routeChange('../dashboardb')
                            }
                            else {
                                routeChange('../dashboardc')
                            }
                        }} >
                            <Typography variant="h7" component="div" sx={{color: "#4760ff"}}>
                                Dashboard
                            </Typography>
                        </Button>
                    </Box>
                    <Box>
                        <Button size='large' sx={{ marginLeft: 3, color: "#4760ff"}} onClick={() => routeChange('../view')} >
                            <Typography variant="h7" component="div" sx={{color: "#4760ff"}}>
                                View E-Invoices
                            </Typography>
                        </Button>
                    </Box>
                    <Box>
                        <Button size='large' sx={{ marginLeft: 3, color: "#4760ff"}} onClick={() => routeChange('../upload')} >
                            <Typography variant="h7" component="div" sx={{color: "#4760ff"}}>
                                Upload E-Invoice
                            </Typography>
                        </Button>
                    </Box>
                    <Box sx={{ marginLeft: 65, display: 'flex' }}>
                        <Button color="inherit" variant='contained' size='large' sx={{ color: '#ffffff', background: '#4760ff'}} onClick={() => routeChange('../')} >Log Out</Button>
                    </Box>
                </Toolbar>
            </AppBar>
        </Box>
    )
}

export default ViewHeader