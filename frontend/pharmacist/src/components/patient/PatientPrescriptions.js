import React, { useEffect, useState } from 'react'
import { useGetPatientPrescriptionByIdQuery } from '../../features/prescription/prescriptionApiSlice'

const PatientPrescriptions = ({ patientId }) => {
    const {data: prescriptions} = useGetPatientPrescriptionByIdQuery(patientId)
    const [prescriptionList, setPrescriptionList] = useState({})

    useEffect(() => {
        if (prescriptions) {
          const prescriptionDetails = {
          }
            setPrescriptionList(prescriptions);
        }
      }, [prescriptions]);
  return (
    <div>{console.log(prescriptionList)}</div>
  )
}

export default PatientPrescriptions