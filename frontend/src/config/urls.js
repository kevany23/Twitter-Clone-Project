/* eslint-disable */
const LOCAL_BACKEND_URL = process.env.VUE_APP_LOCAL_BACKEND_URL;
const SERVER_BACKEND_URL = "";
const mode = process.env.VUE_APP_MODE;
const BACKEND_URL =
  process.env.mode == mode ? LOCAL_BACKEND_URL : SERVER_BACKEND_URL;
export default BACKEND_URL;
