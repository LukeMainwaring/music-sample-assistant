import React, { Component } from 'react';
import WaveSurfer from 'wavesurfer.js';
import { Pause, PlayArrow } from '@material-ui/icons';

import { IconButton } from '@material-ui/core';

import styles from './Waveform.module.css';

class Waveform extends Component {
  state = {
    playing: false,
  };

  componentDidMount() {
    const sampleIdentifier = this.props.sampleName.replace(/[^a-zA-Z ]/g, '');
    const track = document.querySelector(`#${sampleIdentifier}`);
    this.waveform = WaveSurfer.create({
      barWidth: 3,
      cursorWidth: 1,
      container: '#waveform',
      backend: 'WebAudio',
      height: 80,
      progressColor: '#2D5BFF',
      responsive: true,
      waveColor: '#EFEFEF',
      cursorColor: 'transparent',
    });

    this.waveform.load(track);
  }

  handlePlay = () => {
    this.setState({ playing: !this.state.playing });
    this.waveform.playPause();
  };

  render() {
    const { sampleName, audioData } = this.props;
    const sampleIdentifier = sampleName.replace(/[^a-zA-Z ]/g, '');

    return (
      <div className={styles.WaveformContainer}>
        <IconButton className={styles.PlayButton} onClick={this.handlePlay}>
          {!this.state.playing ? <PlayArrow /> : <Pause />}
        </IconButton>
        <div id='waveform' className={styles.Wave} />
        <audio
          id={sampleIdentifier}
          src={`data:audio/x-wav;base64,${audioData}`}
        />
      </div>
    );
  }
}

export default Waveform;
