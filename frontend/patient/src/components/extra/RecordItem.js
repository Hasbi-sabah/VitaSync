import React, { useState } from "react";
import ViewPatientRecord from "./ViewPatientRecord";

const RecordItem = ({ sn, data }) => {
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
        <td className="text-center">{data.date}</td>
        <td className="flex flex-col items-center">
          <div className="h-14 border-l rounded-full border-lightBlue text-center"></div>
          <div className="w-3 h-3 rounded-full bg-lightBlue border border-lightBlue"></div>
          <div className="h-14 border-l rounded-full border-lightBlue "></div>
        </td>
        <td className="text-left pl-3">
          <div>
            <h3 className="text-xl font-medium">Doctor: {data.assessedBy}</h3>
            <p>Diagnosis: {data.diagnosis}</p>
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
