import React, { useState } from "react";
import ViewPatientPrescriptions from "../components/extra/ViewPatientPrescriptions";
import GenerateQRcode from "../components/extra/GenerateQRcode";
import LoadingScreen from "../components/LoadingScreen";
import {useGetHcwByIdQuery} from './hcw/hcwApiSlice'
import {useGetPrintPrescriptionByIdQuery} from './prescription/prescriptionApiSlice'

const LatestPrescription = ({
  latestPrescription,
}) => {
  const { data: prescribedByInfo, isLoading: p } = useGetHcwByIdQuery(latestPrescription.prescribedById)
  // const { data: prsc, isLoading, error } = useGetPrintPrescriptionByIdQuery(latestPrescription.id);
  const [view, setView] = useState(false);
  const handlePrintClick = () => {
    fetch(`/print_prescription/${latestPrescription.id}`, {
      headers: {
        Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMWEzNGQ0MzItY2VkMi00NjJhLTkzZmItMjYzNzU0NGYxOTQxIiwiaWF0IjoxNzEyMjIyMzY0LCJleHAiOjE3MTIzMDg3NjR9.vEgitgvJ1M9nsahMEVzLyJuHzGeSs41O87Y5tfl9nTU', // Add your access token here if needed
      },
    })
      .then(response => response.blob())
      .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'prescription.pdf';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
      })
      .catch(error => console.error('Error downloading prescription:', error));
};
  if (p) {
      return <LoadingScreen />; 
  }
  return (
    <>
      <div className="bg-white rounded-lg relative">
        <h2 className="text-center text-2xl font-medium p-3 shadow-md">
          Latest Prescriptions
        </h2>
        <div onClick={handlePrintClick} className="cursor-pointer">
        <svg
          className="h-12 absolute right-0 top-16"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 512 512"
        >
          <path d="M128 0C92.7 0 64 28.7 64 64v96h64V64H354.7L384 93.3V160h64V93.3c0-17-6.7-33.3-18.7-45.3L400 18.7C388 6.7 371.7 0 354.7 0H128zM384 352v32 64H128V384 368 352H384zm64 32h32c17.7 0 32-14.3 32-32V256c0-35.3-28.7-64-64-64H64c-35.3 0-64 28.7-64 64v96c0 17.7 14.3 32 32 32H64v64c0 35.3 28.7 64 64 64H384c35.3 0 64-28.7 64-64V384zM432 248a24 24 0 1 1 0 48 24 24 0 1 1 0-48z" />
        </svg>
        </div>
        <div className="text-left pl-3 table-cell">
          <div className=" relative">
            <h3 className="text-lg sm:text-[1.3rem] p-1 font-medium">
              <span className="text-actualLightBlue mr-1">Prescribed By:</span>
              Dr. {prescribedByInfo.lastName} {prescribedByInfo.firstName}
            </h3>
            <h3 className="text-lg sm:text-[1.3rem] p-1 font-medium">
              <span className="text-actualLightBlue mr-1">Date:</span>
              {latestPrescription.created_at}
            </h3>
            <h3 className="text-lg sm:text-[1.3rem] p-1 font-medium mb-3">
              <span className="text-actualLightBlue mr-2">
                Prescription status:
              </span>
              {latestPrescription.status ? (
                <span className="text-green">Filled</span>
              ) : (
                <span className="text-red">Pending</span>
              )}
            </h3>
            <span
              className="text-lg lg:text-sm text-blue hover:cursor-pointer"
              onClick={() => setView(true)}
            >
              View
            </span>
            {view && (
              <ViewPatientPrescriptions
                data={latestPrescription}
                handleClosePrescriptions={() => setView(false)}
              />
            )}
          </div>
        </div>
      </div>
    </>
  );
};

export default LatestPrescription;
