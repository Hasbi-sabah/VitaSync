import React, { useState } from "react";
import ViewPatientRecord from "./ViewPatientRecord";
import {useGetHcwByIdQuery } from "../../features/hcw/hcwApiSlice"

const RecordItem = ({ sn, data }) => {
  const { data: hcwInfo } = useGetHcwByIdQuery(data.assessedById || data.takenById)
  const bgColor = sn % 2 === 0 ? "bg-gray" : "";
  const [view, setView] = useState(false);

  const handleViewRecord = () => setView(true);
  const handleCloseRecord = () => {
    setView(false);
    console.log("clicked")
  };
  return (
      <tr
        className={`text-textGray text-xl lg:text-base text-center ${bgColor}`}
      >
        <td className="text-center">{data.created_at}</td>
        <td className="flex flex-col items-center">
          <div className="h-14 border-l rounded-full border-lightBlue text-center"></div>
          <div className="w-3 h-3 rounded-full bg-lightBlue border border-lightBlue"></div>
          <div className="h-14 border-l rounded-full border-lightBlue "></div>
        </td>
        <td className="text-left pl-3">
          <div>
            {data.assessedById ? (
              hcwInfo && <h3 className="text-xl font-medium">With Doctor: {hcwInfo.lastName + ' ' + hcwInfo.firstName}</h3>
            ) : (
              hcwInfo && <h3 className="text-xl font-medium">Taken By: {hcwInfo.lastName + ' ' + hcwInfo.firstName}</h3>
            )}
            
            <span className="text-sm text-blue hover:cursor-pointer" onClick={handleViewRecord}>
              View
            </span>
            {view && <ViewPatientRecord data={data} handleCloseRecord={handleCloseRecord} />}
          </div>
        </td>
      </tr>
  );
};

export default RecordItem;
