import { useState, useEffect } from 'react';

const showStore = (store) => {
    return (
        <>
        <div className="store d-flex justify-content-between align-items-center">
            <div className="d-flex align-items-center gap-3 me-2">
                <div className="image">
                    <img className='rounded-pill' src={`http://127.0.0.1:8000/` + store.logo} alt="noimage" width={75} height={75}/>
                </div>
                <div className="tiny-description">
                    <h5 className='mb-1 pointer'>{store.name}</h5>
                    <p>Some Description</p>
                    <p><b>Rate : {store.rate} / 5</b></p>
                </div>
            </div>
            <div className="visit-button">
                <div className="link rounded-pill pointer">
                    <div>Visit</div>
                </div>
            </div>
        </div>
        </>
    )
}

function TopStore(props) {
    let store1 = props.data.top_stores[0]
    console.log(store1)
    return (
        <>
        <div className="block ">
            <div className="heading">
                <h2 className='p-4'>Top Stores</h2>
            </div>
            <div className="top-stores d-flex flex-column gap-3 border p-4 bg-white shadow">
                {props.data.top_stores.map(showStore)}
            </div>
        </div>
        </>
    )
}

export default TopStore