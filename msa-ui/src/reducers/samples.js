import { TEST_DOWNLOAD_AUDIO, GET_CANDIDATE_SAMPLES } from '../actions/samples';

const initialState = {
  wavFile: null,
  candidateSamples: [],
};

export default (state = initialState, action) => {
  switch (action.type) {
    case TEST_DOWNLOAD_AUDIO:
      return { ...state, wavFile: action.payload };
    case GET_CANDIDATE_SAMPLES:
      return { ...state, candidateSamples: action.payload };
    default:
      return state;
  }
};
