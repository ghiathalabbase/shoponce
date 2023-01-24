import {
  createContext,
  Component,
  useState,
  useEffect
} from "react";
const UserContext = createContext();
function UserContextProvider(props) {
  const [userContext, setUserContext] = useState({
    user: {
      id: null,
      first_name: null,
      last_name: null,
      gender: null,
      gmail: null,
      username: null,
      prfoile_image: null,
      favos_products: null,
      favos_categories: null,
      favos_tags: null,
      city: null,
      is_authenticated: 'checking'
    },
    setUser
  });
  function setUser(data) {
    setUserContext(previousUserContext=>({...previousUserContext, user:data}))
  }
  useEffect(() => {
    async function getUserInfo() {
      const data = await (
        await fetch('http://127.0.0.1:8000/profile/', {
          method: 'GET', credentials: 'include'
        })
      ).json();
      if (data.is_authenticated) {
        setUser(data)
      } else {
        setUserContext({...userContext,user:{...userContext.user, is_authenticated: false}})
      }
    }
    getUserInfo()
  }, [])
  return (
    <UserContext.Provider value={userContext}>
      {props.children}
    </UserContext.Provider>
  )
}
// class MainContextComponent extends Component{
//   constructor(props) {
//     super(props)
//     this.state = { userInfo: null, setUserInfo: this.setUserInfo}
//   }
//   setUserInfo = (data) => {
//     this.setState({ ...this.state, userInfo: data })
//   }
//   componentDidMount() {
//     const getUserInfo = async() => {
//       const userInfo = await (
//         await fetch('http://127.0.0.1:8000/profile/', {
//           method: 'GET', credentials: 'include'
//         })
//       ).json();
//       this.setUserInfo(userInfo)
//     }
//     getUserInfo()
//   }
//   render() {
//     console.log(this.state.userInfo)
//     return (
//       <MainContext.Provider value={this.state}>
//         {this.props.children}
//       </MainContext.Provider>
//     )
//   }
// }
export {UserContext, UserContextProvider}