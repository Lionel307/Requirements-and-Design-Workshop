import * as React from 'react';
import { useRef } from 'react';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Divider from '@mui/material/Divider';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import Chip from '@mui/material/Chip';
import Stack from '@mui/material/Stack';
import Header from '../components/Header';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import AutoGraphIcon from '@mui/icons-material/AutoGraph';
import { ReactComponent as CurveArrowDown } from '../images/CurveArrowDown.svg';
import { ReactComponent as CurveArrowUp } from '../images/CurveArrowUp.svg';
import { ReactComponent as ArrowDown } from '../images/arrowDown.svg';
import { ReactComponent as RenderIcon } from '../images/renderIcon.svg';
import { ReactComponent as RenderIconComp } from '../images/renderIconComp.svg';
import { ReactComponent as StorageLogo } from '../images/storageIcon.svg';
import { ReactComponent as Angry } from '../images/angry.svg';
import { ReactComponent as Money } from '../images/money.svg';
import { ReactComponent as Pie } from '../images/pie.svg';
import { ReactComponent as People } from '../images/people.svg';
import { ReactComponent as Income } from '../images/income.svg';
import { ReactComponent as Folder } from '../images/folder.svg';
import { ReactComponent as Monitor } from '../images/monitor.svg';
import { useNavigate } from "react-router-dom";

import './Home.css';

const Home = () => {
    const scrollVal = useRef(null)
    const scrollStor = useRef(null)
    const scrollTo = (ref) => ref.current.scrollIntoView()  
    
    let navigate = useNavigate(); 
    const routeChange = (ref) =>{ 
      let path = ref; 
      navigate(path);
    }

    return (
        <>
            <Header />            
            <h1>Track your E-Commerce spending and earnings.</h1>

            <Grid container spacing={1} sx={{ paddingLeft: 40, paddingRight: 40, paddingBottom: 9}}>
                <Grid item xs={12}>
                        <Card variant='outlined' sx={{ minWidth: 275, borderRadius: 4.5, boxShadow: 5}} style={{background: 'linear-gradient(to right top, #4760ff, #22e0e0)'}}>
                            <Grid container spacing={3} className='indivCard'>
                                <Grid item xs={4}>
                                    <Card variant='outlined' sx={{ minWidth: 275, borderRadius: 4.5, boxShadow: 5}} style={{backgroundColor: "#ffffff"}}>
                                        <CardContent>
                                            <div class='centerise'>
                                                <People className="receiveLogo"/>
                                            </div>
                                    
                                            <Stack direction="row" spacing={1} className="serviceTitle">
                                                <Chip label="Flexible Use" style={{color: '#ffffff', backgroundColor: '#4760ff'}}/>
                                            </Stack>

                                            <Typography className='centerise'variant="h5" style={{color: '#303030'}}>
                                                Choose to track your business' income or use as an individual to monitor your personal expenses. 
                                            </Typography>
                                        </CardContent>
                                        <CardActions className="centerise">
                                            <Button size="medium" endIcon={<ArrowForwardIosIcon/>} onClick={() => routeChange('GetStarted')}>Get Started</Button>
                                        </CardActions>
                                    </Card>
                                </Grid>

                                <Grid item xs={4}>
                                    <Card variant='outlined' sx={{ minWidth: 275, borderRadius: 4.5, boxShadow: 5}} style={{backgroundColor: "#ffffff"}}>
                                        <CardContent>
                                            <div class='centerise'>
                                                <Pie className="valLogo"/>
                                            </div>
                                    
                                            <Stack direction="row" spacing={1} className="serviceTitle">
                                                <Chip label="Dashboard" style={{color: '#ffffff', backgroundColor: '#4760ff'}}/>
                                            </Stack>

                                            <Typography className='centerise'variant="h5" style={{color: '#303030'}}>
                                                View a breakdown of your monthly earnings and spending in one place.
                                            </Typography>
                                        </CardContent>
                                        <CardActions className="centerise">
                                            <Button size="medium" endIcon={<KeyboardArrowDownIcon/>} onClick={() => scrollTo(scrollVal)}>Learn More</Button>
                                        </CardActions>
                                    </Card>
                                </Grid>

                                <Grid item xs={4}>
                                    <Card variant='outlined' sx={{ minWidth: 275, borderRadius: 4.5, boxShadow: 5}} style={{backgroundColor: "#ffffff"}}>
                                        <CardContent>
                                            <div class='centerise'>
                                                <StorageLogo className="valLogo"/>
                                            </div>
                                    
                                            <Stack direction="row" spacing={1} className="serviceTitle">
                                                <Chip label="Storage" style={{color: '#ffffff', backgroundColor: '#4760ff'}}/>
                                            </Stack>

                                            <Typography className='centerise'variant="h5" style={{color: '#303030'}}>
                                                Store your invoices in an online database where you can access them anytime.
                                            </Typography>
                                        </CardContent>
                                        <CardActions className="centerise">
                                            <Button size="medium" endIcon={<KeyboardArrowDownIcon/>} onClick={() => scrollTo(scrollStor)}>Learn More</Button>
                                        </CardActions>
                                    </Card>
                                </Grid>
                            </Grid>
                        </Card>
                </Grid>
            </Grid>
            <br></br>
            <div className="centerise">
                <AutoGraphIcon className="mainLogo" fontSize="large" sx={{color: '#4760ff'}}/>
            </div>
            <h1> Why Us?</h1>
            <div className="margins">
                <Typography className='centerise'variant="h5" style={{color: '#5e5e5e'}}>
                    With DashTracker, you can view a monthly breakdown of money flow through your invoices whether you're a business or
                    an individual. No need to understand UBL XML, simply upload your invoices and we'll handle the rest for you. 
                </Typography>
            </div>

            <Grid container spacing={1} sx={{ paddingLeft: 60, paddingRight: 60, paddingBottom: 9, paddingTop: 8}}>
                <Grid item xs={12}>
                        <Grid container spacing={3} sx={{}}>
                            <Grid item xs={4}>
                                <Card variant='outlined' sx={{ minWidth: 275, borderRadius: 4.5, boxShadow: 5}} style={{background: 'linear-gradient(to right top, #4760ff, #22e0e0)'}}>
                                    <div className='centerise'>
                                        <Angry className='moneyIcon'/>
                                    </div>
                                </Card>
                            </Grid>
                            <Grid item xs={4}>
                                <Card variant='outlined' sx={{ minWidth: 275, borderRadius: 4.5, boxShadow: 5}} style={{background: 'linear-gradient(to top, #4760ff, #22e0e0)'}}>
                                    <div className='centerise'>
                                        <Money className='moneyIcon'/>
                                    </div>
                                </Card>
                            </Grid>
                            <Grid item xs={4}>
                                <Card variant='outlined' sx={{ minWidth: 275, borderRadius: 4.5, boxShadow: 5}} style={{background: 'linear-gradient(to left top, #4760ff, #22e0e0)'}}>
                                    <div className='centerise'>
                                        <Income className='moneyIcon'/>
                                    </div>
                                </Card>
                            </Grid>
                        </Grid>
                </Grid>
            </Grid>
            <Divider variant="middle" />

            <Grid container spacing={2} sx={{ paddingLeft: 40, paddingRight: 40}} ref={scrollVal}>
                <Grid item xs={6}>
                    <h3> Want to compare earnings and expenses? </h3>
                    <Typography variant="h5" style={{color: '#5e5e5e'}}>
                        View breakdowns of both your monthly monetary gain and losses through your invoices to monitor your business' progress. 
                    </Typography>
                    <h4> Dashboard Features </h4>
                    
                    <Card variant='outlined' sx={{ minWidth: 275, borderRadius: 4.5, boxShadow: 4}} style={{background: 'linear-gradient(to right top, #4760ff, #22e0e0)'}}>
                        <List>
                            <ListItem>
                                <ListItemIcon>
                                    <CheckCircleIcon sx={{ color: '#ffffff'}}/>
                                </ListItemIcon>
                                <Typography variant="h5" style={{color: '#ffffff'}}> Monthly Earnings</Typography>
                            </ListItem>

                            <ListItem>
                                <ListItemIcon>
                                    <CheckCircleIcon sx={{ color: '#ffffff'}}/>
                                </ListItemIcon>
                                <Typography variant="h5" style={{color: '#ffffff'}}> Summary of monthly income and expenses </Typography>
                            </ListItem>

                            <ListItem>
                                <ListItemIcon>
                                    <CheckCircleIcon sx={{ color: '#ffffff'}}/>
                                </ListItemIcon>
                                <Typography variant="h5" style={{color: '#ffffff'}}> Lists biggest factors of monthly earnings</Typography>
                            </ListItem>

                            <ListItem>
                                <ListItemIcon>
                                    <CheckCircleIcon sx={{ color: '#ffffff'}}/>
                                </ListItemIcon>
                                <Typography variant="h5" style={{color: '#ffffff'}}> All in one place</Typography>
                            </ListItem>
                        </List>
                    </Card>
                    <div className="getStarted">
                        <Button size="large" variant="contained" endIcon={<ArrowForwardIosIcon />} sx={{ background: 'linear-gradient(to right top, #4760ff, #22e0e0)'}}  onClick={() => routeChange('GetStarted')}>Get Started</Button>
                    </div>
                </Grid>

                <Grid item xs={6}>
                    <br/>
                    <br/>
                    <br/>
                    <div className="alignLeft">
                        <Folder class='valIcon'/>
                        <CurveArrowDown className="downArrow"/>
                    </div>
                    
                    <div className="alignRight">
                        <CurveArrowUp className="upArrow"/>
                        <Monitor class='valIcon'/>
                    </div>
                </Grid>
            </Grid>
            
            <Divider variant="middle" />

            <Grid container spacing={2} sx={{ paddingLeft: 40, paddingRight: 40}} ref={scrollStor}>
                <Grid item xs={6}>
                    <br/>
                    <div className="centerise">
                        <ArrowDown className="downArrow"/>
                        <RenderIconComp className="renderIcon"/>
                        <ArrowDown className="downArrow"/>
                    </div>
                    <div className="centerise">
                        <RenderIcon marginRight={10} className="renderIconFile"/>
                    </div>
                    
                </Grid>

                <Grid item xs={6}>
                    <h3> Prefer to see tables and graphs? </h3>
                    <Typography variant="h5" style={{color: '#5e5e5e'}}>
                        Download and view your invoices in your database as easy-to-read formats such as HTML to review the contents of an invoice. 
                    </Typography>
                    <h4> Storage Features </h4>
                    <Card variant='outlined' sx={{ minWidth: 275, borderRadius: 4.5, boxShadow: 4}} style={{background: 'linear-gradient(to right bottom, #4760ff, #22e0e0)'}}>
                        <List>
                            <ListItem>
                                <ListItemIcon>
                                    <CheckCircleIcon sx={{ color: '#ffffff'}}/>
                                </ListItemIcon>
                                <Typography variant="h5" style={{color: '#ffffff'}}> Render simple and easy-to-read HTML invoices</Typography>
                            </ListItem>

                            <ListItem>
                                <ListItemIcon>
                                    <CheckCircleIcon sx={{ color: '#ffffff'}}/>
                                </ListItemIcon>
                                <Typography variant="h5" style={{color: '#ffffff'}}> View your rendered invoices in one place</Typography>
                            </ListItem>

                            <ListItem>
                                <ListItemIcon>
                                    <CheckCircleIcon sx={{ color: '#ffffff'}}/>
                                </ListItemIcon>
                                <Typography variant="h5" style={{color: '#ffffff'}}> Delete unwanted invoices</Typography>
                            </ListItem>
                        </List>
                    </Card>
                    <div className="getStarted">
                        <Button size="large" variant="contained" endIcon={<ArrowForwardIosIcon />} sx={{ background: 'linear-gradient(to right bottom, #4760ff, #22e0e0)'}}  onClick={() => routeChange('GetStarted')}>Get Started</Button>
                    </div>
                </Grid>
            </Grid>
            <br/>
            <br/>
            <br/>
        </>
    )
}

export default Home