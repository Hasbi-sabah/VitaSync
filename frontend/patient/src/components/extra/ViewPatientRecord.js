import React from 'react'

const ViewPatientRecord = ({ data, handleCloseRecord}) => {
  return (
    <div className='fixed insert-0 justify-center items-center backdrop-blur-sm backdrop-opacity-50 z-10 sm:mx-auto pt-24'>
        <div className='bg-lightBlue2 rounded-lg shadow-lg sm:p-6 h-full z-20 overflow-auto pt-12 sm:max-w-screen sm:ml-56 lg:ml-64 relative'>
        <svg
          className="absolute top-2 right-2 cursor-pointer"
          onClick={handleCloseRecord}
          xmlns="http://www.w3.org/2000/svg"
          width="32"
          height="32"
          fill="#ffffff"
          viewBox="0 0 256 256"
        >
          <path d="M165.66,101.66,139.31,128l26.35,26.34a8,8,0,0,1-11.32,11.32L128,139.31l-26.34,26.35a8,8,0,0,1-11.32-11.32L116.69,128,90.34,101.66a8,8,0,0,1,11.32-11.32L128,116.69l26.34-26.35a8,8,0,0,1,11.32,11.32ZM232,128A104,104,0,1,1,128,24,104.11,104.11,0,0,1,232,128Zm-16,0a88,88,0,1,0-88,88A88.1,88.1,0,0,0,216,128Z"></path>
        </svg>
        <h1 className="text-2xl text-left text-white font-bold mb-10">
            View Record Details
        </h1>
        <div>
        <div className="bg-white rounded-3xl mx-auto relative lg:w-[43rem] lg:h-[20rem] p-5">
          <p className="text-2xl font-meduim text-left">Recorded Vitals</p>
          <div className="grid gap-4 grid-cols-2 lg:grid-cols-3 mt-5 text-left">
            </div>
        </div>
        </div>
        </div>
    </div>
  )
}

export default ViewPatientRecord