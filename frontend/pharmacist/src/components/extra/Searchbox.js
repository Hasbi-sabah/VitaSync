import React, { useState, useEffect } from 'react';
import { useGetPatientByIdQuery } from '../../features/patient/patientApiSlice'
import ViewPatient from "../patient/ViewPatient";
import { useGetDrugByIdQuery } from '../../features/drug/drugApiSlice';
import ViewDrug from './ViewDrug';


/**
 * LookUpPatient Component
 * 
 * This component allows for looking up patient details based on the provided search query.
 * It fetches patient information using the useGetPatientByIdQuery hook and displays the patient details
 * if found. If the patient is not found or if there's an error, it shows an alert message.
 * 
 * @param searchQuery - The search string used to look up the patient.
 * @returns The ViewPatient component if patient details are found, otherwise null.
 */
export const LookUpPatient = ({ searchQuery }) => {
    const { data: patientInfo, isLoading, isError, error } = useGetPatientByIdQuery(searchQuery);
    const [showPatientDetails, setShowPatientDetails] = useState(false);


    useEffect(() => {
        if (isLoading) {
            return; // Do nothing if still loading
        }
        if (isError) {
            alert("Patient not found.");
            return;
        }
        if (patientInfo) {
            setShowPatientDetails(true);
        } else {
            setShowPatientDetails(false);
        }
    }, [isLoading, isError, patientInfo, searchQuery, error]);

    return (
        <>
            {showPatientDetails && <ViewPatient closeOverlay={() => setShowPatientDetails(false)} userId={searchQuery} />}
        </>
      );
}

/**
 * LookUpDrug Component
 * 
 * This component is similar to LookUpPatient but is intended for looking up drug details
 * based on the provided search query.
 * 
 * @param searchQuery - The search string used to look up the drug.
 * @returns The ViewPatient component if drug details are found, otherwise null.
 */
export const LookUpDrug = ({ searchQuery }) => {
    console.log('Drug Search');
    const { data: drugInfo, isLoading, isError } = useGetDrugByIdQuery(searchQuery);
    const [showDrugDetails, setShowDrugDetails] = useState(false);
    console.log(drugInfo)

    useEffect(() => {
        if (!isLoading && !isError && drugInfo) {
            setShowDrugDetails(true);
        } else {
            setShowDrugDetails(false);
            alert("Drug not found.");
        }
    }, [isLoading, isError, drugInfo])

    // const dummy_data = [
    //     {
    //         "commercialName": "Aspirin",
    //         "activeIngredient": "Acetylsalicylic acid",
    //         "distributor": "Bayer",
    //         "dose": "81 mg",
    //         "form": "Tablet",
    //         "status": true,
    //         "price": 5.99,
    //         "description": "Aspirin is commonly used for pain relief and to reduce fever or inflammation."
    //     },
    //     {
    //         "commercialName": "Tylenol",
    //         "activeIngredient": "Acetaminophen",
    //         "distributor": "Johnson & Johnson",
    //         "dose": "500 mg",
    //         "form": "Caplet",
    //         "status": true,
    //         "price": 7.49,
    //         "description": "Tylenol is a common over-the-counter pain reliever and fever reducer."
    //     },
    //     {
    //         "commercialName": "Advil",
    //         "activeIngredient": "Ibuprofen",
    //         "distributor": "Pfizer",
    //         "dose": "200 mg",
    //         "form": "Capsule",
    //         "status": false,
    //         "price": 8.99,
    //         "description": "Advil is used to relieve pain from various conditions such as headache, dental pain, menstrual cramps, muscle aches, or arthritis."
    //     }
    // ]
    return (
    <>
        {showDrugDetails && <ViewDrug closeOverlay={() => setShowDrugDetails(false)} drugId={searchQuery} drugInfo={drugInfo} />}
    </>
    );
}

/**
 * Searchbox Component
 * 
 * This component provides a search input field for looking up patient details.
 * It allows users to enter a search query and triggers the LookUpPatient component
 * when the Enter key is pressed.
 * 
 * @returns The search input field along with the LookUpPatient component if Enter key is pressed.
 */
const Searchbox = ({ callSearch }) => {
    const [searchQuery, setSearchQuery] = useState('');
    const [enterPressed, setEnterPressed] = useState(false);

    const handleInputChange = (event) => {
        setSearchQuery(event.target.value);
        setEnterPressed(false);
    }

    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            setEnterPressed(true);
        }
    };

    const svgIcon = <svg xmlns="http://www.w3.org/2000/svg" width="40" height="30" color="#212121" viewBox="0 0 256 256"><path d="M229.66,218.34l-50.07-50.06a88.11,88.11,0,1,0-11.31,11.31l50.06,50.07a8,8,0,0,0,11.32-11.32ZM40,112a72,72,0,1,1,72,72A72.08,72.08,0,0,1,40,112Z"></path></svg>

    const [searchType, setSearchType] = useState('patient');
    const handleFilterChange = (event) => {
        if (event?.target?.value){
            setSearchType(event.target.value);
        }
    }
    return (
        <div className='relative flex flex-col'>
            <input 
                type='text' 
                name='searchBox'
                placeholder='Patient lookup' 
                value={searchQuery} 
                onChange={handleInputChange} 
                onKeyDown={handleKeyPress}
                className='rounded-[20px] p-2 text-center h-16 w-72 lg:w-128'
            />
            <span className='inline absolute h-10 w-10 top-4 left-5'>
                { svgIcon }
            </span>
            <select name="searchType" onChange={handleFilterChange} className="bg-gray rounded-md p-2 w-[60%]">
                <option className="text-xs" value="">
                    searchType
                </option>
                <option className="text-xs" value="patient">
                    Patient
                </option>
                <option className="text-xs" value="drug">
                    Drug
                </option>
            </select>
            {enterPressed && (searchType === 'patient') && <LookUpPatient searchQuery={searchQuery} />}
            {enterPressed && (searchType === 'drug') && <LookUpDrug searchQuery={searchQuery} />}
            {callSearch && (searchType === 'patient') && <LookUpPatient searchQuery={callSearch} />}
            {callSearch && (searchType === 'drug') && <LookUpDrug searchQuery={callSearch} />}
            
            {/* {console.log("Search comp", scannedId)} */}
            {/* {scannedId && <LookUp searchQuery={scannedId} />} */}
        </div>
      );
};

export default Searchbox
