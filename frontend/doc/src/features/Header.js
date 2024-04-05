
import React, { useEffect } from 'react';
import MediaQuery from 'react-responsive';
import { useGetHcwByIdQuery } from './hcw/hcwApiSlice';
import logo from '../inverted_logo.jpg';

/**
 * Header component displays the header of the application.
 * It fetches HCW information based on an ID stored in localStorage.
 * It uses MediaQuery to adjust the layout for mobile devices.
 * @returns {JSX.Element} The Header component.
 */
const Header = () => {
  const { data: hcwInfo, isLoading } = useGetHcwByIdQuery(localStorage.getItem("id"));
  const isMobile = MediaQuery({ maxWidth:640 })
  if (!isLoading) {  
    return (
        <header className='h-14 sm:h-[6vh] lg:h-[10vh] w-screen fixed top-0 flex justify-between items-center px-3 sm:px-5 bg-white z-50'>
          {isMobile ? <div></div> : ''}
          <div className="ml-44 sm:ml-20 lg:ml-0">
            <img className='h-12 sm:h-[5vh] lg:h-[9vh]' src={logo} alt='LOGO' />
          </div>
          <div className='flex align-center justify-center'>
            <MediaQuery minWidth={640}>
              <span className='text-2xl font-semibold mr-3'>Dr. </span>
              <span className='text-2xl font-normal uppercase '>{hcwInfo && (hcwInfo.lastName + ' ' + hcwInfo.firstName)}</span>
            </MediaQuery>
            <svg className='inline ml-3' xmlns="http://www.w3.org/2000/svg" width="40" height="30" fill="#212121" viewBox="0 0 256 256"><path d="M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24ZM74.08,197.5a64,64,0,0,1,107.84,0,87.83,87.83,0,0,1-107.84,0ZM96,120a32,32,0,1,1,32,32A32,32,0,0,1,96,120Zm97.76,66.41a79.66,79.66,0,0,0-36.06-28.75,48,48,0,1,0-59.4,0,79.66,79.66,0,0,0-36.06,28.75,88,88,0,1,1,131.52,0Z"></path></svg>
          </div>
        </header>
    );
  }
  };

export default Header;
