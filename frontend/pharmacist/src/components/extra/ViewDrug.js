import React from "react";
import ToggleSwitch from "./ToggleSwitch";

const ViewDrug = ({ drugInfo, drugId, closeOverlay }) => {
  return (
    <div className="fixed inset-0 flex justify-center items-center backdrop-blur-sm backdrop-opacity-50 z-10 sm:mx-auto pt-24">
      <div className="bg-lightBlue2 rounded-lg shadow-lg sm:p-6 py-10 z-20 overflow-auto pt-12 sm:max-w-screen relative min-w-[20rem] lg:min-w-[40rem]">
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
        <div className="table w-full">
          <div className="table-header-group">
            <div className="table-row relative h-[6rem]">
              <h2 className="table-cell text-center w-[60%] text-2xl">Set Status</h2>
              <span className="table-cell absolute top-1 w-[40%] right-2">
                <ToggleSwitch />
              </span>
            </div>
          </div>
          <div className="table-row-group">
            <div className="table-row py-5 h-[4rem] w-full">
              <h3 className="pl-3 text-xl font-[600] table-cell">Commercial Name: </h3>
              <span className="text-lg table-cell">{drugInfo?.commercialName}</span>
            </div>
            <div className="table-row py-5 h-[4rem]">
              <h3 className="pl-3 text-xl font-[600] table-cell">Active Ingredient: </h3>
              <span className="text-lg table-cell">{drugInfo?.activeIngredient}</span>
            </div>
            <div className="table-row py-5 h-[4rem]">
              <h3 className="pl-3 text-xl font-[600] table-cell">Distributor: </h3>
              <span className="text-lg table-cell">{drugInfo?.distributor}</span>
            </div>
            <div className="table-row py-5 h-[4rem]">
              <h3 className="pl-3 text-xl font-[600] table-cell">Dose: </h3>
              <span className="text-lg table-cell">{drugInfo?.dose}</span>
            </div>
            <div className="table-row py-5 h-[4rem]">
              <h3 className="pl-3 text-xl font-[600] table-cell">Form: </h3>
              <span className="text-lg table-cell">{drugInfo?.form}</span>
            </div>
            <div className="table-row py-5 h-[4rem]">
              <h3 className="pl-3 text-xl font-[600] table-cell">Status: </h3>
              <span className="text-lg table-cell">{drugInfo?.status ? 'Active' : 'Inactive'}</span>
            </div>
            <div className="table-row py-5 h-[4rem]">
              <h3 className="pl-3 text-xl font-[600] table-cell">Price: </h3>
              <span className="text-lg table-cell">{drugInfo?.price}</span>
            </div>
            <div className="table-row py-5 h-[4rem]">
              <h3 className="pl-3 text-xl font-[600] table-cell">Description: </h3>
              <span className="w-52">{drugInfo?.description}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ViewDrug;
