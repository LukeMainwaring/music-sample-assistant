import msaApi from '../apis/msaApi';

export const TEST_DOWNLOAD_AUDIO = 'TEST_DOWNLOAD_AUDIO';

export const getTestBpm = () => async (dispatch) => {
  const response = await msaApi.get('/testBpm');
  console.log(response);
};

export const testDownloadAudio = () => async (dispatch) => {
  const response = await msaApi.get('/downloadAudio');

  // Flask response format: { audioData: <base64 string> , sampleFileName: 'sample_name.wav' }
  const audioData = response.data.audioData;
  // const sampleFileName = response.data.sampleFileName; // Not needed yet

  dispatch({ type: TEST_DOWNLOAD_AUDIO, payload: audioData });
};
