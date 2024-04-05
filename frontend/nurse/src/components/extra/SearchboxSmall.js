import { useState } from 'react';
import {useMediaQuery} from 'react-responsive';

/**
 * Component for a small search box to search for drugs.
 */
const SearchBoxSmall = () => {
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

    const isMobile = useMediaQuery({maxWidth:640})

    const svgIcon = <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" color="#212121" viewBox="0 0 256 256"><path d="M229.66,218.34l-50.07-50.06a88.11,88.11,0,1,0-11.31,11.31l50.06,50.07a8,8,0,0,0,11.32-11.32ZM40,112a72,72,0,1,1,72,72A72.08,72.08,0,0,1,40,112Z"></path></svg> 
    const svgIconMobile = <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" color="#212121" viewBox="0 0 256 256"><path d="M229.66,218.34l-50.07-50.06a88.11,88.11,0,1,0-11.31,11.31l50.06,50.07a8,8,0,0,0,11.32-11.32ZM40,112a72,72,0,1,1,72,72A72.08,72.08,0,0,1,40,112Z"></path></svg> 
  return (
    <div className='relative'>
            <input
                type='text'
                name='searchBoxSmall'
                placeholder='Patient lookup'
                value={searchQuery}
                onChange={handleInputChange}
                onKeyDown={handleKeyPress}
                className= 'rounded-full p-2 text-center h-5 w-40 sm:h-10 sm:w-80 bg-gray'
            />
            <span className='inline absolute h-6 w-6 top-2 left-2'>
                {isMobile ? svgIconMobile : svgIcon}
            </span>
    </div>
  )
}

export default SearchBoxSmall;
