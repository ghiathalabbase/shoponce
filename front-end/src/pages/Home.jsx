import React from 'react'
import TopStore from '../components/topStore'
import HomeSlider from '../components/HomeSlider'
import {useState, useEffect} from 'react'
import './css/home.css'

function Home() {
  const [data, setData] = useState({ top_stores: [] });

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
    <div className="row">
      <div className="best-stores col-md-4 rounded">
        <TopStore data={data}/>
      </div>
      <div className="main-image col-md rounded">
        {/* <HomeSlider/> */}
      </div>
    </div>
    </>
  )
}

export default Home