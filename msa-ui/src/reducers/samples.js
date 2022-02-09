import {
  TEST_DOWNLOAD_AUDIO,
  GET_CANDIDATE_SAMPLES_FINISH,
  GET_CANDIDATE_SAMPLES_LOADING,
  GET_CANDIDATE_SAMPLES_ERROR,
} from '../actions/samples';

const initialState = {
  wavFile: null,
  candidateSamples: [],
  loading: false,
  error: null,
};

export default (state = initialState, action) => {
  switch (action.type) {
    case TEST_DOWNLOAD_AUDIO:
      return { ...state, wavFile: action.payload };
    case GET_CANDIDATE_SAMPLES_LOADING:
      return { ...state, loading: true };
    case GET_CANDIDATE_SAMPLES_FINISH:
      return { ...state, candidateSamples: action.payload, loading: false };
    case GET_CANDIDATE_SAMPLES_ERROR:
      return { ...state, error: action.error, loading: false };
    default:
      return state;
  }
};
