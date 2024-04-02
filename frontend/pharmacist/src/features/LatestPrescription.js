import React from "react";
import ViewPatientPrescriptions from "../components/extra/ViewPatientPrescriptions";
import GenerateQRcode from "../components/extra/GenerateQRcode";

const LatestPrescription = ({
  latestPrescriptions,
  view,
  handleViewPrescriptions,
  handleClosePrescriptions,
  prescriptionId,
}) => {
  const handleApprove = (id) => {
    //POST status
  }
  const handleDenial = (id) => {
    //POST status
  }
  return (
    <>
      <div className="bg-white rounded-lg relative">
        <h2 className="text-center text-2xl font-medium p-3 shadow-md">
          Latest Prescriptions
        </h2>
        <svg
          className="h-12 absolute right-0 top-16"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 512 512"
        >
          <path d="M128 0C92.7 0 64 28.7 64 64v96h64V64H354.7L384 93.3V160h64V93.3c0-17-6.7-33.3-18.7-45.3L400 18.7C388 6.7 371.7 0 354.7 0H128zM384 352v32 64H128V384 368 352H384zm64 32h32c17.7 0 32-14.3 32-32V256c0-35.3-28.7-64-64-64H64c-35.3 0-64 28.7-64 64v96c0 17.7 14.3 32 32 32H64v64c0 35.3 28.7 64 64 64H384c35.3 0 64-28.7 64-64V384zM432 248a24 24 0 1 1 0 48 24 24 0 1 1 0-48z" />
        </svg>
        <td className="text-left pl-3">
          <div className=" relative">
            <h3 className="text-lg sm:text-[1.3rem] p-1 font-medium">
              <span className="text-actualLightBlue mr-1">Prescribed By:</span>
              {latestPrescriptions.prescribedById}
            </h3>
            <h3 className="text-lg sm:text-[1.3rem] p-1 font-medium">
              <span className="text-actualLightBlue mr-1">Filled By:</span>
              {latestPrescriptions?.filledById}
            </h3>
            
            {/* Add two buttons, fill or not fill */}
            <span
              className="text-lg lg:text-sm text-blue hover:cursor-pointer"
              onClick={handleViewPrescriptions}
            >
              View
            </span>
            {view && (
              <ViewPatientPrescriptions
                data={latestPrescriptions}
                handleClosePrescriptions={handleClosePrescriptions}
                handleApprove={handleApprove}
                handleDenial={handleDenial}
                prescriptionId={prescriptionId}
              />
            )}
          </div>
        </td>
      </div>
      <GenerateQRcode />
    </>
  );
};

export default LatestPrescription;
