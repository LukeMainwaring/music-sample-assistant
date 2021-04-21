import msaApi from '../apis/msaApi';

export const TEST_DOWNLOAD_AUDIO = 'TEST_DOWNLOAD_AUDIO';
export const GET_CANDIDATE_SAMPLES = 'GET_CANDIDATE_SAMPLES';

export const getTestBpm = () => async (dispatch) => {
  const response = await msaApi.get('/testBpm');
  console.log(response);
};

export const testDownloadAudio = () => async (dispatch) => {
  const response = await msaApi.get('/downloadAudio');

  // Flask response format: { audioData: <base64 string> , sampleFileName: 'sample_name.wav' }
  const audioData = response.data.audioData;

  dispatch({ type: TEST_DOWNLOAD_AUDIO, payload: audioData });
};

export const getCandidateSamples = () => async (dispatch) => {
  const response = await msaApi.get('/getCandidateSamplesMatched');
  // Flask response format: [ { audioData: <base64 string> , sampleFileName: 'sample_name.wav' }, ... ]
  dispatch({ type: GET_CANDIDATE_SAMPLES, payload: response.data });
};
