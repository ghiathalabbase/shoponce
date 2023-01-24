async function useCSRFSetter(setCSRFToken) {
  if (!useCSRFCookieGetter()) {
    const response = await fetch('http://127.0.0.1:8000/login/', {
      method: 'GET',
      credentials: 'include'
    })
    const data = await response.json()
    setCSRFToken(useCSRFCookieGetter())
  }
}

function useCSRFCookieGetter() {
  const cookieName = 'csrftoken'
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    let cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      if (cookie.substring(0, cookieName.length + 1) === cookieName + "=") {
        cookieValue = decodeURIComponent(cookie.substring(cookieName.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
// async function useUserGetter(){
//   const userInfo = await (await (await fetch('http://127.0.0.1:8000/profile/')).json());
//   if (!userInfo) redirect('/login')
// }
export {useCSRFSetter, useCSRFCookieGetter}