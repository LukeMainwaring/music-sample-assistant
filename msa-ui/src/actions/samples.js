import msaApi from '../apis/msaApi';

export const TEST_DOWNLOAD_AUDIO = 'TEST_DOWNLOAD_AUDIO';
export const GET_CANDIDATE_SAMPLES_LOADING = 'GET_CANDIDATE_SAMPLES_LOADING';
export const GET_CANDIDATE_SAMPLES_FINISH = 'GET_CANDIDATE_SAMPLES_FINISH';
export const GET_CANDIDATE_SAMPLES_ERROR = 'GET_CANDIDATE_SAMPLES_ERROR';

export const getTestBpm = () => async (dispatch) => {
  const response = await msaApi.get('/testBpm');
  console.log(response);
};

export const testDownloadAudio = () => async (dispatch) => {
  const response = await msaApi.get('/downloadAudio');
  const audioData = response.data.audioData;
  dispatch({ type: TEST_DOWNLOAD_AUDIO, payload: audioData });
};

export const getCandidateSamples = (songKey, tempo) => async (dispatch) => {
  try {
    dispatch({ type: GET_CANDIDATE_SAMPLES_LOADING });
    const response = await msaApi.get(
      `/getCandidateSamplesMatched/${songKey}/${tempo}`
    );
    // Flask response format: [ { audioData: <base64 string> , sampleFileName: 'sample_name.wav' }, ... ]
    dispatch({ type: GET_CANDIDATE_SAMPLES_FINISH, payload: response.data });
  } catch (err) {
    dispatch({ type: GET_CANDIDATE_SAMPLES_ERROR, error: err });
  }
};
