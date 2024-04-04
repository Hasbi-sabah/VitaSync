import { useEffect } from "react";
import { logOut } from "../features/auth/authSlice"; // Importing the logout action creator from the authSlice
import { useDispatch } from "react-redux"; // Importing useDispatch hook from react-redux for dispatching actions

// Retrieving the authentication URL from the environment variables
const authLink = process.env.REACT_APP_AUTH_URL;

// Logout component
const Logout = () => {
  const dispatch = useDispatch(); // Initializing dispatch function using useDispatch hook

  // Effect hook to trigger logout on component mount
  useEffect(() => {
    // Function to handle logout
    const handleLogOut = () => {
      dispatch(logOut()); // Dispatching the logout action
      window.location.href = `${authLink}/login`; // Redirecting user to login page after logout
    };

    handleLogOut(); // Calling handleLogOut function when component mounts
  }, [dispatch]); // Dependency array with dispatch as the only dependency

  return null; // Returning null because this component doesn't render any UI
};

export default Logout; // Exporting the Logout component
