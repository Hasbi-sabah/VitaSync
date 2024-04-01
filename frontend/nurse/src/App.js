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
    if (token){
    dispatch(
      setCredentials({
        accessToken: token,
        userId: userId,
        role: role,
      })
    );}
    else{
      dispatch(
        setCredentials({
          accessToken: localStorage.getItem('token'),
          userId: localStorage.getItem('id'),
          role: localStorage.getItem('role'),
        })
      )
    }
    
    // console.log(`token: ${token}, id: ${userId}, role: ${role}`)
    // if (!token) re_routeLogin()
  }, [])
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
