import { useEffect } from "react";
import { Form } from "react-router-dom";
import { useCSRFSetter, useCSRFCookieGetter } from "../hooks/CSRFHooks";
function Register() {
  useEffect(() => {
    useCSRFSetter()
  }, [])
  return (
    <>
      <Form method="post"  >
        <label htmlFor="">Username: </label>
        <input type="text" value="username" placeholder="ghiath_abbas" name="username"/>
        <br />
        <label htmlFor="">Email: </label>
        <input type="text" value="username@gmail.com" placeholder="ghiath@gmail.com" name="email"/>
        <br />
        <label htmlFor="">Password: </label>
        <input type="password" value="username" name="password"/>
        <button type="submit">Register</button>
      </Form>
    </>
  )
}

export default Register