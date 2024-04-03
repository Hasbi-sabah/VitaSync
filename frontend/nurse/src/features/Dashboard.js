import { useState } from "react";
import CreateSearchPatient from '../components/extra/CreateSearchPatient'
import DisplayPatients from '../components/patient/DisplayPatients'
import { useSelector } from 'react-redux';
import { selectPinnedIds } from './auth/authSlice';
import { useGetSearchPatientQuery } from './patient/patientApiSlice';
import LoadingScreen from '../components/LoadingScreen';
import QrScan from "../components/QrScanner/QrScan";
import { LookUpPatient } from "../components/extra/Searchbox";

const Dashboard = () => {
  const pinnedIds = useSelector(selectPinnedIds);
  console.log(pinnedIds)
  const { data: patientsData, isLoading } = useGetSearchPatientQuery({ids: pinnedIds});
  console.log(patientsData)
  const label = "Pinned Profiles"
  const [activeQrScanner, setActiveQrScanner] = useState(false)  
  const [callSearch, setCallSearch] = useState('');

  if (isLoading) {
    return <LoadingScreen />
 }
  return (
    <div className='bg-gray pb-12 flex flex-col items-center justify-center'>
      <CreateSearchPatient setActiveQrScanner={setActiveQrScanner}/>
      {activeQrScanner && <QrScan setCallSearch={setCallSearch} setActiveQrScanner={setActiveQrScanner} />}
      {patientsData && <DisplayPatients data={patientsData} label={label}/>}
      {callSearch && <LookUpPatient searchQuery={callSearch} />}
    </div>
  )
}

export default Dashboard