
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { Provider } from 'react-redux';
import { store } from './app/store';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

/**
 * Renders the main App component wrapped in Redux Provider and BrowserRouter.
 * This setup allows the application to use Redux for state management and React Router for routing.
 */
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Provider store={store}>
      <BrowserRouter>
      <Routes>
        <Route path="/*" element={<App />} />
      </Routes>
      </BrowserRouter>
    </Provider>
  </React.StrictMode>
);
