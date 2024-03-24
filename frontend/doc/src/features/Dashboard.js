import CreateSearchPatient from '../components/extra/CreateSearchPatient'
import DisplayPatients from '../components/patient/DisplayPatients'

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

  const label = "Today's Appointments"
  return (
    <div className='bg-gray pb-12'>
      <CreateSearchPatient />
      <DisplayPatients data={data} label={label}/>
    </div>
  )
}

export default Dashboard