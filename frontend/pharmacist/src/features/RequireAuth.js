import { Outlet } from "react-router-dom";
import { useSelector } from "react-redux";
import { selectCurrentToken } from "./auth/authSlice";

const authLink = process.env.REACT_APP_AUTH_URL;
const RequireAuth = () => {
    const token = localStorage.getItem('token');

    const re_routeLogin = () => {
      window.location.href = `${authLink}/login`;
      return null;
    };
    if (token === null || !token) {
      re_routeLogin();
      return null; 
  }
  return <Outlet />;
}

export default RequireAuth
