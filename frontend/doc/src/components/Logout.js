import { useEffect } from 'react'
import { logOut } from '../features/auth/authSlice'
import { useDispatch } from 'react-redux';

const Logout = () => {
  const re_routeLogin = () => {
      window.location.href = "http://localhost:3000/login";
      return null;
    };
    logOut()
    re_routeLogin()
  return null
}

export default Logout
