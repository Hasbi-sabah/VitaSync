import Dashboard from './features/Dashboard';
import { Route, Routes } from 'react-router-dom';
import Layout from './components/Layout';
import RequireAuth from './features/RequireAuth';
import PatientMan from './features/PatientMan';
import ContactHCW from './features/ContactHCW';
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { setCredentials } from './features/auth/authSlice';
import Logout from './components/Logout';

const authLink = process.env.REACT_APP_AUTH_URL;
function App() {
  const dispatch = useDispatch()
  const re_routeLogin = () => {
    window.location.href = `${authLink}/login`;
    return null;
  };

  const urlParams = new URLSearchParams(window.location.search);
  const token = urlParams.get("token");
  const userId = urlParams.get("id");
  const role = urlParams.get("role");
  if (token && userId && role) {
    dispatch(
      setCredentials({
        accessToken: token,
        userId: userId,
        role: role,
        pinnedIds: []
      })
    );
    window.history.replaceState({}, document.title, window.location.pathname);
  } else {
      dispatch(
        setCredentials({
          accessToken: localStorage.getItem('token'),
          userId: localStorage.getItem('id'),
          role: localStorage.getItem('role'),
          pinnedIds: JSON.parse(localStorage.getItem('pinnedIds'))
        })
      )
    }
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
      <Route index element={<Dashboard />} />
        {/* pulic routes*/}
        
        {/* private routes*/}
        <Route element={<RequireAuth />}>
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="contactHCW" element={<ContactHCW />} />
          <Route path="logout" element={<Logout />} />
        </Route>

      </Route>
    </Routes>
  );
}

export default App;
