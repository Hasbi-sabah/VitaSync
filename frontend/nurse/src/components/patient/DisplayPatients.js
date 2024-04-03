import React, { useState, useMemo } from "react";
import Pagination from "../pagination/Pagination";
import UserItem from "./UserItem";
import { useMediaQuery } from "react-responsive";
import { useLocation } from "react-router-dom";

const DisplayPatients = ({ data, label }) => {
  const [currentPage, setCurrentPage] = useState(1);
  const pageSize = 10;
  const isMobile = useMediaQuery({ maxWidth: 1024 });

  const currentTableData = useMemo(() => {
    const firstPageIndex = (currentPage - 1) * pageSize;
    const lastpageIndex = firstPageIndex + pageSize;
    return data.slice(firstPageIndex, lastpageIndex);
  }, [currentPage]);

  const location = useLocation();
  const isDashboard = location.pathname === "/dashboard";
  if (currentTableData.length > 0) {
    return (
      <div className="lg:w-[80%] sm:w-[34rem] sm:rounded-[1.875rem] bg-white mt-9 mx-5 sm:ml-56 lg:mx-auto sm:px-10 pb-8">
        <h3 className="text-left text-2xl lg:text-xl font-semibold py-3 pl-2 sm:py-6">
          {label}
        </h3>
        <table className="min-w-full text-base">
          <thead className="h-12">
            <tr className="bg-darkBlue text-white">
              <th className="px-4 ">Name</th>
              <th className="px-3 lg:px-4">Sex</th>
              <th className="px-3 lg:px-4">Age</th>
              {!isMobile && <th className=" px-4">Contact</th>}
              <th className=""></th>
            </tr>
          </thead>
  
          <tbody>
            {currentTableData.map((user, idx) => (
              <UserItem
                key={idx}
                name={`${user.firstName} ${user.lastName}`}
                sex={user.sex === "male" ? "M" : user.sex === "female" ? "F" : "N/A"}
                dob={user.birthDate}
                contact={user.phoneNumber}
                date={user.date}
                time={"12:00"}
                patientId={user.id}
              />
            ))}
          </tbody>
        </table>
        <div className="flex justify-end">
          <Pagination
            className={"pagination-bar"}
            currentPage={currentPage}
            totalCount={data.length}
            pageSize={pageSize}
            onPageChange={(page) => setCurrentPage(page)}
          />
        </div>
      </div>
    );
  } else {
    return (
      <div className="lg:w-[80%] w-[90%] sm:w-[80%] sm:rounded-[1.875rem] bg-white mt-9 mx-5 sm:px-10 pb-2">
        <h3 className="text-center text-2xl lg:text-xl font-semibold py-3 pl-2 sm:py-6">
          No pinned patient!
        </h3>
      </div>
    )
  }
};

export default DisplayPatients;
