import React from 'react'
import avatar from '../assets/avatar.svg'
const Header = () => {
  return (
    <header className='d-flex justify-content-between align-items-center p-3 text-white'>
      <h1 className='logo m-0'><a href="/">Logo</a></h1>
      <nav className='d-flex align-items-center gap-3'>
        <ul className='d-flex gap-3 m-0'>
          <li><a href="">Home</a></li>
          <li><a href="">Stores</a></li>
          <li><a href="">Categories</a></li>
          <li><a href="">Products</a></li>
          <li><a href="">Contact Us</a></li>
          <li><a href="">About Us</a></li>
        </ul>
        <a className='profile'><img src={avatar} alt="profile"/></a>
      </nav>
    </header>
  )
}

export default Header