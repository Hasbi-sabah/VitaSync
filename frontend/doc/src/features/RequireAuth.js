import { Outlet } from "react-router-dom";
import { useSelector } from "react-redux";
import { selectCurrentToken } from "./auth/authSlice";


const RequireAuth = () => {
    const token = useSelector(selectCurrentToken);

    const re_routeLogin = () => {
      window.location.href = "http://localhost:3000/login";
      return null;
    };
    if (!token) {
      re_routeLogin();
      return null; 
  }
  return <Outlet />;
}

export default RequireAuth
