import React from "react";
import { useGetDrugPrescriptionExtendedByIdQuery } from "../../features/prescription/prescriptionApiSlice";
import LoadingScreen from "../LoadingScreen";

const ViewPatientPrescriptions = ({ data, handleClosePrescriptions }) => {
  const { data: prscDrugs, isLoading } =
    useGetDrugPrescriptionExtendedByIdQuery(data.id);
  if (isLoading) {
    return <LoadingScreen />;
  }
  console.log(prscDrugs);
  return (
    <div className="fixed inset-0 flex justify-center items-center backdrop-blur-sm backdrop-opacity-50 z-10 sm:mx-auto pt-24">
      <div className="bg-lightBlue2 rounded-lg mb-10 shadow-lg sm:p-6 z-20 overflow-auto pt-12 sm:max-w-screen sm:ml-56 lg:ml-64 relative">
        <svg
          className="absolute top-2 right-2 cursor-pointer"
          onClick={handleClosePrescriptions}
          xmlns="http://www.w3.org/2000/svg"
          width="32"
          height="32"
          fill="#ffffff"
          viewBox="0 0 256 256"
        >
          <path d="M165.66,101.66,139.31,128l26.35,26.34a8,8,0,0,1-11.32,11.32L128,139.31l-26.34,26.35a8,8,0,0,1-11.32-11.32L116.69,128,90.34,101.66a8,8,0,0,1,11.32-11.32L128,116.69l26.34-26.35a8,8,0,0,1,11.32,11.32ZM232,128A104,104,0,1,1,128,24,104.11,104.11,0,0,1,232,128Zm-16,0a88,88,0,1,0-88,88A88.1,88.1,0,0,0,216,128Z"></path>
        </svg>
        <h1 className="text-3xl text-center text-white font-normal mb-5 mx-10">
          Full Prescription
        </h1>
        <div className="mb-10">
          {/* Add more patient details here */}
          <div className="bg-white rounded-lg my-5 w-full max-h-[60vh] overflow-auto">
            <hr />
            <div className="table w-full">
              <div className="table-header-group w-full">
                <div className="table-row w-full h-12 text-lg font-semibold bg-gray">
                  <div className="table-cell text-xl text-center p-2">Drug</div>
                  <div className="table-cell text-xl text-center p-2">
                    instructions
                  </div>
                </div>
              </div>
              <div className="table-row-group w-full">
                {prscDrugs &&
                  prscDrugs.map((drug, idx) => (
                    <div className="table-row w-full h-8" key={idx}>
                      <div className="table-cell text-center p-2 sm:text-lg">
                        {drug.commercialName} ({drug.activeIngredient}),{" "}
                        {drug.form}, {drug.dose}
                      </div>
                      <div className="table-cell text-center p-2 sm:text-lg">
                        {drug.instructions}
                      </div>
                    </div>
                  ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ViewPatientPrescriptions;
