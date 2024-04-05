import { useState } from 'react';

/**
 * Searchbox Component
 * 
 * This component provides a search input field for looking up patient details.
 * It allows users to enter a search query and triggers the LookUpPatient component
 * when the Enter key is pressed.
 * 
 * @returns The search input field along with the LookUpPatient component if Enter key is pressed.
 */
const Searchbox = () => {
    const [searchQuery, setSearchQuery] = useState('');

    const handleInputChange = (event) => {
        setSearchQuery(event.target.value);
        handleSearch();
    }

    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            handleSearch();
        }
    };

    const handleSearch = () => {
        // handle search logic
        console.log('Search query: ', searchQuery)
    };

    const svgIcon = <svg xmlns="http://www.w3.org/2000/svg" width="40" height="30" color="#212121" viewBox="0 0 256 256"><path d="M229.66,218.34l-50.07-50.06a88.11,88.11,0,1,0-11.31,11.31l50.06,50.07a8,8,0,0,0,11.32-11.32ZM40,112a72,72,0,1,1,72,72A72.08,72.08,0,0,1,40,112Z"></path></svg>
  return (
    <div className='relative'>
        <input 
            type='text' 
            name='searchBox'
            placeholder='Patient lookup' 
            value={searchQuery} 
            onChange={handleInputChange} 
            onKeyDown={handleKeyPress}
            className='rounded-[20px] p-2 text-center h-16 w-72 lg:w-[24rem]'
        />
        <span className='inline absolute h-10 w-10 top-4 left-5'>
            { svgIcon }
        </span>
    </div>
  )
}

export default Searchbox