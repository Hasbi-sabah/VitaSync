
// API call /patient
const PatientMan = () => {
  const currentDate = new Date();
  const date = currentDate.getDate();
  const month = currentDate.getMonth();
  const year = currentDate.getFullYear();

  const day = "" + date + "/"  + month +  "/" + year;
  const patient1 = {'userId': '123', 'firstName': 'Bob', 'lastName': 'The Builder', 'sex': 'Male', 'birthDate': '26', 'phoneNumber': '(406) 555-0120', 'date': day}
  const patient2 = {'userId': '103', 'firstName': 'Bob', 'lastName': 'The Builder', 'sex': 'Male', 'birthDate': '26', 'phoneNumber': '(406) 555-0120', 'date': day}
  const patient3 = {'userId': '113', 'firstName': 'Bob', 'lastName': 'The Builder', 'sex': 'Male', 'birthDate': '26', 'phoneNumber': '(406) 555-0120', 'date': day}
  const patient4 = {'userId': '13', 'firstName': 'Bob', 'lastName': 'The Builder', 'sex': 'Male', 'birthDate': '26', 'phoneNumber': '(406) 555-0120', 'date': day}
  const patient5 = {'userId': '23', 'firstName': 'Bob', 'lastName': 'The Builder', 'sex': 'Male', 'birthDate': '26', 'phoneNumber': '(406) 555-0120', 'date': day}
  const patient6 = {'userId': '3', 'firstName': 'Bob', 'lastName': 'The Builder Of The Great Wall', 'sex': 'Female', 'birthDate': '26', 'phoneNumber': '(406) 555-0120', 'date': day}
  const patient7 = {'userId': '3', 'firstName': 'Bob', 'lastName': 'The Builder Of The Great Wall', 'sex': 'Female', 'birthDate': '26', 'phoneNumber': '(406) 555-0120', 'date': day}
  const patient8 = {'userId': '3', 'firstName': 'Bob', 'lastName': 'The Builder Of The Great Wall', 'sex': 'Female', 'birthDate': '26', 'phoneNumber': '(406) 555-0120', 'date': day}
  const patient9 = {'userId': '3', 'firstName': 'Bob', 'lastName': 'The Builder Of The Great Wall', 'sex': 'Female', 'birthDate': '26', 'phoneNumber': '(406) 555-0120', 'date': day}
  const patient10 = {'userId': '3', 'firstName': 'Bob', 'lastName': 'The Builder Of The Great Wall', 'sex': 'Female', 'birthDate': '26', 'phoneNumber': '(406) 555-0120', 'date': day}
  
  const data = [patient1, patient2, patient3, patient4, patient5, patient6, patient7, patient8, patient9, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient1, patient2, patient3, patient4, patient5, patient6, patient7, patient8, patient9, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10, patient10];

  const label = "Patients"
  return (
    <div className='bg-gray pb-12'>
    </div>
  )
}

export default PatientMan;