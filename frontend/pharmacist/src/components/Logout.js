import React from 'react'
import { logOut } from '../features/auth/authSlice'

const Logout = () => {
    const re_routeLogin = () => {
        window.location.href = "http://localhost:3000/login";
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