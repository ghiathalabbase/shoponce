import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import { About, Categories, Contact, Dashboard, Home, Login, Product, Products, Profile, Register, Store, Stores } from './pages';
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
        path: 'stores/',
        element: <Stores/>
      },
      {
        path: 'categories',
        element: <Categories/>
      },
      {
        path: 'products',
        element: <Products/>
      },
      {
        path: 'contact',
        element: <Contact/>
      },
      {
        path: 'about',
        element: <About/>
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
    ]
    
  }
  
])
ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={router}/>
)
