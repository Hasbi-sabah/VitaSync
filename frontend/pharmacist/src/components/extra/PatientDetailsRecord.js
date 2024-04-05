import React, { useState } from "react";
import LoadingScreen from "../LoadingScreen";
import { useGetPrescriptionFilledByIdMutation } from "../../features/prescription/prescriptionApiSlice";
import { useGetHcwByIdQuery } from "../../features/hcw/hcwApiSlice";
import { useGetDrugPrescriptionExtendedByIdQuery } from "../../features/prescription/prescriptionApiSlice";

/**
 * Component to display patient details and records.
 * 
 * This component fetches and displays patient prescription details,
 * diagnosis, notes, procedures, and vaccine records.
 * 
 * @param data - Patient data including prescription details.
 * @param prscData - Prescription data associated with the patient.
 * @returns The JSX element representing the component.
 */
const PatientDetailsRecord = ({ data, prscData }) => {
  const filledById = prscData?.filledById || "";
  const prescribedById = prscData?.prescribedById || "";
  
  // API Querys
  const { data: filledByInfo, isLoading: f } = useGetHcwByIdQuery(filledById);
  const { data: prescribedByInfo, isLoading: p } = useGetHcwByIdQuery(prescribedById);
  const [sendProcedureRequest, { isLoading: isSendingRequest }] =
    useGetPrescriptionFilledByIdMutation();

  const [requestSent, setRequestSent] = useState(false);

  const sendRequest = () => {
    if (!prscData.status && !requestSent) {
      sendProcedureRequest(data.prescriptionId)
        .unwrap()
        .then(() => {
          setRequestSent(true);
          window.location.reload();
        })
        .catch((error) => {
          // Handle error
          alert("Failed to send request:", error);
        });
    }
  };
  const { data: mergedArray, isLoading: isPrscDataLoading } =
    useGetDrugPrescriptionExtendedByIdQuery(data.prescriptionId);

  if (f || p || isPrscDataLoading) {
    return <LoadingScreen />;
  }
  return (
    <div className="w-screen sm:w-128">
      <div className="grid sm:items-center lg:items-baseline">
        {mergedArray && mergedArray.length > 0 && (
          <div className="bg-white rounded-lg mt-5 p-5 w-full">
            <div className="flex">
            <button
                className="bg-blue hover:bg-blue-700 text-white font-bold h-10 px-4 mr-20 rounded"
                onClick={sendRequest}
                disabled={prscData.status || requestSent || isSendingRequest}
              >
                {prscData.status || requestSent ? "Filled" : "Mark as filled"}
              </button>
              
            <h2 className="text-center font-bold text-2xl font-meduim p-3">
              Prescriptions
            </h2>
              </div>
            <tr
              className={`text-textGray p-1 lg:text-base text-center`}
            >              
              <td className="text-left pl-3">
                <div>
                  <h3 className="sm:text-[1.3rem] p-1 font-small">
                    <span className="text-actualLightBlue mr-1">
                      Prescribed By:
                    </span>
                    Dr. {prescribedByInfo.lastName} {prescribedByInfo.firstName}
                  </h3>
                  <h3 className="sm:text-[1.3rem] p-1 font-small">
                    <span className="text-actualLightBlue mr-1">
                      Date:
                    </span>
                    {prscData.created_at}
                  </h3>
                  {prscData.status && (
                    <h3 className="sm:text-[1.3rem] p-1 font-small">
                      <span className="text-actualLightBlue mr-1">
                        Filled By:
                      </span>
                      {filledByInfo.lastName} {filledByInfo.firstName}
                    </h3>
                  )}
                  <h3 className="sm:text-[1.3rem] p-1 font-small mb-3">
                    <span className="text-actualLightBlue mr-2">
                      Prescription filled:
                    </span>
                    {prscData.status ? (
                      <span className="text-green">Filled</span>
                    ) : (
                      <span className="text-red">Pending</span>
                    )}
                  </h3>
                </div>
              </td>
            </tr>
            {mergedArray &&
              mergedArray.map((item, idx) => (
                <div className="p-2 " key={idx}>
                  {item.commercialName} ({item.activeIngredient}), {item.form},{" "}
                  {item.dose} : {item.instructions}
                </div>
              ))}
          </div>
        )}
      </div>
      {data.diagnosis && (
          <div className="bg-white rounded-lg mx-auto w-full mt-5 ">
            <h2 className="text-center text-2xl font-bold font-meduim p-3">Diagnosis</h2>
            <div className="p-3">{data.diagnosis}</div>
          </div>
        )}
        {data.notes && (
          <div className="bg-white rounded-lg mx-auto w-full mt-5 ">
            <h2 className="text-center text-2xl  font-bold font-meduim p-3">Notes</h2>
            {data.notes}
          </div>
        )}
        {data.name && (
          <div className="bg-white rounded-lg mx-auto w-full mt-5">
              <h2 className="text-center text-2xl font-bold font-meduim">Procedures</h2>
              
            <div className="p-3">{data.name}</div>
          </div>
        )}
        {data.vaccine && data.vaccine.length > 0 && (
          <div className="bg-white rounded-lg mx-auto w-full mt-5 ">
            <h2 className="text-center text-2xl font-bold font-meduim">Vaccine</h2>
            <hr />
            <div className="table w-full">
              <div className="table-header-group w-full">
                <div className="table-row w-full bg-gray">
                  <div className="table-cell text-center">Drug</div>
                  <div className="table-cell text-center">Dosage</div>
                </div>
              </div>
              <div className="table-row-group w-full">
                {data.vaccine &&
                  data.vaccine.map((item, idx) => (
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
