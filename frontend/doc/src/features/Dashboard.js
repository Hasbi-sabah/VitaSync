import CreateSearchPatient from '../components/extra/CreateSearchPatient';
import DisplayPatients from '../components/patient/DisplayPatients';
import { useGetPatientQuery } from './patient/patientApiSlice';

const Dashboard = () => {
  const patient1 = {'userId': '123', 'firstName': 'Bob', 'lastName': 'The Builder', 'sex': 'Male', 'birthDate': '26', 'phoneNumber': '(406) 555-0120'}
  const patient2 = {'userId': '103', 'firstName': 'Bob', 'lastName': 'The Builder', 'sex': 'Male', 'birthDate': '26', 'phoneNumber': '(406) 555-0120'}
  const patient3 = {'userId': '113', 'firstName': 'Bob', 'lastName': 'The Builder', 'sex': 'Male', 'birthDate': '26', 'phoneNumber': '(406) 555-0120'}
  const patient4 = {'userId': '13', 'firstName': 'Bob', 'lastName': 'The Builder', 'sex': 'Male', 'birthDate': '26', 'phoneNumber': '(406) 555-0120'}
  const patient5 = {'userId': '23', 'firstName': 'Bob', 'lastName': 'The Builder', 'sex': 'Male', 'birthDate': '26', 'phoneNumber': '(406) 555-0120'}
  const patient6 = {'userId': '3', 'firstName': 'Bob', 'lastName': 'The Builder Of The Great Wall', 'sex': 'Female', 'birthDate': '26', 'phoneNumber': '(406) 555-0120'}
  const patient7 = {'userId': '3', 'firstName': 'Bob', 'lastName': 'The Builder Of The Great Wall', 'sex': 'Female', 'birthDate': '26', 'phoneNumber': '(406) 555-0120'}
  const patient8 = {'userId': '3', 'firstName': 'Bob', 'lastName': 'The Builder Of The Great Wall', 'sex': 'Female', 'birthDate': '26', 'phoneNumber': '(406) 555-0120'}
  const patient9 = {'userId': '3', 'firstName': 'Bob', 'lastName': 'The Builder Of The Great Wall', 'sex': 'Female', 'birthDate': '26', 'phoneNumber': '(406) 555-0120'}
  const patient10 = {'userId': '3', 'firstName': 'Bob', 'lastName': 'The Builder Of The Great Wall', 'sex': 'Female', 'birthDate': '26', 'phoneNumber': '(406) 555-0120'}
  
  const data = [patient1, patient2, patient3, patient4, patient5, patient6, patient7, patient8, patient9, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient1, patient2, patient3, patient4, patient5, patient6, patient7, patient8, patient9, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10];

  const { data: patientList, isLoading, error } = useGetPatientQuery();
  if (isLoading) console.log("Loading");
  if (error) console.log(error);
  console.log(patientList);
  const label = "Today's Appointments"
  return (
    <div className='bg-gray pb-12 flex flex-col items-center justify-center'>
      <CreateSearchPatient />
      <DisplayPatients data={patientList} label={label}/>
    </div>
  )
}

export default Dashboard