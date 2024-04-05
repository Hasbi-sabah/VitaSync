import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { Provider } from 'react-redux';
import { store } from './app/store';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

/**
 * Root component rendering the application.
 * 
 * This component renders the entire application within the specified DOM element.
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
