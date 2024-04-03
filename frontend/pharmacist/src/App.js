import Dashboard from './features/Dashboard';
import { Route, Routes } from 'react-router-dom';
import Layout from './components/Layout';
import RequireAuth from './features/RequireAuth';
import PatientMan from './features/PatientMan';
import Records from './features/Records';
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { setCredentials } from './features/auth/authSlice';
import Logout from './components/Logout';
import ContactHCW from './features/ContactHCW';

function App() {
  const dispatch = useDispatch()
  const re_routeLogin = () => {
    window.location.href = "http://localhost:3000/login";
    return null;
  };

  useEffect(() => {
    const urlParams = new URLSearchParams(window.location.search);
    const token = urlParams.get("token");
    const userId = urlParams.get("id");
    const role = urlParams.get("role");
    const username = urlParams.get("username");
    if(username?.includes('.')){
      username.replace('.', ' ');
    }
    dispatch(
      setCredentials({
        accessToken: token,
        userId: userId,
        role: role,
        username: username,
      })
    );
    
    // console.log(`token: ${token}, id: ${userId}, role: ${role}`)
    // if (!token) re_routeLogin()
  }, [])
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
