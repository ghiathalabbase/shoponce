import React from 'react'
import { NavLink } from 'react-router-dom'
import avatar from '../assets/avatar.svg'
const Header = () => {
  return (
    <header className='d-flex justify-content-between align-items-center p-3'>
      <NavLink to='/'><h1 className='logo m-0'>Logo</h1></NavLink>
      
      <nav className='d-flex align-items-center gap-3'>
        <ul className='d-flex gap-3 m-0'>
          <li><a href="">Home</a></li>
          <li><a href="">Stores</a></li>
          <li><a href="">Categories</a></li>
          <li><a href="">Products</a></li>
          <li><a href="">Contact Us</a></li>
          <li><a href="">About Us</a></li>
        </ul>
        <NavLink to='login/' className='profile'><img src={avatar} alt="profile"/></NavLink>
      </nav>
    </header>
  )
}

export default Header