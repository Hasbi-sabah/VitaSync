import React from 'react'
import { logOut } from '../features/auth/authSlice'

const app_auth = process.env.APP_AUTH_URL;
const Logout = () => {
    const re_routeLogin = () => {
        window.location.href = app_auth + "/login";
        return null;
      };
  return (
    <>
        {logOut()}
        {re_routeLogin()}
    </>
  )
}

export default Logout
