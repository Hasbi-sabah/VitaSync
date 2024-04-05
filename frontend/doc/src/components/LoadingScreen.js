/**
 * Imports React for creating the LoadingScreen component.
 * @module LoadingScreen
 */
import React from 'react';

/**
 * Renders a loading screen with animated bouncing circles.
 * @function
 * @returns {JSX.Element} The JSX element representing the loading screen.
 */
const LoadingScreen = () => {
 return (
 <div className='flex space-x-2 justify-center items-center bg-blue-500 h-screen z-1000 backdrop-blur-md'>
    <span className='sr-only'>Loading...</span>
    <div className='h-8 w-8 bg-blue rounded-full animate-bounce [animation-delay:-0.3s]'></div>
    <div className='h-8 w-8 bg-blue rounded-full animate-bounce [animation-delay:-0.15s]'></div>
    <div className='h-8 w-8 bg-blue rounded-full animate-bounce '></div>
 </div>
 );
};

/**
 * Exports the LoadingScreen component.
 * @exports LoadingScreen
 */
export default LoadingScreen;
