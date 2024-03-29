import React from 'react';
import CreateSearchPatient from '../components/extra/CreateSearchPatient';
import DisplayPatients from '../components/patient/DisplayPatients';
import { useGetPatientQuery } from './patient/patientApiSlice';

const Dashboard = () => {
  const { data: patientList, isLoading, error } = useGetPatientQuery();

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  const label = "Today's Appointments";
  
  return (
    <div className='bg-gray pb-12 flex flex-col items-center justify-center'>
      <CreateSearchPatient />
      {patientList && <DisplayPatients data={patientList} label={label}/>}
    </div>
  );
}

export default Dashboard;