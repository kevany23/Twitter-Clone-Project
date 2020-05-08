/*
Basic Functions for checking authentication status and token
*/
/* eslint-disable */
export function setLoginToken(token) {
  sessionStorage.setItem('jwt', token);
}

export function getLoginToken() {
  return sessionStorage['jwt'];
}

export function isLoggedIn() {
  if (sessionStorage['jwt']) {
    return true;
  }
  return false;
}

export function deleteLoginToken() {
  sessionStorage.removeItem('jwt');
}

export function authHeader() {
  return {
    authorization: "Bearer " + getLoginToken(),
  };
}