import { useEffect } from "react"
import Header from "../layout/Header"
function Register() {
  // useEffect(() => {
  //   async function getToken() {
  //     const token = await (await fetch('http://127.0.0.1:8000/register/')).json()
  //     console.log(token)
  //     console.log('kk')
  //   }
  //   getToken()
  // })
  return (
    <>
      <form method="post" action="http://127.0.0.1:8000/register/">
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

export default Register