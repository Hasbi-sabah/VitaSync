import { useState } from "react";
import CreateNewPatient from "../patient/CreateNewPatient";
import Searchbox from "./Searchbox";

/**
 * Component for creating and searching patients.
 * 
 * This component provides functionality to add a new patient,
 * search for existing patients, and scan QR codes for patient
 * identification.
 * 
 * @param setActiveQrScanner - Function to set the active state of the QR scanner.
 * @returns The JSX element representing the component.
 */
const CreateSearchPatient = ({ setActiveQrScanner, callSearch }) => {
  const [showAddPatient, setShowAddPatient] = useState(false);
  
  /**
   * Handles the click event for adding a new patient.
   */
  const handleOnClick = () => {
    setShowAddPatient(true);
  };

  /**
   * Closes the overlay for adding a new patient.
   */
  const closeOverlay = () => {
    setShowAddPatient(false);
  };
  return (
    <div className="mt-32 sm:mt-24 lg:mt-32 flex flex-col justify-center lg:flex-row items-center gap-5 sm:gap-8 lg:gap-20">
    {showAddPatient && <CreateNewPatient closeOverlay={closeOverlay} />}
    <button onClick={handleOnClick} className='uppercase bg-blue text-white h-16 w-72 rounded-[20px] relative font-semibold text-base hover:bg-lightBlue'>
          <span className="absolute top-3 left-5">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="#ffffff" viewBox="0 0 256 256"><path d="M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm0,192a88,88,0,1,1,88-88A88.1,88.1,0,0,1,128,216Zm48-88a8,8,0,0,1-8,8H136v32a8,8,0,0,1-16,0V136H88a8,8,0,0,1,0-16h32V88a8,8,0,0,1,16,0v32h32A8,8,0,0,1,176,128Z"></path></svg>
          </span>
          <span className="pl-8">Add new patient</span>
        </button>
        <button onClick={() => setActiveQrScanner(true)} className="h-16 w-72 bg-lightBlue rounded-[20px] relative text-base font-semibold text-white hover:bg-LightBlue2 hover:cursor-pointer">
        <span className="absolute top-3 left-10">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="40"
            height="40"
            fill="#ffffff"
            viewBox="0 0 256 256"
            
          >
            <path d="M224,40V80a8,8,0,0,1-16,0V48H176a8,8,0,0,1,0-16h40A8,8,0,0,1,224,40ZM80,208H48V176a8,8,0,0,0-16,0v40a8,8,0,0,0,8,8H80a8,8,0,0,0,0-16Zm136-40a8,8,0,0,0-8,8v32H176a8,8,0,0,0,0,16h40a8,8,0,0,0,8-8V176A8,8,0,0,0,216,168ZM40,88a8,8,0,0,0,8-8V48H80a8,8,0,0,0,0-16H40a8,8,0,0,0-8,8V80A8,8,0,0,0,40,88ZM80,72h96a8,8,0,0,1,8,8v96a8,8,0,0,1-8,8H80a8,8,0,0,1-8-8V80A8,8,0,0,1,80,72Zm8,96h80V88H88Z"></path>
          </svg>
        </span>
        <span className="pl-8">Scan QrCode</span>
      </button>
      <Searchbox callSearch={callSearch} />
    </div>
  );
};

export default CreateSearchPatient;
