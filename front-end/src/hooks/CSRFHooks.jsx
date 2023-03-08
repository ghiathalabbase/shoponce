async function useCSRFSetter(setCSRFToken) {
    const response =  fetch('http://127.0.0.1:8000/get-csrftoken', {
      method: 'GET',
      credentials: 'include'
    })
    setCSRFToken(useCSRFCookieGetter())
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
export {useCSRFSetter, useCSRFCookieGetter}