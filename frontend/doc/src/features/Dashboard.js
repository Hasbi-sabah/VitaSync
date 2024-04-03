import React from 'react';
import { useEffect, useState } from 'react';
import CreateSearchPatient from '../components/extra/CreateSearchPatient';
import DisplayAppointments from '../components/patient/DisplayAppointments';
import { useGetHCWAppointmentByIdQuery } from './appointment/appointmentApiSlice';
import { useGetPatientQuery } from './patient/patientApiSlice';
import LoadingScreen from '../components/LoadingScreen';

const Dashboard = () => {
  const currentDate = new Date();
  currentDate.setHours(0, 1, 0, 0);
  const formattedDate = currentDate.toISOString().slice(0, 10);
  const start_end = {start_time: formattedDate + ' 12:01 AM', end_time: formattedDate + ' 11:59 PM'}

  // Move the hook calls to the top level
  const { data: patientList, isLoading: isPatientListLoading } = useGetHCWAppointmentByIdQuery([localStorage.getItem("id"), start_end]);
  const { data: patientsData, isLoading: isPatientsDataLoading } = useGetPatientQuery();
  const [patients, setPatients] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
 
  useEffect(() => {
     if (patientList && patientsData) {
       setPatients(patientsData);
       setIsLoading(false);
     }
  }, [patientList, patientsData]);
  
  if (isLoading) {
     return <LoadingScreen />
  }
  
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
  
  return null; // This will render nothing if there's no data and not loading
}

export default Dashboard;
