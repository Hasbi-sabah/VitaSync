import React, { useMemo, useState, useEffect } from "react";
import Pagination from "../components/pagination/Pagination";
import { useGetPatientRecordByIdQuery } from "./record/recordApiSlice";
import { useGetPatientVitalByIdQuery } from "./vital/vitalApiSlice";
import { useGetPatientProcedureByIdQuery } from "./procedure/procedureApiSlice";
import RecordItem from "../components/extra/RecordItem";
import LoadingScreen from "../components/LoadingScreen";

const Records = () => {
  const { data: records, isLoading: isRecordsLoading } =
    useGetPatientRecordByIdQuery(localStorage.getItem('id'));
  const { data: vitals, isLoading: isVitalsLoading } =
    useGetPatientVitalByIdQuery(localStorage.getItem('id'));

  const [isLoading, setIsLoading] = useState(true); // Initialize isLoading to true
  const [recAndVit, setRecAndVit] = useState([]); // Manage recAndVit as state


  const { data: procedures, isLoading: isProceduresLoading } =
  useGetPatientProcedureByIdQuery(localStorage.getItem('id'));
  useEffect(() => {
    if (!isRecordsLoading && !isVitalsLoading && !isProceduresLoading) {
      setIsLoading(false);
      // TODO: replace procedureId with actual procedure data
      const updatedRecords = records.map(record => {
        if (record.procedureId) {
          const procedureData = procedures.find(procedure => procedure?.id === record.procedureId);
          return { ...record, ...procedureData };
        }
        return record;
      });
      console.log(updatedRecords)
      if (updatedRecords && vitals) {
        const combinedData = updatedRecords.concat(vitals).sort((a, b) => {
          const dateA = new Date(a.created_at.replace(' at ', ' '));
          const dateB = new Date(b.created_at.replace(' at ', ' '));
          return dateA - dateB;
        });
        combinedData.reverse();
        setRecAndVit(combinedData); 
      }
    }
  }, [isRecordsLoading, isVitalsLoading, isProceduresLoading, vitals, records, procedures]);
  const [currentPage, setCurrentPage] = useState(1);
  const pageSize = 5;

  const currentPageData = useMemo(() => {
    console.log(recAndVit)
    const firstPageIndex = (currentPage - 1) * pageSize;
    const lastPageIndex = firstPageIndex + pageSize;
    return recAndVit.slice(firstPageIndex, lastPageIndex);
  }, [currentPage, recAndVit]);
  if (isLoading) {
    return <LoadingScreen />; // Display LoadingScreen while isLoading is true
  }
  if (currentPageData.length > 0) {
    return (
      <div className="bg-gray mt-20 pb-12 sm:mt-12 lg:mt-12 mx-4">
        <table className="w-full text-lg bg-white table-auto">
          <thead>
            <tr>
              <td
                colSpan={3}
                className="text-3xl py-4 font-semibold text-center bg-lightBlue text-white"
              >
                Medical History
              </td>
            </tr>
          </thead>
          <tbody className="">
            {currentPageData.map((record, idx) => (
              <RecordItem
                sn={(currentPage - 1) * pageSize + idx + 1}
                key={record.id}
                data={record}
              />
            ))}
          </tbody>
        </table>
        <div className="flex justify-end">
          <Pagination
            className={""}
            currentPage={currentPage}
            totalCount={recAndVit.length}
            pageSize={pageSize}
            onPageChange={(page) => setCurrentPage(page)}
          />
        </div>
      </div>
    );
  } else {
    return (
      <div className="lg:w-[97%] w-[90%] sm:w-[80%] sm:rounded-[1.875rem] bg-white mt-9 mx-5 sm:px-10 pb-2">
        <h3 className="text-center text-2xl lg:text-xl font-semibold py-3 pl-2 sm:py-6">
          No records available!
        </h3>
      </div>
    );
  }
};

export default Records;
