// import { StrictMode } from 'react'
// import { createRoot } from 'react-dom/client'
// import './index.css'
// import App from './App.jsx'

// createRoot(document.getElementById('root')).render(
//   <StrictMode>
//     <App />
//   </StrictMode>,
// )

import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.tsx';
import './index.css';

// Mount to the sidebar's root if it exists, else fallback to default
const rootElement = document.getElementById('root') || document.body;
ReactDOM.createRoot(rootElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);