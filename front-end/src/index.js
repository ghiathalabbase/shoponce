import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './style/main.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Home from './pages/Home'
import Register from './pages/Register'
import Login from './pages/Login'
const router = createBrowserRouter([
  {
    element: <App />,
    children: [
      {
        path: '/',
        element:<Home/>
      },
      {
        path: 'login/',
        element: <Login/>
      }
    ]
    
  },
  
])
ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={router}/>
)
