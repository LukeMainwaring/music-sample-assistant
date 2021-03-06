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
} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import Waveform from './Waveform';
import { VALID_SONG_KEYS } from '../util/constants';
import { getCandidateSamples } from '../actions/samples';

const Home = ({ getCandidateSamples, candidateSamples }) => {
  const classes = useStyles();

  const [tempo, setTempo] = useState('120');
  const [songKey, setSongKey] = useState('C major');

  const handleTempoChange = (e) => {
    setTempo(e.target.value);
  };

  const handleSongKeyChange = (e) => {
    setSongKey(e.target.value);
  };

  const renderAudio = () => {
    if (candidateSamples && candidateSamples.length > 0) {
      return candidateSamples.map((sample) => (
        <div>
          {sample.sampleFileName}
          <Waveform
            sampleName={sample.sampleFileName}
            audioData={sample.audioData}
          />
        </div>
      ));
    }
    return;
  };

  return (
    <div>
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Typography variant='h2' component='h2' align='center'>
            Welcome to Music Sample Assistant
          </Typography>
        </Grid>
        <Grid item xs={12}>
          <Grid container justify='center'>
            <Grid item>
              <Typography variant='h5' component='h5'>
                Select Tempo
              </Typography>
            </Grid>
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
        </Grid>
        <Grid item xs={12}>
          <Grid container justify='center'>
            <Grid item>
              <Typography variant='h5' component='h5'>
                Select Key
              </Typography>
            </Grid>
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
        </Grid>
        <Grid item xs={12}>
          <Grid container justify='center'>
            <Grid item>
              <Button
                variant='contained'
                onClick={() => getCandidateSamples(songKey, tempo)}
              >
                Get Candidate Samples
              </Button>
              {renderAudio()}
            </Grid>
          </Grid>
        </Grid>
      </Grid>

      <Typography
        variant='h4'
        component='h4'
        align='center'
        style={{ marginTop: 50 }}
      >
        (eventually) upload current song section
      </Typography>
    </div>
  );
};

const useStyles = makeStyles((theme) => ({
  bpmInput: {
    marginBottom: 20,
    marginLeft: 20,
  },
}));

const mapStateToProps = ({ samples }) => {
  return { candidateSamples: samples.candidateSamples };
};

const mapDispatchToProps = (dispatch) => {
  return bindActionCreators({ getCandidateSamples }, dispatch);
};

export default connect(mapStateToProps, mapDispatchToProps)(Home);
