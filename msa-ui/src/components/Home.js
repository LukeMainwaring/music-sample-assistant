import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { Typography, withStyles } from '@material-ui/core';

const Home = ({}) => {
  return (
    <div>
      <Typography variant='h2' component='h2' align='center'>
        Welcome to Music Sample Assistant
      </Typography>
    </div>
  );
};

const mapStateToProps = ({}) => {
  return {};
};

const mapDispatchToProps = (dispatch) => {
  return bindActionCreators({}, dispatch);
};

const styles = {};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(withStyles(styles)(Home));
