import { useEffect } from 'react'
import { logOut } from '../features/auth/authSlice'
import { useDispatch } from 'react-redux';

const Logout = () => {
      const dispatch = useDispatch()

      const handleLogOut = () => {
        dispatch(logOut())
        window.location.href = "http://localhost:3000/login";
      };
      
      useEffect(() => {
        handleLogOut()
      }, [dispatch]);

      return null;
}

export default Logout
