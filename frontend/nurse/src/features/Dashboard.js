import CreateSearchPatient from '../components/extra/CreateSearchPatient'
import DisplayPatients from '../components/patient/DisplayPatients'
import { useSelector } from 'react-redux';
import { selectPinnedIds } from './auth/authSlice';
import { useGetSearchPatientQuery } from './patient/patientApiSlice';

const Dashboard = () => {
  const pinnedIds = useSelector(selectPinnedIds);
  console.log(pinnedIds)
  const { data: patientsData } = useGetSearchPatientQuery({ids: pinnedIds});
  console.log(patientsData)
  const label = "Pinned Profiles"
  return (
    <div className='bg-gray pb-12 flex flex-col items-center justify-center'>
      <CreateSearchPatient />
      {patientsData && <DisplayPatients data={patientsData} label={label}/>}
    </div>
  )
}

export default Dashboard