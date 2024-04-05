import { Outlet } from "react-router-dom";
import { useSelector } from "react-redux";
import { selectCurrentToken } from "./auth/authSlice";

const authLink = process.env.REACT_APP_AUTH_URL;
/**
 * RequireAuth component that checks if the user is authenticated.
 * If the user is not authenticated, it redirects them to the login page.
 * Otherwise, it renders the children components.
 */
const RequireAuth = () => {
    /**
     * Retrieves the authentication token from local storage.
     * @returns {string|null} The authentication token or null if not found.
     */
    const token = localStorage.getItem('token');

    /**
     * Redirects the user to the login page.
     * @returns {null} Always returns null to prevent rendering of the component.
     */
    const re_routeLogin = () => {
      window.location.href = `${authLink}/login`;
      return null;
    };

    /**
     * Checks if the token is null or empty.
     * If true, redirects the user to the login page.
     * Otherwise, renders the children components.
     */
    if (token === null || !token) {
      re_routeLogin();
      return null; 
  }

    /**
     * Renders the children components if the user is authenticated.
     * @returns {React.Element} The children components wrapped in an Outlet component.
     */
  return <Outlet />;
}

export default RequireAuth
