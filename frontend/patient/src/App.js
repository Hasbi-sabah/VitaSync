import Dashboard from './features/Dashboard';
import { Route, Routes } from 'react-router-dom';
import Layout from './components/Layout';
import Public from './components/Public';
import Login from './features/auth/Login';
import RequireAuth from './features/RequireAuth';
import ContactHCW from './features/ContactHCW';
import PatientMan from './features/PatientMan';
import Records from './features/Records';

function App() {
  return (
    <Routes>
      <Route path="login" element={<Login />} />
      <Route index element={<Public />} />
      <Route path="/" element={<Layout />}>
      <Route path="dashboard" element={<Dashboard />} />
      <Route path="contactHCW" element={<ContactHCW />} />
      <Route path="records" element={<Records />} />
        {/* pulic routes*/}
        
        {/* private routes*/}
        <Route element={<RequireAuth />}>
          <Route path="patients" element={<PatientMan />} />
        </Route>

      </Route>
    </Routes>
  );
}

export default App;
