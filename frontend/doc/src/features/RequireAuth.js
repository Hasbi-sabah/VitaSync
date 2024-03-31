import { Outlet } from "react-router-dom";
import { useSelector } from "react-redux";
import { selectCurrentToken } from "./auth/authSlice";

const app_auth = process.env.APP_AUTH_URL;
const RequireAuth = () => {
    const token = useSelector(selectCurrentToken);

    const re_routeLogin = () => {
      window.location.href = app_auth + "/login";
      return null;
    };
    if (!token) {
      re_routeLogin();
      return null; 
  }
  return <Outlet />;
}

export default RequireAuth
