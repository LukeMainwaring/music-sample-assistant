import axios from 'axios';

let instance = axios.create({
  baseURL: '',
});

if (process.env.NODE_ENV === 'development') {
  instance = axios.create({
    baseURL: '/api',
  });
} else {
  // Production server
  instance = axios.create({
    // TODO: Replace with AWS or production url
    // baseURL:
    // 'http://ontrackserver-env.pikgvbwvcg.us-east-1.elasticbeanstalk.com/'
  });
}

export { instance as default };
