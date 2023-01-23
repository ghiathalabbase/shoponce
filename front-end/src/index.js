import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './style/main.css'
import './style/bootstrap.min.css'
import './style/normalize.css'
import './style/all.min.css'
// import './js/jquery-3.6.0.min.js'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Home from './pages/Home'
// import Register from './pages/Register'
import Login from './pages/Login'
import Stores from './pages/Stores.jsx'

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
