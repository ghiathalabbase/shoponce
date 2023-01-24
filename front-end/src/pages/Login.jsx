import { useEffect, useState, useContext } from "react";
import { useNavigate  } from "react-router-dom";
import { useCSRFSetter, useCSRFCookieGetter } from '../hooks/CSRFHooks';
import { UserContext } from "../context/UserContext";

function Login() {
  const [error, setError] = useState(null)
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
    event.preventDefault()
    const credentials = {
      username : document.getElementById('username').value,
      password : document.getElementById('password').value
    }
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
    setError(data.Error)
    if (data.is_authenticated) {
      userContext.setUser(data)
      // ????
      navigate('/profile')
    } 
  }
  return( 
    <>
      <form onSubmit={login} method="post" action="http://127.0.0.1:8000/login/">
        <label htmlFor="">Username: </label>
        <input id='username' type="text" placeholder="ghiath_abbas" name="username"/>
        <br />
        <label htmlFor="">Password: </label>
        <input id='password' type="password" name="password"/>
        <button type="submit">Register</button>
      </form>
      {error}
    </>
  )
}

export default Login