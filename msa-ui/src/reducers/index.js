import { combineReducers } from 'redux';
import { reducer as formReducer } from 'redux-form';

import samples from './samples';

export default combineReducers({
  form: formReducer,
  samples,
});
