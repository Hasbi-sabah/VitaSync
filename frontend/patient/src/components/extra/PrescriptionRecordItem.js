import React, { useState } from "react";
import ViewPatientPrescriptions from "./ViewPatientPrescriptions";

const PrescriptionRecordItem = ({ sn, data, view, handleViewPrescriptions, handleClosePrescriptions }) => {
  const bgColor = sn % 2 === 0 ? "bg-gray" : "";

  // API call to get
  // `/api/hcw/${id}` for:
  // - data.prescribedById
  // - data.filledById
  return (
    <tr
      className={`text-textGray text-lg p-1 lg:text-base text-center ${bgColor}`}
    >
      <td className="text-center">{data.date}</td>
      <td className="flex flex-col items-center">
        <div className="h-24 border-l rounded-full border-lightBlue text-center"></div>
        <div className="w-4 h-4 rounded-full bg-lightBlue border border-lightBlue"></div>
        <div className="h-24 border-l rounded-full border-lightBlue "></div>
      </td>
      <td className="text-left pl-3">
        <div>
          <h3 className="text-lg sm:text-[1.3rem] p-1 font-medium">
            <span className="text-actualLightBlue mr-1">Prescribed By:</span>
            {data.prescribedById}
          </h3>
          <h3 className="text-lg sm:text-[1.3rem] p-1 font-medium">
            <span className="text-actualLightBlue mr-1">Filled By:</span>
            {data.filledById}
          </h3>
          <h3 className="text-lg sm:text-[1.3rem] p-1 font-medium mb-3">
            <span className="text-actualLightBlue mr-2">Prescription filled:</span>
                {data.status ? 
                    <span className="text-green">Filled</span> 
                    : <span className="text-red">Pending</span>
                }
          </h3>
          <span
            className="text-lg lg:text-sm text-blue hover:cursor-pointer"
            onClick={handleViewPrescriptions}
          >
            View
          </span>
          {view && (
            <ViewPatientPrescriptions
              data={data}
              handleClosePrescriptions={handleClosePrescriptions}
            />
          )}
        </div>
      </td>
    </tr>
  );
};

export default PrescriptionRecordItem;
