import React from 'react';

/**
 * Vital component displays vital readings, vital name, and current date.
 * It checks if the Vitalreading includes 'undefined' to avoid rendering undefined values.
 * @param {Object} props - The props object.
 * @param {string} props.Vitalreading - The vital reading value.
 * @param {string} props.vitalName - The name of the vital.
 * @param {string} props.currentDate - The current date.
 * @returns {JSX.Element} The Vital component.
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
