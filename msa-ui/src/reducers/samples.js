import { TEST_DOWNLOAD_AUDIO } from '../actions/samples';

const initialState = {
  wavFile: null,
};

export default (state = initialState, action) => {
  switch (action.type) {
    case TEST_DOWNLOAD_AUDIO:
      return { ...state, wavFile: action.payload };
    default:
      return state;
  }
};
