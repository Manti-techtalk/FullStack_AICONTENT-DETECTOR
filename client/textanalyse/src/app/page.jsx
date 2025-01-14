"use client"
import React, { useState } from 'react'
import Header from '@/components/Header'


function page() {
  const [textValue,setTextValue] = useState('')
  const len = textValue.length
  return (
    <>
      <Header/>
      <div className="container-fluid bg-light vh-100">
      <div className="container ">
        <div className="row ">
          <div className="col-8">
            <h1>Text Analyzer</h1>
          </div>
          <div className="col-4 mt-3 ">
            <span className='btn border'>copy</span> <span className='btn border'>clear</span>
          </div>
        </div>
        <div className="row">
          <div className="col-12">
            <textarea
            value={textValue}
            onChange={(e)=>setTextValue(e.target.value)}
            style={{width:'100%',height:'15em'}} name="" id="" placeholder='Enter your text here'></textarea>
          </div>
        </div>
        <div className="row">
          <div className="col-3">
            <div
            style={{
              backgroundColor:'#E8F9FF',
              color: '#9381ff'
            }}
            className="card">
              <p className='p-1'>Words</p>
              <p>{len}</p>
            </div>
          </div>
          <div className="col-3">
            <div
            style={{
              backgroundColor:'#C2FFC7',
              color: '#5CB338'
            }}
            className="card">
              <p className='p-1'>characters</p>
              <p></p>
            </div>
          </div>
          <div className="col-3">
            <div
            style={{
              backgroundColor:'#F5EFFF',
              color: '#8B5DFF'
            }}
            className="card">
              <p className='p-1'>Reading Time</p>
              <p></p>
            </div>
          </div>
          <div className="col-3">
            <div
            style={{
              backgroundColor:'#FCFFC1',
              color: '#F26B0F'
            }}
            className="card">
              <p className='p-1'>Complexity</p>
              <p></p>
            </div>
          </div>
        </div>
      </div>
    </div>
</>
  )
}

export default page