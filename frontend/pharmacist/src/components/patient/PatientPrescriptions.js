import React, { useEffect, useState } from 'react'
import { useGetPatientPrescriptionByIdQuery } from '../../features/prescription/prescriptionApiSlice'

const PatientPrescriptions = ({ patientId }) => {
    const {data: prescriptions} = useGetPatientPrescriptionByIdQuery(patientId)
    const [prescriptionList, setPrescriptionList] = useState({})

    useEffect(() => {
        if (prescriptions) {
          const prescriptionDetails = {
          }
            setPrescriptionList();
        }
      }, [prescriptions]);
  return (
    <div>PatientPrescriptions</div>
  )
}

export default PatientPrescriptions