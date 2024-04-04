import React, { useMemo, useState, useEffect, useCallback } from "react";
import Pagination from "../components/pagination/Pagination";
import PrescriptionRecordItem from "../components/extra/PrescriptionRecordItem";
import { useMediaQuery } from "react-responsive";
import LatestPrescription from "./LatestPrescription";
import { useGetPatientPrescriptionExtendedByIdQuery } from './prescription/prescriptionApiSlice';
import LoadingScreen from "../components/LoadingScreen"



const Prescriptions = () => {
  // API call to /api/patient/${id}/prescription
  const { data: prescriptions, isLoading } = useGetPatientPrescriptionExtendedByIdQuery(localStorage.getItem('id'));
  
  const isMobile = useMediaQuery({ maxWidth: 640 });
  const [currentPage, setCurrentPage] = useState(1);
  const [pageSize, setPageSize] = useState(isMobile ? 2 : 3);

  useEffect(() => {
    setPageSize(isMobile ? 2 : 3);
  }, [isMobile]);

  // console.log("Base: ", prescriptions)
    // FOCUS
  const latestPrescription = useMemo(() => {
    if (!prescriptions) return null;
    const sortedPrescriptions = prescriptions
       .filter(prescription => prescription.status === false)
       .sort((a, b) => new Date(b.created_at.replace(' at ', ' ')) - new Date(a.created_at.replace(' at ', ' ')));
    console.log("Got here???")
    return sortedPrescriptions.length > 0 ? sortedPrescriptions[0] : null;
  }, [prescriptions]);
  const currentPageData = useMemo(() => {
    if (!prescriptions) return [];
    const p = prescriptions
    ? prescriptions
         .filter(prescription => prescription.status === false)
         .sort((a, b) => new Date(b.created_at.replace(' at ', ' ')) - new Date(a.created_at.replace(' at ', ' '))) : null
    if (p && p.length > 0) {
      p.shift();
    }
    const firstPageIndex = (currentPage - 1) * pageSize;
    const lastPageIndex = firstPageIndex + pageSize;
    return p.slice(firstPageIndex, lastPageIndex);
 }, [currentPage, prescriptions, pageSize]);


  if (isLoading) {
    return <LoadingScreen />; 
 }
// console.log('CurrentPage', currentPageData)
// console.log('n', latestPrescription)
  return (
    <div className="bg-gray mt-20 pb-12 sm:mt-24 lg:mt-32 mx-4">
      {console.log("Lastest", latestPrescription)}
      {latestPrescription ? <LatestPrescription 
        latestPrescription={latestPrescription}
        /> : ""}
      <table className="w-full text-lg bg-white table-auto">
        <thead>
          <tr>
            <td
              colSpan={3}
              className="text-2xl py-4 font-semibold text-center bg-lightBlue text-white"
            >
              Prescription History
            </td>
          </tr>
        </thead>
        <tbody className="">
          {/* {console.log("H", currentPageData)} */}
          {currentPageData.map((prescribe, idx) => (
            <PrescriptionRecordItem
              sn={(currentPage - 1) * pageSize + idx + 1}
              key={prescribe.id}
              data={prescribe}
            />
          ))}
        </tbody>
      </table>
      <div className="flex justify-end mt-5 mr-5">
        <Pagination
          className={""}
          currentPage={currentPage}
          totalCount={prescriptions?.length || 0}
          pageSize={pageSize}
          onPageChange={(page) => setCurrentPage(page)}
        />
      </div>
    </div>
  );
};

export default Prescriptions;
