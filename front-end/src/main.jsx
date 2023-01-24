import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Home from './pages/Home'
import Register from './pages/Register'
import Login from './pages/Login';
import Profile from './pages/Profile';
import Stores from './pages/Stores.jsx'
// import './js/jquery-3.6.0.min.js'
const router = createBrowserRouter([
  {
    element: <App />,
    children: [
      {
        path: '/',
        element: <Home />,
      },
      {
        path: 'profile/',
        element: <Profile />,
      },
      {
        path: 'login/',
        element: <Login />
      },
      {
        path: 'register/',
        element: <Register />,
      },
      {
        path: 'stores/',
        element: <Stores/>
      }
    ]
    
  },
  
])
ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={router}/>
)
