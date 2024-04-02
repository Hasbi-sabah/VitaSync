import { useLocation, Outlet } from "react-router-dom";
import { useSelector } from "react-redux";
import { selectCurrentToken } from "./auth/authSlice";


const RequireAuth = () => {
    const token = useSelector(selectCurrentToken);
    const location = useLocation();

    // Define the re_routeLogin function
    const re_routeLogin = () => {
      window.location.href = "http://localhost:3000/login";
      return null;
    };

    if (!token) {
      return re_routeLogin();
    }

    return <Outlet />;
};

export default RequireAuth
