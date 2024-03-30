import React, { useMemo, useState } from 'react'
import Pagination from '../components/pagination/Pagination';
import ViewPatientRecord from '../components/extra/ViewPatientRecord';
import RecordItem from '../components/extra/RecordItem';

const Records = () => {
  //API call to obtain records

  const date = new Date()
  const dummytRecords = [
    {
      id: 1,
      patient: "John Doe",
      date: "2023-09-20",
      diagnosis: "Hypertension",
      notes: "Blood pressure slightly elevated, advised to continue medication.",
      vitals: {
        bloodPressure: "130/80 mmHg",
        heartRate: "75 bpm",
        temperature: "98.6°F",
      },
      procedures: ["Blood pressure measurement"],
      prescriptions: [
        { drug: "Lisinopril", dosage: "10 mg daily" },
        { drug: "Aspirin", dosage: "81 mg daily" },
      ],
      assessedBy: "Dr. Smith",
      vaccines: [],
      followUp: date.toLocaleDateString(),
    },
    {
      id: 2,
      patient: "Jane Smith",
      date: "2023-10-15",
      diagnosis: "Normal",
      notes: "Overall health in good condition, advised to maintain healthy lifestyle.",
      vitals: {
        bloodPressure: "120/70 mmHg",
        heartRate: "60 bpm",
        temperature: "98.2°F",
      },
      procedures: ["Physical examination", "Blood test"],
      prescriptions: [],
      assessedBy: "Dr. Johnson",
      vaccines: [],
      followUp: date.toLocaleDateString(),
    },
    {
      id: 3,
      patient: "Alice Brown",
      date: "2023-11-05",
      diagnosis: "Influenza",
      notes: "Prescribed antiviral medication, advised bed rest.",
      vitals: {
        temperature: "101.5°F",
      },
      procedures: ["Physical examination"],
      prescriptions: [{ drug: "Oseltamivir", dosage: "75 mg twice daily" }],
      assessedBy: "Dr. Lee",
      vaccines: [],
      followUp: date.toLocaleDateString(),
    },
    {
      id: 4,
      patient: "Michael Johnson",
      date: "2023-12-10",
      diagnosis: "Muscle strain",
      notes: "Prescribed pain medication, advised to avoid heavy lifting.",
      procedures: ["Physical examination"],
      prescriptions: [{ drug: "Ibuprofen", dosage: "200 mg as needed" }],
      assessedBy: "Dr. Patel",
      vaccines: [],
      followUp: date.toLocaleDateString(),
    },
    {
      id: 5,
      patient: "Emily Davis",
      date: "2024-01-20",
      diagnosis: "Normal",
      notes: "No issues reported, scheduled next appointment in six months.",
      procedures: ["Physical examination"],
      prescriptions: [],
      assessedBy: "Dr. Garcia",
      vaccine: [],
      followUp: date.toLocaleDateString(),
    },
  ];
  

  const [currentPage, setCurrentPage] = useState(1);
  const pageSize = 5;

  const currentPageData = useMemo(() => {
    const firstPageIndex = (currentPage - 1) * pageSize;
    const lastPageIndex = firstPageIndex + pageSize;
    return dummytRecords.slice(firstPageIndex, lastPageIndex);
  }, [currentPage]);


  return (
  <div className="bg-gray mt-20 pb-12 sm:mt-24 lg:mt-32 mx-4">

    <table className='w-full text-lg bg-white table-auto'>
      <thead>
        <tr>
          <td colSpan={3} className='text-3xl py-4 font-semibold text-center bg-lightBlue text-white'>Medical History</td>
        </tr>
      </thead>
      <tbody className=''>
        {currentPageData.map((record, idx) => (
          <RecordItem 
            sn={(currentPage - 1) * pageSize + idx + 1}
            key={record.id}
            data={record}
          />
        ))}
      </tbody>
    </table>
    <div className='flex justify-end'>
      <Pagination
        className={""}
        currentPage={currentPage}
        totalCount={dummytRecords.length}
        pageSize={pageSize}
        onPageChange={(page) => setCurrentPage(page)}
      />
    </div>
  </div>
  )
}

export default Records
