import { useEffect } from "react";
import { logOut } from "../features/auth/authSlice";
import { useDispatch } from "react-redux";

const authLink = process.env.REACT_APP_AUTH_URL;
const Logout = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    const handleLogOut = () => {
      dispatch(logOut());
      window.location.href = `${authLink}/login`;
    };

    handleLogOut();
  }, [dispatch]);

  return null;
};

export default Logout;
