import React, { useState } from "react";
import PatientDetails from "./PatientDetails";
import NewPatientRecord from "./NewPatientRecord";

// API call for patient record
const ViewPatient = ({ patientId, closeOverlay }) => {

  return (
    <div className="fixed inset-0 flex justify-center items-center backdrop-blur-sm backdrop-opacity-50 z-10 sm:mx-auto pt-24">
      <div className="bg-lightBlue2 rounded-lg shadow-lg sm:p-6 h-full z-20 overflow-auto pt-12 sm:max-w-screen sm:ml-56 lg:ml-64 relative">
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
          <PatientDetails patientId={patientId} closeOverlay={closeOverlay} />
        </div>
        <div
          className="rounded-lg h-10 w-full mt-10 flex justify-between items-center cursor-pointer  bg-white"
        >
          <h3 className="font-semibold text-lg pl-4">Past Record</h3>
        </div>
        <NewPatientRecord closeOverlay={closeOverlay} patientId={patientId} />
      </div>
    </div>
  );
};

export default ViewPatient;
