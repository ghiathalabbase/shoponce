import React from 'react'
import TopStores from '../components/TopStores'
import HomeSlider from '../components/HomeSlider'
import {useState, useEffect} from 'react'
import './css/home.css'
import { useLocation } from 'react-router-dom'

function Home() {
  const [data, setData] = useState({ top_stores: [] });
  const location = useLocation()
  useEffect(() => {
    const requestOptions = {}
    fetch("http://127.0.0.1:8000/store/get-top/")
    .then((response) => response.json())
    .then((data) => {
      setData({top_stores: data})
    })
  }, [])

  // const getTopStores = () => {}
  // getTopStores()

  return (
    <>
      {location.state}
      <div className="row">
        <div className="best-stores col-md-4 rounded">
          <TopStores data={data}/>
        </div>
        <div className="main-image col-md rounded">
          {/* <HomeSlider/> */}
        </div>
      </div>
    </>
  )
}

export default Home