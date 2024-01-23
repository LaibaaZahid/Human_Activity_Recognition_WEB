import PropTypes from 'prop-types';
import React,{ useState } from 'react';
import axios from 'axios';


// material-ui
import { useTheme } from '@mui/material/styles';
import {  Button,  CardContent,  Grid, Menu, MenuItem, Typography } from '@mui/material';

// project imports
import BajajAreaChartCard from './BajajAreaChartCard';
import MainCard from 'ui-component/cards/MainCard';
import SkeletonPopularCard from 'ui-component/cards/Skeleton/PopularCard';
import { gridSpacing } from 'store/constant';

// assets
/*import ChevronRightOutlinedIcon from '@mui/icons-material/ChevronRightOutlined';*/
import MoreHorizOutlinedIcon from '@mui/icons-material/MoreHorizOutlined';
const PopularCard = ({ isLoading }) => {

  

const handleButtonClick = async () => {
  
  try {
      const response = await axios.post('http://localhost:8000/api/socket_connect,{withCredentials: true}');
      console.log(response.data);
  } catch (error) {
      console.error('Error calling connect function:', error);
  }
};

const handleSocketBindClick = async () => {
  
  try {
      const response = await axios.post('http://localhost:8000/api/socket_bind');
      console.log(response.data);
  } catch (error) {
      console.error('Error calling Bind function:', error);
  }
};

  const theme = useTheme();
  

  const [anchorEl, setAnchorEl] = useState(null);

  
  // Your component JSX

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  

  return (
    <>
      {isLoading ? (
        <SkeletonPopularCard />
      ) : (
        <MainCard content={false}>
          <CardContent>
            <Grid container spacing={gridSpacing}>
              <Grid item xs={12}>
                <Grid container alignContent="center" justifyContent="space-between">
                  <Grid item>
                    <Typography variant="h4">Server Connection</Typography>
                  </Grid>
                  <Grid item>
                    <MoreHorizOutlinedIcon
                      fontSize="small"
                      sx={{
                        color: theme.palette.primary[200],
                        cursor: 'pointer'
                      }}
                      aria-controls="menu-popular-card"
                      aria-haspopup="true"
                      onClick={handleClick}
                    />
                    <Menu
                      id="menu-popular-card"
                      anchorEl={anchorEl}
                      keepMounted
                      open={Boolean(anchorEl)}
                      onClose={handleClose}
                      variant="selectedMenu"
                      anchorOrigin={{
                        vertical: 'bottom',
                        horizontal: 'right'
                      }}
                      transformOrigin={{
                        vertical: 'top',
                        horizontal: 'right'
                      }}
                    >
                      <MenuItem onClick={handleClose}> Today</MenuItem>
                      <MenuItem onClick={handleClose}> This Month</MenuItem>
                      <MenuItem onClick={handleClose}> This Year </MenuItem>
                    </Menu> 
                  </Grid>
                </Grid>
              </Grid>
              <Grid item xs={12} sx={{ pt: '16px !important' }}>
                <BajajAreaChartCard />
              </Grid>
              <Grid item xs={12}>
                <Grid container direction="column">
                  <Grid item>
                    <Grid container alignItems="center" justifyContent="space-between">
                      <Grid item >
                        {/* Add the button here */}

                 
                        <Button variant="contained" onClick={handleButtonClick} sx={{backgroundColor:"#AF3CFF"}} >
                         Start Server
                        </Button> 
                  
                      </Grid>
                      <Grid item >
                      <Button onClick={handleSocketBindClick} variant="contained" sx={{backgroundColor:"#AF3CFF"}}>
                      Socket Bind
                        </Button>
                      </Grid>
                      <Grid item >
                      <Button variant="contained" sx={{backgroundColor:"#AF3CFF", marginTop:10+'px', marginLeft:65+'px'}} onClick={"location.href='{% url 'disconnect' %}'"}>
                         Server Stop
                        </Button>
                      </Grid>
                    </Grid>
                  </Grid>
                </Grid>
              </Grid>
            </Grid>
          </CardContent>
        </MainCard>
      )}
    </>
  );
};
          
PopularCard.propTypes = {
  isLoading: PropTypes.bool
};

export default PopularCard;
