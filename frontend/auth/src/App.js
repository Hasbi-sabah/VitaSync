import { Route, Routes } from 'react-router-dom';
import Public from './components/Public';
import Login from './features/auth/Login';

/**
 * The main component of the application.
 * 
 * This component represents the root of the application's UI hierarchy.
 * It defines the routing configuration using React Router's <Routes> and <Route> components.
 * 
 */
function App() {
  return (
    <Routes>
      <Route path="login" element={<Login />} />
      <Route index element={<Login />} />
        {/* pulic routes*/}
        
        {/* private routes*/}
    </Routes>
  );
}

export default App;
