import React from 'react';
import { useGetPrescriptionByIdQuery } from "../../features/prescription/prescriptionApiSlice";
import LoadingScreen from "../LoadingScreen";
import PatientDetailsRecord from './PatientDetailsRecord';
import PatientDetailsVital from './PatientVitalsRecord';

/**
 * Component to view patient records.
 * @param data - The data of the patient record.
 * @param handleCloseRecord - Function to handle closing the record view.
 * @returns - The JSX element representing the component.
 */
const ViewPatientRecord = ({ data, handleCloseRecord}) => {
  const { data: prscData, isLoading} = useGetPrescriptionByIdQuery(
    data.prescriptionId
  );  
  if (isLoading) {
    return (
      <div className="fixed inset-0 flex justify-center items-center">
        <LoadingScreen />
      </div>
    );
  }
  return (
    <div className="fixed inset-0 flex justify-center items-center backdrop-blur-sm backdrop-opacity-50 z-10 sm:mx-auto pt-24">
      <div className="bg-lightBlue rounded-lg mb-10 shadow-lg sm:p-6 z-20 overflow-auto pt-12 sm:max-w-screen sm:ml-56 lg:ml-64 relative ove">
        <svg
          className="absolute top-2 right-2 cursor-pointer"
          onClick={handleCloseRecord}
          xmlns="http://www.w3.org/2000/svg"
          width="32"
          height="32"
          fill="#ffffff"
          viewBox="0 0 256 256"
        >
          <path d="M165.66,101.66,139.31,128l26.35,26.34a8,8,0,0,1-11.32,11.32L128,139.31l-26.34,26.35a8,8,0,0,1-11.32-11.32L116.69,128,90.34,101.66a8,8,0,0,1,11.32-11.32L128,116.69l26.34-26.35a8,8,0,0,1,11.32,11.32ZM232,128A104,104,0,1,1,128,24,104.11,104.11,0,0,1,232,128Zm-16,0a88,88,0,1,0-88,88A88.1,88.1,0,0,0,216,128Z"></path>
        </svg>
        <h1 className="text-2xl text-center text-white font-bold mb-5">
          Record Details
        </h1>
        <div className="mb-10">
          {data.assessedById ? (
          <PatientDetailsRecord data={data} prscData={prscData} />
          ) : (
          <PatientDetailsVital data={data} />
          )}
        </div>
      </div>
    </div>
  )
}

export default ViewPatientRecord
