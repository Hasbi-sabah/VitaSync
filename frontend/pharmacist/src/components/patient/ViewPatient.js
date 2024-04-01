import React, { useState } from "react";
import PatientDetails from "./PatientDetails";
import NewPatientRecord from "./NewPatientRecord";

// API call for patient record
const ViewPatient = ({ userId, closeOverlay, patientInfo }) => {
  const [showHistory, setShowHistory] = useState(false);

  const toggleHistory = () => {
    setShowHistory(!showHistory);
  };

  return (
    <div className="fixed inset-0 flex justify-center items-center backdrop-blur-sm backdrop-opacity-50 z-10 sm:mx-auto pt-24">
      <div className="bg-lightBlue2 rounded-lg shadow-lg sm:p-6 h-full z-20 overflow-auto pt-12 sm:max-w-screen relative lg:min-w-[40rem]">
        <svg
          className="absolute top-2 right-2 cursor-pointer"
          onClick={closeOverlay}
          xmlns="http://www.w3.org/2000/svg"
          width="32"
          height="32"
          fill="#ffffff"
          viewBox="0 0 256 256"
        >
          <path d="M165.66,101.66,139.31,128l26.35,26.34a8,8,0,0,1-11.32,11.32L128,139.31l-26.34,26.35a8,8,0,0,1-11.32-11.32L116.69,128,90.34,101.66a8,8,0,0,1,11.32-11.32L128,116.69l26.34-26.35a8,8,0,0,1,11.32,11.32ZM232,128A104,104,0,1,1,128,24,104.11,104.11,0,0,1,232,128Zm-16,0a88,88,0,1,0-88,88A88.1,88.1,0,0,0,216,128Z"></path>
        </svg>
        <h1 className="text-2xl text-left text-white font-bold mb-10">
          View Patient Details
        </h1>
        <div className="mb-4">
          {/* Add more patient details here */}
          <PatientDetails userId={userId} closeOverlay={closeOverlay} patientInfo={patientInfo} />
        </div>
        <div
          className="rounded-lg h-10 w-full mt-10 flex justify-between items-center cursor-pointer  bg-white"
          onClick={toggleHistory}
        >
          <h3 className="font-semibold text-lg pl-4">Past Record</h3>
          {showHistory ? (
            <svg
              className="ml-auto pr-4"
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              fill="#000000"
              viewBox="0 0 256 256"
            >
              <path d="M215.39,163.06A8,8,0,0,1,208,168H48a8,8,0,0,1-5.66-13.66l80-80a8,8,0,0,1,11.32,0l80,80A8,8,0,0,1,215.39,163.06Z"></path>
            </svg>
          ) : (
            <svg
              className="ml-auto pr-4"
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              fill="#000000"
              viewBox="0 0 256 256"
            >
              <path d="M213.66,101.66l-80,80a8,8,0,0,1-11.32,0l-80-80A8,8,0,0,1,48,88H208a8,8,0,0,1,5.66,13.66Z"></path>
            </svg>
          )}
        </div>
        {showHistory ? (
          <p className="mt-5 w-full h-12 border">
            This holds History (To be Implemented)
          </p>
        ) : (
          ""
        )}
        <NewPatientRecord closeOverlay={closeOverlay} userId={userId} />
      </div>
    </div>
  );
};

export default ViewPatient;