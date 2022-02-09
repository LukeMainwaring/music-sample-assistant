import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import {
  Typography,
  Grid,
  Container,
  AppBar,
  IconButton,
  Toolbar,
  CssBaseline,
} from '@material-ui/core';
import MenuIcon from '@material-ui/icons/Menu';
import { makeStyles } from '@material-ui/core/styles';
import Samples from './Samples';
import SampleFilterBox from './SampleFilterBox';

const Home = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <CssBaseline />
      <AppBar position='absolute'>
        <Toolbar>
          <IconButton
            edge='start'
            className={classes.menuButton}
            color='inherit'
            aria-label='menu'
          >
            <MenuIcon />
          </IconButton>
          <Typography
            component='h1'
            variant='h4'
            color='inherit'
            noWrap
            className={classes.title}
          >
            Music Sample Assistant
          </Typography>
        </Toolbar>
      </AppBar>
      <main className={classes.content}>
        <div className={classes.appBarSpacer} />
        <Container maxWidth='lg' className={classes.container}>
          <Grid container spacing={4}>
            <Grid item xs={6}>
              <SampleFilterBox />
            </Grid>
            <Grid item xs={12}>
              <Samples />
            </Grid>
            <Typography
              variant='h4'
              component='h4'
              align='center'
              style={{ marginTop: 50 }}
            >
              Upload current song section
            </Typography>
          </Grid>
        </Container>
      </main>
    </div>
  );
};

const useStyles = makeStyles((theme) => ({
  appBarSpacer: theme.mixins.toolbar,
  container: {
    paddingTop: theme.spacing(4),
    paddingBottom: theme.spacing(4),
  },
  content: {
    flexGrow: 1,
    height: '100vh',
    overflow: 'auto',
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  root: {
    display: 'flex',
  },
  title: {
    flexGrow: 1,
  },
}));

const mapStateToProps = () => {
  return {};
};

const mapDispatchToProps = (dispatch) => {
  return bindActionCreators({}, dispatch);
};

export default connect(mapStateToProps, mapDispatchToProps)(Home);
