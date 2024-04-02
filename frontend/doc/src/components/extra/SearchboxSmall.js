import React, { useState, useEffect } from 'react';
import { useDrugLookUpQuery } from '../../features/drug/drugApiSlice';


const LookUpDrug = ({ userId, searchQuery, setDrugOptions }) => {
    // const search = `name:${searchQuery}`
    const { data: drugInfo, isLoading, isError } = useDrugLookUpQuery({'name': searchQuery});
    console.log(drugInfo)

    // drugInfo && setDrugOptions(drugInfo)
    // console.log('drugInfo')
    useEffect(() => {
        if (!isLoading && !isError && drugInfo) {
            setDrugOptions(drugInfo);
        }
    }, [isLoading, isError, drugInfo, searchQuery, setDrugOptions]);

    return null
}

const SearchBoxSmall = ({ userId, setDrugOptions }) => {
    const [searchQuery, setSearchQuery] = useState('');

    const handleInputChange = (event) => {
        setSearchQuery(event.target.value);
    }

    // useEffect(() => {
    //     LookUpDrug( userId, searchQuery, setDrugOptions)
    // }, [searchQuery, setDrugOptions, userId])

    const svgIcon = <svg xmlns="http://www.w3.org/2000/svg" width="40" height="30" color="#212121" viewBox="0 0 256 256"><path d="M229.66,218.34l-50.07-50.06a88.11,88.11,0,1,0-11.31,11.31l50.06,50.07a8,8,0,0,0,11.32-11.32ZM40,112a72,72,0,1,1,72,72A72.08,72.08,0,0,1,40,112Z"></path></svg>

    return (
        <div className='relative'>
            <input
                type='text'
                name='drugSearchBox'
                placeholder='drug search'
                value={searchQuery}
                onChange={handleInputChange}
                className='rounded-[20px] p-2 text-center h-16 w-72 lg:w-[24rem]'
            />
            <span className='inline absolute h-10 w-10 top-4 left-5'>
                { svgIcon }
            </span>
            <LookUpDrug userId={userId} searchQuery={searchQuery} setDrugOptions={setDrugOptions} />
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
