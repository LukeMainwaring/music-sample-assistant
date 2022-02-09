import React, { useState } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import {
  Typography,
  InputLabel,
  Select,
  MenuItem,
  Grid,
  Button,
  TextField,
  Paper,
} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { VALID_SONG_KEYS } from '../util/constants';
import { getCandidateSamples } from '../actions/samples';

const SampleFilterBox = ({ getCandidateSamples }) => {
  const classes = useStyles();

  const [tempo, setTempo] = useState('90');
  const [songKey, setSongKey] = useState('E major');

  const handleTempoChange = (e) => {
    setTempo(e.target.value);
  };

  const handleSongKeyChange = (e) => {
    setSongKey(e.target.value);
  };

  return (
    <React.Fragment>
      <Paper className={classes.paper}>
        <Grid container>
          <Typography component='h2' variant='h6' color='primary' gutterBottom>
            Select Tempo and Key of song
          </Typography>
          <Grid item xs={12}>
            <Grid item className={classes.bpmInput}>
              <TextField
                required
                id='standard-required'
                label='Input Tempo'
                name='tempo'
                value={tempo}
                onChange={handleTempoChange}
              />
            </Grid>
          </Grid>
          <Grid item xs={12}>
            <Grid item className={classes.bpmInput}>
              <InputLabel id='demo-simple-select-label'>Song Key</InputLabel>
              <Select
                labelId='demo-simple-select-label'
                id='demo-simple-select'
                name='songKey'
                value={songKey}
                onChange={handleSongKeyChange}
              >
                {VALID_SONG_KEYS.map((songKey, index) => (
                  <MenuItem key={index} value={songKey}>
                    {songKey}
                  </MenuItem>
                ))}
              </Select>
            </Grid>
          </Grid>
          <Grid item xs={12}>
            <Button
              variant='contained'
              onClick={() => getCandidateSamples(songKey, tempo)}
            >
              Get Candidate Samples
            </Button>
          </Grid>
        </Grid>
      </Paper>
    </React.Fragment>
  );
};

const useStyles = makeStyles((theme) => ({
  bpmInput: {
    marginBottom: theme.spacing(4),
    marginLeft: theme.spacing(1),
  },
  paper: {
    padding: theme.spacing(2),
    display: 'flex',
    overflow: 'auto',
    flexDirection: 'column',
  },
}));

const mapStateToProps = () => {
  return {};
};

const mapDispatchToProps = (dispatch) => {
  return bindActionCreators({ getCandidateSamples }, dispatch);
};

export default connect(mapStateToProps, mapDispatchToProps)(SampleFilterBox);
