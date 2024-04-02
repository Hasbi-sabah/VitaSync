import Dashboard from './features/Dashboard';
import { Route, Routes } from 'react-router-dom';
import Layout from './components/Layout';
import Public from './components/Public';
import Login from './features/auth/Login';
import RequireAuth from './features/RequireAuth';
import ContactHCW from './features/ContactHCW';
import PatientMan from './features/PatientMan';
import Records from './features/Records';
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { setCredentials } from './features/auth/authSlice';
import Prescriptions from './features/Prescriptions';
import Logout from './components/Logout';


function App() {
  const dispatch = useDispatch()
  const re_routeLogin = () => {
    window.location.href = "http://localhost:3000/login";
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
      <Route path="login" element={<Login />} />
      <Route index element={<Public />} />
      <Route path="/" element={<Layout />}>

        {/* pulic routes*/}
        
        {/* private routes*/}
        <Route element={<RequireAuth />}>
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="contactHCW" element={<ContactHCW />} />
          <Route path="records" element={<Records />} />
          <Route path="prescriptions" element={<Prescriptions />} />
          <Route path="patients" element={<PatientMan />} />
          <Route path="logout" element={<Logout />} />
        </Route>

      </Route>
    </Routes>
  );
}

export default App;
