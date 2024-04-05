import React from 'react'

/**
 * Vital Component
 * @param Vitalreading - The reading value of the vital.
 * @param vitalName - The name of the vital.
 * @param currentDate - The date of the vital reading.
 * @returns Vital component to display vital information.
 */
const Vital = ({ Vitalreading, vitalName, currentDate }) => {
  if (!Vitalreading.includes('undefined')) {
    return (
      <div className='w-[11rem] h-[5rem]'>
          <p className='text-[1rem] font-semibold w-[11rem]'>{Vitalreading}</p>
          <p className='text-[1.2rem] font-meduim w-[11rem]'>{vitalName}</p>
          <p className='text-sm font-light w-[11rem]'>{currentDate.split(' ')[0]}</p>
      </div>
    )
  }
}

export default Vital;
