import React from 'react'

const RecordItem = ({ sn, date, diagnosis }) => {
    const bgColor = sn % 2 === 1 ? "bg-grey" : "";
  return (
    <div>
        <tr key={record.id} className='border-b-2 border-b-gray'>
            <td className='text-center'>{record.date}</td>
            <div className='flex flex-col items-center'>
              <div className='h-10 border-l rounded-full border-lightBlue text-center'></div>
              <div className='w-3 h-3 rounded-full bg-lightBlue border border-lightBlue'></div>
              <div className='h-10 border-l rounded-full border-lightBlue '></div>
            </div>
            <td className='text-left pl-3'>
              <h3 className='text-xl font-medium'>Doctor: {record.assessedBy}</h3>
              <p>Diagnosis: {record.diagnosis}</p>
              <span className='text-sm' onClick={handleViewRecord}>View</span>
              {view && <ViewPatientRecord data={dummytRecords} handleCloseRecord={handleCloseRecord} />}
            </td>
          </tr>
    </div>
  )
}

export default RecordItem