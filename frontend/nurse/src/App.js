import Dashboard from './features/Dashboard';
import { Route, Routes } from 'react-router-dom';
import Layout from './components/Layout';
import Public from './components/Public';
import Login from './features/auth/Login';
import RequireAuth from './features/RequireAuth';
import PatientMan from './features/PatientMan';
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { setCredentials } from './features/auth/authSlice';
import Records from './features/Records';

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
    dispatch(
      setCredentials({
        accessToken: token,
        userId: userId,
        role: role,
      })
    );
    
    console.log(`token: ${token}, id: ${userId}, role: ${role}`)
    // if (!token) re_routeLogin()
  }, [])
  return (
    <Routes>
      <Route path="login" element={<Login />} />
      <Route index element={<Public />} />
      <Route path="/" element={<Layout />}>
      <Route path="dashboard" element={<Dashboard />} />
        {/* pulic routes*/}
        
        {/* private routes*/}
        <Route element={<RequireAuth />}>
          <Route path="patients" element={<PatientMan />} />
          <Route path="records" element={<Records />} />
        </Route>

      </Route>
    </Routes>
  );
}

export default App;
