import React from 'react'

/**
 * Vital component displays a patient's vital reading, name, and date.
 * This component checks if the vital reading is not 'undefined' before rendering.
 * It takes in props for the vital reading, vital name, and current date.
 * @param {Object} props - The props object.
 * @param {string} props.Vitalreading - The patient's vital reading.
 * @param {string} props.vitalName - The name of the vital.
 * @param {string} props.currentDate - The current date.
 * @returns {JSX.Element|null} The rendered Vital component or null if the vital reading is 'undefined'.
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
