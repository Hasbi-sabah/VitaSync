import React, { useState } from "react";
import ViewPatient from "./ViewPatient";
import { useMediaQuery } from "react-responsive";
import { useLocation } from "react-router-dom";

const UserItem = ({ userId, sn, name, sex, age, contact, date, time }) => {
  const location = useLocation();
  const isDashboard = location.pathname === "/dashboard";
  const bgColor = sn % 2 === 1 ? "bg-gray" : "";
  const [showPatientDetails, setShowPatientDetails] = useState(false);
  const handleOnClick = () => {
    setShowPatientDetails(true);
  };

  const closeOverlay = () => {
    setShowPatientDetails(false);
  };

  const isMobile = useMediaQuery({ maxWidth: 1024 });
  return (
    <tr
      className={`text-textGray text-xl lg:text-base text-center h-12 ${bgColor}`}
    >
      <td>{sn}</td>
      <td className="pl-2 sm:pl-3 py-2 sm:max-w-18 lg:max-w-24 text-left text-wrap mx-auto">
        {name}
      </td>
      <td>{sex}</td>
      <td>{age}</td>
      {!isMobile && <td>{contact}</td>}
      {!isMobile && <td>{date}</td>}
      {isDashboard && isMobile && <td>{time}</td>}
      <td>
        {/* Overlay */}
        {showPatientDetails && (
          <ViewPatient closeOverlay={closeOverlay} userId={userId} />
        )}
        <svg
          onClick={handleOnClick}
          className="hover:cursor-pointer"
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          fill="#3e3e3e"
          viewBox="0 0 256 256"
        >
          <path d="M247.31,124.76c-.35-.79-8.82-19.58-27.65-38.41C194.57,61.26,162.88,48,128,48S61.43,61.26,36.34,86.35C17.51,105.18,9,124,8.69,124.76a8,8,0,0,0,0,6.5c.35.79,8.82,19.57,27.65,38.4C61.43,194.74,93.12,208,128,208s66.57-13.26,91.66-38.34c18.83-18.83,27.3-37.61,27.65-38.4A8,8,0,0,0,247.31,124.76ZM128,192c-30.78,0-57.67-11.19-79.93-33.25A133.47,133.47,0,0,1,25,128,133.33,133.33,0,0,1,48.07,97.25C70.33,75.19,97.22,64,128,64s57.67,11.19,79.93,33.25A133.46,133.46,0,0,1,231.05,128C223.84,141.46,192.43,192,128,192Zm0-112a48,48,0,1,0,48,48A48.05,48.05,0,0,0,128,80Zm0,80a32,32,0,1,1,32-32A32,32,0,0,1,128,160Z"></path>
        </svg>
      </td>
    </tr>
  );
};

export default UserItem;
