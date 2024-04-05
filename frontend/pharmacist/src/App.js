import Dashboard from './features/Dashboard'; // Importing Dashboard component
import { Route, Routes } from 'react-router-dom'; // Importing Route and Routes components from react-router-dom
import Layout from './components/Layout'; // Importing Layout component
import RequireAuth from './features/RequireAuth'; // Importing RequireAuth component
import PatientMan from './features/PatientMan'; // Importing PatientMan component
import ContactHCW from './features/ContactHCW'; // Importing ContactHCW component
import { useEffect } from "react"; // Importing useEffect hook from React
import { useDispatch } from "react-redux"; // Importing useDispatch hook from react-redux
import { setCredentials } from './features/auth/authSlice'; // Importing setCredentials action creator from authSlice
import Logout from './components/Logout'; // Importing Logout component

const authLink = process.env.REACT_APP_AUTH_URL; // Retrieving authentication URL from environment variables

function App() {
  const dispatch = useDispatch(); // Initializing dispatch function using useDispatch hook

  // Function to redirect to login page
  const re_routeLogin = () => {
    window.location.href = `${authLink}/login`; // Redirecting to login page
    return null; // Returning null
  };

  // Getting token, userId, and role from URL parameters
  const urlParams = new URLSearchParams(window.location.search);
  const token = urlParams.get("token");
  const userId = urlParams.get("id");
  const role = urlParams.get("role");

  // If token, userId, and role are available, set credentials and replace URL
  if (token && userId && role) {
    dispatch(
      setCredentials({
        accessToken: token,
        userId: userId,
        role: role,
      })
    );
    window.history.replaceState({}, document.title, window.location.pathname);
  } else {
    // If not available, set credentials from local storage
    dispatch(
      setCredentials({
        accessToken: localStorage.getItem('token'),
        userId: localStorage.getItem('id'),
        role: localStorage.getItem('role'),
      })
    );
  }

  return (
    <Routes>
      {/* public routes*/}
      
      {/* private routes*/}
      <Route element={<RequireAuth />}>
        <Route path="/" element={<Layout />}>
          <Route index element={<Dashboard />} />
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="contactHCW" element={<ContactHCW />} />
          <Route path="logout" element={<Logout />} />
        </Route>
      </Route>
    </Routes>
  );
}

export default App; // Exporting the App component
