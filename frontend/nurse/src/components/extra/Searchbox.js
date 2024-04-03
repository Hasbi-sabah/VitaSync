import React, { useState, useEffect } from 'react';
import { useGetPatientByIdQuery } from '../../features/patient/patientApiSlice'
import ViewPatient from "../patient/ViewPatient";


const LookUp = ({ searchQuery }) => {
    const { data: patientInfo, isLoading, isError } = useGetPatientByIdQuery(searchQuery);
    const [showPatientDetails, setShowPatientDetails] = useState(false);
    console.log(patientInfo)

    useEffect(() => {
        if (!isLoading && !isError && patientInfo) {
            setShowPatientDetails(true);
        } else {
            setShowPatientDetails(false);
        }
    }, [isLoading, isError, patientInfo, searchQuery])

    return showPatientDetails ? (
        <ViewPatient closeOverlay={() => setShowPatientDetails(false)} userId={searchQuery} />
      ) : null;
}

const Searchbox = () => {
    const [searchQuery, setSearchQuery] = useState('');
    const [enterPressed, setEnterPressed] = useState(false);

    const handleInputChange = (event) => {
        setSearchQuery(event.target.value);
        setEnterPressed(false);
    }

    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            setEnterPressed(true); // Set the state to true when Enter is pressed
        }
    };

    const svgIcon = <svg xmlns="http://www.w3.org/2000/svg" width="40" height="30" color="#212121" viewBox="0 0 256 256"><path d="M229.66,218.34l-50.07-50.06a88.11,88.11,0,1,0-11.31,11.31l50.06,50.07a8,8,0,0,0,11.32-11.32ZM40,112a72,72,0,1,1,72,72A72.08,72.08,0,0,1,40,112Z"></path></svg>

    return (
        <div className='relative mr-32'>
            <input 
                type='text' 
                name='searchBox'
                placeholder='Patient lookup' 
                value={searchQuery} 
                onChange={handleInputChange} 
                onKeyDown={handleKeyPress}
                className='rounded-[20px] p-2 text-center h-16 w-128'
            />
            <span className='inline absolute h-10 w-10 top-4 left-5'>
                { svgIcon }
            </span>
            {enterPressed && <LookUp searchQuery={searchQuery} />}
        </div>
      );
};

export default Searchbox
