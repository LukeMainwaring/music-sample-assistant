import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  Typography,
  Paper,
  CircularProgress,
} from '@material-ui/core';
import Waveform from './Waveform';
import { makeStyles } from '@material-ui/core/styles';

const Samples = ({ samples, candidateSamples }) => {
  const classes = useStyles();

  const renderAudio = () => {
    if (samples.loading) {
      return (
        <div className={classes.progressCircle}>
          <CircularProgress />
        </div>
      );
    }
    if (candidateSamples && candidateSamples.length > 0) {
      return candidateSamples.map((sample, index) => (
        <TableRow key={index}>
          <TableCell>
            <Waveform
              sampleName={sample.sampleFileName}
              audioData={sample.audioData}
            />
          </TableCell>
          <TableCell>{sample.sampleFileName}</TableCell>
          <TableCell>100</TableCell>
        </TableRow>
      ));
    }
    return;
  };

  return (
    <React.Fragment>
      <Paper className={classes.paper}>
        <Typography component='h2' variant='h6' color='primary' gutterBottom>
          Candidate Samples
        </Typography>
        <Table size='small'>
          <TableHead>
            <TableRow>
              <TableCell className={classes.sampleColumnTitle}>
                Sample
              </TableCell>
              <TableCell className={classes.columnTitle}>Name</TableCell>
              <TableCell className={classes.columnTitle}>Rating</TableCell>
            </TableRow>
          </TableHead>

          <TableBody>{renderAudio()}</TableBody>
        </Table>
      </Paper>
    </React.Fragment>
  );
};

const useStyles = makeStyles((theme) => ({
  columnTitle: {
    fontWeight: 'bold',
  },
  sampleColumnTitle: {
    fontWeight: 'bold',
    paddingLeft: theme.spacing(6),
  },
  paper: {
    padding: theme.spacing(2),
    display: 'flex',
    overflow: 'auto',
    flexDirection: 'column',
  },
  progressCircle: {
    padding: theme.spacing(2),
  },
}));

const mapStateToProps = ({ samples }) => {
  return { samples: samples, candidateSamples: samples.candidateSamples };
};

const mapDispatchToProps = (dispatch) => {
  return bindActionCreators({}, dispatch);
};

export default connect(mapStateToProps, mapDispatchToProps)(Samples);
