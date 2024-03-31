import React, { useMemo, useState } from "react";
import Pagination from "../components/pagination/Pagination";
import PrescriptionRecordItem from "../components/extra/PrescriptionRecordItem";
import { useMediaQuery } from "react-responsive";
import LatestPrescription from "./LatestPrescription";

const Prescriptions = () => {
  // API call to /api/patient/${id}/prescription

  const dummy_prescriptions = [
    {
      prescribedById: "doctor_id_1",
      filledById: "pharmacist_id_1",
      prescribedForId: "patient_id_1",
      status: true,
      notes: "Take medicine with food",
      drugs: [
        { drug: "Aspirin", dosage: "10mg", quantity: 30 },
        { drug: "Paracetamol", dosage: "20mg", quantity: 20 },
      ],
      date: "2023-12-10",
    },
    {
      prescribedById: "doctor_id_2",
      filledById: "pharmacist_id_2",
      prescribedForId: "patient_id_2",
      status: false,
      notes: "Avoid driving after taking medication",
      drugs: [
        { drug: "Ibuprofen", dosage: "15mg", quantity: 25 },
        { drug: "Lipitor", dosage: "40mg", quantity: 10 },
      ],
      date: "2023-12-10",
    },
    {
      prescribedById: "doctor_id_1",
      filledById: "pharmacist_id_1",
      prescribedForId: "patient_id_1",
      status: true,
      notes: "Take medicine with food",
      drugs: [
        { drug: "Aspirin", dosage: "10mg", quantity: 30 },
        { drug: "Paracetamol", dosage: "20mg", quantity: 20 },
      ],
      date: "2023-12-10",
    },
    {
      prescribedById: "doctor_id_2",
      filledById: "pharmacist_id_2",
      prescribedForId: "patient_id_2",
      status: false,
      notes: "Avoid driving after taking medication",
      drugs: [
        { drug: "Ibuprofen", dosage: "15mg", quantity: 25 },
        { drug: "Lipitor", dosage: "40mg", quantity: 10 },
        { drug: "Lipitor", dosage: "40mg", quantity: 10 },
        { drug: "Lipitor", dosage: "40mg", quantity: 10 },
        { drug: "Lipitor", dosage: "40mg", quantity: 10 },
        { drug: "Lipitor", dosage: "40mg", quantity: 10 },
        { drug: "Lipitor", dosage: "40mg", quantity: 10 },
        { drug: "Lipitor", dosage: "40mg", quantity: 10 },
        { drug: "Lipitor", dosage: "40mg", quantity: 10 },
        { drug: "Lipitor", dosage: "40mg", quantity: 10 },
      ],
      date: "2023-12-10",
    },
    {
      prescribedById: "doctor_id_1",
      filledById: "pharmacist_id_1",
      prescribedForId: "patient_id_1",
      status: true,
      notes: "Take medicine with food",
      drugs: [
        { drug: "Aspirin", dosage: "10mg", quantity: 30 },
        { drug: "Paracetamol", dosage: "20mg", quantity: 20 },
      ],
      date: "2023-12-10",
    },
    {
      prescribedById: "doctor_id_2",
      filledById: "pharmacist_id_2",
      prescribedForId: "patient_id_2",
      status: false,
      notes: "Avoid driving after taking medication",
      drugs: [
        { drug: "Ibuprofen", dosage: "15mg", quantity: 25 },
        { drug: "Lipitor", dosage: "40mg", quantity: 10 },
      ],
      date: "2023-12-10",
    },
    // Add more dummy prescriptions as needed
  ];
  const latestPrescriptions = dummy_prescriptions.at(0);

  const isMobile = useMediaQuery({ maxWidth: 640 });
  const [currentPage, setCurrentPage] = useState(1);
  let pageSize = 5;
  isMobile ? (pageSize = 2) : (pageSize = 3);

  const currentPageData = useMemo(() => {
    const firstPageIndex = (currentPage - 1) * pageSize;
    const lastPageIndex = firstPageIndex + pageSize;
    return dummy_prescriptions.slice(firstPageIndex, lastPageIndex);
  }, [currentPage]);

  const [view, setView] = useState(false);

  const handleViewPrescriptions = () => setView(true);
  const handleClosePrescriptions = () => {
    setView(false);
  };
  return (
    <div className="bg-gray mt-20 pb-12 sm:mt-24 lg:mt-32 mx-4">
      <LatestPrescription 
        latestPrescriptions={latestPrescriptions}
        view={view}
        handleViewPrescriptions={handleViewPrescriptions}
        handleClosePrescriptions={handleClosePrescriptions}
        />
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
          {currentPageData.map((prescribe, idx) => (
            <PrescriptionRecordItem
              sn={(currentPage - 1) * pageSize + idx + 1}
              key={`${prescribe.prescribedForId} - ${prescribe.filledById}`}
              data={prescribe}
              view={view}
              handleViewPrescriptions={handleViewPrescriptions}
              handleClosePrescriptions={handleClosePrescriptions}
            />
          ))}
        </tbody>
      </table>
      <div className="flex justify-end mt-5 mr-5">
        <Pagination
          className={""}
          currentPage={currentPage}
          totalCount={dummy_prescriptions.length}
          pageSize={pageSize}
          onPageChange={(page) => setCurrentPage(page)}
        />
      </div>
    </div>
  );
};

export default Prescriptions;
