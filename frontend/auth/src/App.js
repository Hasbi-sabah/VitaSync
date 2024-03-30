import { Route, Routes } from 'react-router-dom';
import Public from './components/Public';
import Login from './features/auth/Login';

function App() {
  return (
    <Routes>
      <Route path="login" element={<Login />} />
      <Route index element={<Public />} />
        {/* pulic routes*/}
        
        {/* private routes*/}
    </Routes>
  );
}

export default App;
