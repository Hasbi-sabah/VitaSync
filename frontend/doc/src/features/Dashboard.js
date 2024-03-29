import React from 'react';
import { useEffect, useState } from 'react';
import CreateSearchPatient from '../components/extra/CreateSearchPatient';
import DisplayAppointments from '../components/patient/DisplayAppointments';
import { useGetHCWAppointmentByIdQuery } from './appointment/appointmentApiSlice';
import { useGetPatientQuery } from './patient/patientApiSlice';

const Dashboard = () => {
  const currentDate = new Date();
  currentDate.setHours(0, 1, 0, 0);
  const formattedDate = currentDate.toISOString().slice(0, 10);
  const dict = {start_time: formattedDate + ' 00:01 AM', end_time: formattedDate + ' 11:59 PM'}
  
  const [patients, setPatients] = useState([]);

  // Move the hook calls to the top level
  const { data: patientList } = useGetHCWAppointmentByIdQuery(
     sessionStorage.getItem("id"),
     dict
  );
  const ids = {
    ids: patientList ? patientList.map((patient) => patient.patientId) : []
   };
  const { data: patientsData } = useGetPatientQuery(ids);
 
  const GetPatient = async () => {
     try {
       if (patientList && patientsData) {
         setPatients(patientsData);
       }
     } catch (error) {
       console.error(error);
     }
  };
 
  useEffect(() => {
     GetPatient();
  }, [patientList, patientsData]);


  console.log(patientsData)  
  const label = "Today's Appointments";
  
  return (
    <div className='bg-gray pb-12 flex flex-col items-center justify-center'>
      <CreateSearchPatient />
      {patientsData && <DisplayAppointments data={patientsData} label={label}/>}
    </div>
  );
}

export default Dashboard;