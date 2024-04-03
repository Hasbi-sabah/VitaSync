import { Outlet } from "react-router-dom";
import { useSelector } from "react-redux";
import { selectCurrentToken } from "./auth/authSlice";


const RequireAuth = () => {
    const token = localStorage.getItem('token');

    const re_routeLogin = () => {
      window.location.href = "http://localhost:3000/login";
      return null;
    };
    if (token === null || !token) {
      re_routeLogin();
      return null; 
  }
  return <Outlet />;
}

export default RequireAuth
