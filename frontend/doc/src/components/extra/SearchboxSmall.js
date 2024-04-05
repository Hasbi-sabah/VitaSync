import React, { useState, useEffect } from 'react';
import { useDrugLookUpQuery } from '../../features/drug/drugApiSlice';


/**
 * Component to look up drug information based on a search query.
 * @param searchQuery - The search query for the drug.
 * @param setDrugOptions - Function to set the drug options based on the search results.
 * @returns - The JSX element representing the component.
 */
const LookUpDrug = ({ searchQuery, setDrugOptions }) => {
    const { data: drugInfo, isLoading, isError } = useDrugLookUpQuery({'name': searchQuery});

    useEffect(() => {
        if (!isLoading && !isError && drugInfo) {
            setDrugOptions(drugInfo);
        }
    }, [isLoading, isError, drugInfo, searchQuery, setDrugOptions]);

    return null
}

/**
 * Component for a small search box to search for drugs.
 * @param key - The key for React rendering.
 * @param setDrugOptions - Function to set the drug options based on the search results.
 * @param setSearchListVisible - Function to set the visibility of the search list.
 * @param searchValue - The current value of the search input.
 * @param setSearchValue - Function to set the value of the search input.
 * @returns - The JSX element representing the component.
 */
const SearchBoxSmall = ({ key, setDrugOptions, setSearchListVisible, searchValue, setSearchValue}) => {

    const handleInputChange = (event) => {
        setSearchListVisible(true);
        setSearchValue(event.target.value);

    }

    const svgIcon = <svg xmlns="http://www.w3.org/2000/svg" width="40" height="30" color="#212121" viewBox="0 0 256 256"><path d="M229.66,218.34l-50.07-50.06a88.11,88.11,0,1,0-11.31,11.31l50.06,50.07a8,8,0,0,0,11.32-11.32ZM40,112a72,72,0,1,1,72,72A72.08,72.08,0,0,1,40,112Z"></path></svg>

    return (
        <div className='relative'>
            <input
                type='text'
                name='drugSearchBox'
                placeholder='drug search'
                value={searchValue}
                onChange={handleInputChange}
                // onBlur={handleBlur}
                className='rounded-[20px] p-2 text-center h-16 w-150'
            />
            <span className='inline absolute h-10 w-10 top-4 left-5'>
                { svgIcon }
            </span>
            <LookUpDrug searchQuery={searchValue} setDrugOptions={setDrugOptions} />
        </div>
      );
};


// export const SearchOptions = ({ userId}) => {
//     const [searchResult, setSearchResult] = useState({});
//     const [search, setSearch] = useState("")
//     const handleOnchange = (event) => setSearch(event.target.value)
//     return(
//     <input
//         name="searchResult"
//         onChange={handleOnchange}
//         value={searchResult}
//     >
//         <option>...</option>
//         {searchResult.map((searchItem, idx) => (
//             <option name={searchItem} key={idx} value={searchItem}>{searchItem}</option>
//         ))}
//         {search && <LookUpDrug userId={userId} searchQuery={search} heandleSearchResult={setSearchResult} />}
//     </input>)
// }


export default SearchBoxSmall
