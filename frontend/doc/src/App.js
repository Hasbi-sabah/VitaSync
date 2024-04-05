import Dashboard from './features/Dashboard';
import { Route, Routes } from 'react-router-dom';
import Layout from './components/Layout';
import RequireAuth from './features/RequireAuth';
import ContactHCW from './features/ContactHCW';
import { useDispatch } from "react-redux";
import { setCredentials } from './features/auth/authSlice';
import Logout from './components/Logout';

const authLink = process.env.REACT_APP_AUTH_URL;

/**
 * Main component of the application.
 * 
 * This component handles authentication, sets user credentials, and defines routing.
 * 
 * @returns The JSX element representing the main application component.
 */
function App() {
  const dispatch = useDispatch()
  const re_routeLogin = () => {
    window.location.href = `${authLink}/login`;
    return null;
  };

  // Extract token, user ID, and role from URL parameters
  const urlParams = new URLSearchParams(window.location.search);
  const token = urlParams.get("token");
  const userId = urlParams.get("id");
  const role = urlParams.get("role");

  // Set user credentials if present in URL parameters, otherwise from local storage
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
      dispatch(
        setCredentials({
          accessToken: localStorage.getItem('token'),
          userId: localStorage.getItem('id'),
          role: localStorage.getItem('role'),
        })
      )
    }
  return (
    <Routes>
        {/* pulic routes*/}
        
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

export default App;
