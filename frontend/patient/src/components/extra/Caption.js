import React from 'react'
import { Link } from 'react-router-dom'
import { useMediaQuery } from "react-responsive";

const Caption = () => {
  const isMobile = useMediaQuery({maxWidth:640});

  return (
    <div className={`bg-white mt-8 mx-12 p-4 pb-8 rounded-2xl sm:mt-12  ${isMobile ? '' : 'lg:my-20'} lg:px-10 lg:pt-12`}>
      <h2 className='text-2xl font-medium '>Book your appointment now!</h2>
      <p className='text-xl my-2'>Find a doctor and reserve an appointment.</p>
      <div className='flex justify-end mt-4' >
        <Link to={"/contactHCW"}>
          <span className='w-28 text-xl text-center p-2 bg-lightBlue2 text-white h-10 hover:bg-blue mr-auto rounded-sm'>
            Schedule
          </span>
        </Link>
      </div>
    </div>
  )
}

export default Caption