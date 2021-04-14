import msaApi from '../apis/msaApi';

export const TEST_DOWNLOAD_AUDIO = 'TEST_DOWNLOAD_AUDIO';

export const getTestBpm = () => async (dispatch) => {
  const response = await msaApi.get('/testBpm');
  console.log(response);
};

export const testDownloadAudio = () => async (dispatch) => {
  const response = await msaApi.get('/downloadAudio');
  // TODO: figure out how to play this data/WAV file on UI
  console.log(response);
  dispatch({ type: TEST_DOWNLOAD_AUDIO, payload: response.data });
};
