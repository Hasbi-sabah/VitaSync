import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { Provider } from 'react-redux';
import { store } from './app/store';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

/**
 * The root component of the application.
 * 
 * This component renders the entire application wrapped in a Redux Provider
 * for state management and BrowserRouter for client-side routing.
 * 
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
