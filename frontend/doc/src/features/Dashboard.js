import React from 'react';
import { useEffect, useState } from 'react';
import CreateSearchPatient from '../components/extra/CreateSearchPatient';
import DisplayAppointments from '../components/patient/DisplayAppointments';
import { useGetHCWAppointmentByIdQuery } from './appointment/appointmentApiSlice';
import { useGetSearchPatientQuery } from './patient/patientApiSlice';

const Dashboard = () => {
  const currentDate = new Date();
  currentDate.setHours(0, 1, 0, 0);
  const formattedDate = currentDate.toISOString().slice(0, 10);
  const start_end = {start_time: formattedDate + ' 12:01 AM', end_time: formattedDate + ' 11:59 PM'}

  const { data: patientList } = useGetHCWAppointmentByIdQuery([localStorage.getItem("id"), start_end]);
  const ids = {
    ids: patientList ? patientList.map((patient) => patient.patientId) : []
   };
  const { data: patientsData } = useGetSearchPatientQuery(ids);
  const [patients, setPatients] = useState([]);
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
  
  if (patientsData && patientList) {
    const mergedArray = patientList.map(obj1 => {
      const matchedObj = patientsData.find(obj2 => obj1.patientId === obj2.id);
      return { ...obj1, ...matchedObj };
    });
    
    const label = "Today's Appointments";
  
    return (
      <div className='bg-gray pb-12 flex flex-col items-center justify-center'>
        <CreateSearchPatient />
        {mergedArray && <DisplayAppointments data={mergedArray} label={label}/>}
      </div>
    );
  }
}

export default Dashboard;