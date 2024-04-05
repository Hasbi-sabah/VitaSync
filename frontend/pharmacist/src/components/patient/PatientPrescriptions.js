import React, { useEffect, useState } from 'react'
import { useGetPatientPrescriptionByIdQuery } from '../../features/prescription/prescriptionApiSlice'

/**
 * PatientPrescriptions component fetches and displays a list of prescriptions for a specific patient.
 * This component uses the useGetPatientPrescriptionByIdQuery custom hook to fetch prescriptions based on the patientId prop.
 * It also uses the useState and useEffect hooks to manage and update the prescription list state.
 * @param {Object} props - The props object.
 * @param {string} props.patientId - The ID of the patient for whom to fetch prescriptions.
 * @returns {JSX.Element} The rendered PatientPrescriptions component, displaying the list of prescriptions.
 */
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
