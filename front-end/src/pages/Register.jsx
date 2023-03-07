import { useState, useContext, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { UserContext } from "../context/UserContext";
import { InvalidField } from "../components";
import { useCSRFSetter, useCSRFCookieGetter } from "../hooks/CSRFHooks";

function Register() {

  const navigate = useNavigate()
  const userContext = useContext(UserContext)
  const [csrftoken, setCSRFToken] = useState()

  useEffect(() => {
    if (userContext.user.is_authenticated === true) {
      navigate('/')
    } else {
      useCSRFSetter(setCSRFToken)
    }
  }, [userContext])

  class Field {
    #isValid;
    constructor(regexp, validators, errorMessage) {
      Object.defineProperties(this, {
        value: {
          value: null,
          writable: true
        },
        regexp: {
          value: regexp,
          writable: false
        },
        validators: {
          value: validators,
          writable: false
        },
        errorMessage: {
          value: errorMessage,
          writable: false
        }
      });
      this.#isValid;
    }
    // Apply given validators and decide whether the field value is valid or invlaid. 
    applyValidators() {
      if (this.value) {

        if (this.regexp) {
          if (!this.regexp.test(this.value))
          return false
        }

        if (this.validators) {
          return this.validators.every((validator) => validator(this.value))
        }

        return true
      }
      return null
    }

    isValid() {
      return this.#isValid;
    }

    setValue(newValue) {
      this.value = newValue;
      this.#isValid = this.applyValidators()
    }
  }
  const [fields, setFields] = useState(() => {
    return {
      name: new Field(/^[A-Za-z]*$/, [], 'A Name Field Must Not Have Any Special Character, Numbers Or Whitespaces.'),
      username: new Field(/^\w{6,}$/i, [], 'Username Field Must Be At Least 8 Characters And Not Have Whitespaces Or Any Speical Character Except Underscore.'),
      email: new Field(/(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/i,[], 'Invalid Email'),
      password: new Field(/.{8,}/i, [], 'your password must be at least 8 characters'),
      country_id: new Field(),
      city_id: new Field(),
    }
  })

  function validateField(event) {
    let { name, value } = event.target;
    setFields(prevFields => {
      let changedField = prevFields[name]
      changedField.setValue(value);
      return {
        ...prevFields,
        [name]: changedField
      }
    })

    // if (name === 'password') {

    //   const specialCharcters = '~`!@#$%^&*()-=_+,<>.?/:;\'"{}[]|\\';
    //   let hasSpecialCharacter = false;
    //   let hasNumber = false;

    //   function changeStrength(content, color) {
    //     passwordStrength.current.textContent = content
    //     passwordStrength.current.style.color = color
    //   }

    //   if (value.length >= 8) {

    //     setIsValid(prevIsValid => ({
    //       ...prevIsValid,
    //       password: true
    //     }))

    //     value.split('').forEach(character => {
    //       if (specialCharcters.includes(character)) {
    //         hasSpecialCharacter = true;
    //       }

    //       if (!isNaN(parseInt(character))) {
    //         hasNumber = true;
    //       }
    //     })


    //     if (hasSpecialCharacter && hasNumber) {
    //       changeStrength('Very Strong Password', 'green')
    //     } else if (!hasSpecialCharacter && !hasNumber) {
    //       changeStrength('Weak Password', 'red')
    //     } else {
    //       changeStrength('Strong Password', 'green')
    //     }

    //   } else {
    //     if (passwordStrength.current.textContent) {
    //       changeStrength('')
    //     }
    //     setIsValid(prevIsValid => ({
    //       ...prevIsValid,
    //       password: false
    //     }))
    //   }


    // } else {
    //   setIsValid(prevIsValid => ({
    //     ...prevIsValid,
    //     [name]: validationRegExps[name].test(value) ? true : !value ? null : false
    //   }))
    // }
  }
  const passwordStrength = useRef()

  // Submitting Registering Data To The Server
  async function register(event) {
    event.preventDefault();

    // Checking if all fields have valid values or not before sending data.
    const fieldsKeys = Object.keys(fields)

    if (fieldsKeys.every(key => fields[key].isValid())) {

      // Gathering data from fields
      let formData = { user: {}, user_profile: {} }
      let AuthenticationFields = ['username', 'email', 'password']
      for (const key of fieldsKeys) {
        if (AuthenticationFields.includes(key)) {
          formData.user[key] = fields[key].value
        } else {
          formData.user_profile[key] = fields[key].value
        }
      }
      const response = await (await fetch('http://127.0.0.1:8000/auth/register/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(formData),
        credentials: 'include'
      })).json()

      // These errors are errors sent from the backend server if any,
      // but if there are no errors  react-router will navigate to home route.
      const errors = response.errors
      if (errors) {
        console.log(errors)
        document.querySelector(`#username #invalid-message`).textContent = errors['username'] ? errors['username'][0] : ""
        document.querySelector(`#email #invalid-message`).textContent = errors['email'] ? errors['email'][0] : ""
      } else {
        console.log(response)
        navigate('/', { state: response.message })
      }
      
    }
  } 
  return (
    <>
      {!userContext.user.is_authenticated && <form
        id='register-form'
        onSubmit={register}
      >
        <div id="name">
          <label htmlFor="">Full Name:</label>
          <input
            type="text"
            name='name'
            required
            onChange={validateField}
          />
          <InvalidField isValidField={fields.name.isValid()} invlaidMessage={fields.name.errorMessage} />
        </div>
        <div id="username">
          <label htmlFor="">Username: </label>
          <input
            type="text"
            name='username'
            required
            onChange={validateField}
          />
          <br />
          <InvalidField isValidField={fields.username.isValid()} invlaidMessage={fields.username.errorMessage} />
        </div>
        <div id="email">
          <label htmlFor="">Email: </label>
          <input
            type="email"
            name='email'
            required
            onChange={validateField}
          />
          <br />
          <InvalidField isValidField={fields.email.isValid()} invlaidMessage={fields.email.errorMessage} />
        </div>
        <div id="password">
          <label htmlFor="">Password: </label>
          <input
            type="password"
            name='password'
            required
            min={8}
            onChange={validateField}
          />
          <br />
          <span ref={passwordStrength}></span>
          <InvalidField isValidField={fields.password.isValid()} invlaidMessage={fields.password.errorMessage} />
        </div>
        <div id='country'>
          <label htmlFor="">Country:</label>
          <select
            name='country_id'
            required
            onChange={validateField}
          >
            <option value="">Select your country</option>
            <option value={1}>Syria</option>
            {/* {countries? countries.map(country => <option key={country.id} value={country.id}>{ country.name }</option>):null} */}
          </select>
          <InvalidField />
        </div>
        <div id='city'>
          <label htmlFor="">city:</label>
          <select
            name='city_id'
            required
            onChange={validateField}
          >
            <option value="">Select your country</option>
            <option value={1}>Homs</option>
            {/* {countries? countries.map(country => <option key={country.id} value={country.id}>{ country.name }</option>):null} */}
          </select>
          <InvalidField />
        </div>
        {/* <div id="gender">
          <p>Gender:</p>
          <div> 
            <input 
              type="radio"
              name="gender" 
              value={true}
              onChange={validateField}
              />
            <label htmlFor="male">Male</label>
          </div>
          <div>
            <input
              type="radio"
              name="gender" 
              value={false}
              onChange={validateField}
              />
            <label htmlFor="female">Female</label>
          </div>
          <InvalidField />
        </div> */}
        <button type="submit">Register</button>
      </form>}
    </>
  )
}

export default Register