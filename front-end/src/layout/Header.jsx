import React from 'react'
import { NavLink, Outlet } from 'react-router-dom'
import avatar from '../assets/avatar.svg'
const Header = () => {
  return (
    <>
    <header className='mb-5'>
      <div className="container d-flex justify-content-between align-items-center pt-3 pb-3">
        <NavLink to='/'><h1 className='logo m-0'>Logo</h1></NavLink>
        
        <nav className='d-flex align-items-center gap-3'>
          <ul className='d-flex gap-3 m-0 fs-5'>
            <li><a href="/">Home</a></li>
            <li><a href="stores">Stores</a></li>
            <li><a href="categories">Categories</a></li>
            <li><a href="products">Products</a></li>
            <li><a href="contact">Contact Us</a></li>
            <li><a href="about">About Us</a></li>
          </ul>
          <NavLink to='login/' className='profile'><img src={avatar} alt="profile"/></NavLink>
        </nav>
      </div>
    </header>
    </>
  )
}

export default Header