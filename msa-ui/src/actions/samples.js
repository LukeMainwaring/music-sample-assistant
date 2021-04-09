import msaApi from '../apis/msaApi';

export const getTestBpm = () => async (dispatch) => {
  const response = await msaApi.get('/testBpm');
  console.log(response);
};

export const testDownloadAudio = () => async (dispatch) => {
  const response = await msaApi.get('/downloadAudio');
  // TODO: figure out how to play this data/WAV file on UI
  console.log(response.data);
};
