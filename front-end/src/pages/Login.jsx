import { useEffect, useState, useContext } from "react";
import { NavLink, useNavigate  } from "react-router-dom";
import { useCSRFSetter, useCSRFCookieGetter } from '../hooks/CSRFHooks';
import { UserContext } from "../context/UserContext";

function Login() {
  const [wrong, setWrong] = useState(null)
  const userContext = useContext(UserContext)
  const [csrftoken, setCSRFToken] = useState(useCSRFCookieGetter())
  const navigate = useNavigate()
  useEffect(() => {
    if (userContext.user.is_authenticated === true) {
      navigate('/')
    } else {
      useCSRFSetter(setCSRFToken)
    }
  }, [userContext])
  async function login(event) {
    setWrong('Logging In...')
    event.preventDefault()
    const form = document.getElementById('login-form')
    let credentials = new FormData(form)
    credentials = Object.fromEntries(credentials)
    const response = await fetch('http://127.0.0.1:8000/login/', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
        'X-CSRFToken': csrftoken
      },
      body: JSON.stringify(credentials),
      credentials: 'include',
      
    })
    const data = await response.json()
    if (data.is_authenticated) {
      userContext.setUser(data)
    } else {
      setWrong(data)
    }
  }
  return(!userContext.user.is_authenticated &&
    <>
      <form id="login-form" onSubmit={login} method="post">
        <label htmlFor="">Username: </label>
        <input type="text" placeholder="ghiath_abbas" name="username"/>
        <br />
        <label htmlFor="">Password: </label>
        <input type="password" name="password"/>
        <button type="submit">Login</button>
      </form>
      {wrong}
      <NavLink to='/register'>Sign up</NavLink>
    </>
  )
}

export default Login