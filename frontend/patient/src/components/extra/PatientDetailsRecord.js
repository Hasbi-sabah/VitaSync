import React from "react";
import { useGetPrescriptionByIdQuery } from "../../features/prescription/prescriptionApiSlice";
import LoadingScreen from "../LoadingScreen";
import PrescriptionRecordItem from "./PrescriptionRecordItem";

const PatientDetailsRecord = ({ data }) => {
  console.log("wio", data);

  const { data: prscData, isLoading } = useGetPrescriptionByIdQuery(
    data.prescriptionId
  );

  if (isLoading) {
    return <LoadingScreen />;
  }
  console.log("wio", prscData);

  return (
    <div className="w-screen sm:w-128">
      <div className="grid sm:items-center lg:items-baseline">
        {prscData  && (
          <PrescriptionRecordItem key={prscData.id} data={prscData} />
        )}
      </div>
      {data.diagnosis && (
        <div className="bg-white rounded-sm mx-auto w-full mt-5 ">
          <h2 className="text-center text-2xl font-meduim">Diagnosis</h2>
          <hr />
          {data.diagnosis}
        </div>
      )}
      {data.notes && (
        <div className="bg-white rounded-sm mx-auto w-full mt-5 ">
          <h2 className="text-center text-2xl font-meduim">Notes</h2>
          <hr />
          {data.notes}
        </div>
      )}
      {data.name && (
        <div className="bg-white rounded-sm mx-auto w-full mt-5 ">
          <h2 className="text-center text-2xl font-meduim">Procedures</h2>
          <hr />
          {data.name}
        </div>
      )}
      {data.vaccine && data.vaccine.length > 0 && (
        <div className="bg-white rounded-sm mx-auto w-full mt-5 ">
          <h2 className="text-center text-2xl font-meduim">Vaccine</h2>
          <hr />
          <div className="table w-full">
            <div className="table-header-group w-full">
              <div className="table-row w-full bg-gray">
                <div className="table-cell text-center">Drug</div>
                <div className="table-cell text-center">Dosage</div>
              </div>
            </div>
            <div className="table-row-group w-full">
              {data.vaccine.map((item, idx) => (
                <div className="table-row w-full" key={idx}>
                  <div className="table-cell text-center">{item.drug}</div>
                  <div className="table-cell text-left">{item.dosage}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default PatientDetailsRecord;
