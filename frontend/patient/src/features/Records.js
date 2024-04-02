import React, { useMemo, useState } from 'react'
import Pagination from '../components/pagination/Pagination';
import ViewPatientRecord from '../components/extra/ViewPatientRecord';
import { useGetPatientRecordByIdQuery } from "./record/recordApiSlice"
import { useGetPatientVitalByIdQuery } from "./vital/vitalApiSlice"
import RecordItem from '../components/extra/RecordItem';

const Records = () => {
  //API call to obtain records
  const { data: records } = useGetPatientRecordByIdQuery(localStorage.getItem('id'))
  const { data: vitals } = useGetPatientVitalByIdQuery(localStorage.getItem('id'))

  let recAndVit = []
  if (records && vitals) {
    recAndVit = records.concat(vitals).sort((a, b) => {
      const A = a.created_at.replace(' at ', 'T').replace(' AM', '').replace(' PM', '');
      const B = b.created_at.replace(' at ', 'T').replace(' AM', '').replace(' PM', '');
      const dateA = new Date(`${A}:00`);
      const dateB = new Date(`${B}:00`);
      return dateA - dateB;
     });    
  }

  const date = new Date()

  const [currentPage, setCurrentPage] = useState(1);
  const pageSize = 5;
  console.log(recAndVit)

  const currentPageData = useMemo(() => {
    const firstPageIndex = (currentPage - 1) * pageSize;
    const lastPageIndex = firstPageIndex + pageSize;
    return recAndVit.slice(firstPageIndex, lastPageIndex);
  }, [currentPage]);


  if (recAndVit) {
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
        totalCount={recAndVit.length}
        pageSize={pageSize}
        onPageChange={(page) => setCurrentPage(page)}
      />
    </div>
  </div>
  )
}
}

export default Records
