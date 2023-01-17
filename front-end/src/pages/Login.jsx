import { useEffect } from "react"
import Header from "../layout/Header"
function Login() {
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      let cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  const csrftoken = getCookie("csrftoken");
  function login(event) {
    event.preventDefault()
    // fetch(
    //   'http://127.0.0.1:8000/login/',
    //   {
    //     method: 'POST',
    //     headers: {
    //       "Content-type": "application/json",
    //       "X-CSRFToken": csrftoken,
    //     },
    //     body: {
    //       username: 'Ahmad',
    //       password: '12345678'
    //     }
    //   }
    // ).then(res=>console.log(res))
  }
  // useEffect(() => {
  //   function get() {
  //     fetch('http://127.0.0.1:8000/done/').then(
  //       res => {
  //         console.log(res)
  //         return res.json()
  //       }
  //     ).then(
  //       res=>console.log(res)
  //     )
  //   }
  //   // function done() {
  //   //   fetch('http://127.0.0.1:8000/done/', {
  //   //     method: 'POST',
  //   //     headers: {
  //   //       'Content-type':'application/json'
  //   //     },
  //   //     credentials:'include',
  //   //     body:JSON.stringify({name:'imad'})
  //   //   }).then(
  //   //     res => {
  //   //       console.log(res)
  //   //       return res.json()
  //   //     }
  //   //   ).then(
  //   //     res=>console.log(res)
  //   //   )
  //   // }
  //   get()
  //   // done()
  // }, [])
  
  return( 
    <>
      <form onSubmit={login} method="post" action="http://127.0.0.1:8000/login/">
        <label htmlFor="">Username: </label>
        <input type="text" placeholder="ghiath_abbas" name="username"/>
        <br />
        <label htmlFor="">Password: </label>
        <input type="password" name="password"/>
        <button type="submit">Register</button>
      </form>
    </>
  )
}

export default Login