import PatientDetails from "../components/patient/PatientDetails"

const Dashboard = () => {
  return (
    <div className='bg-gray mt-16 pb-12 flex flex-col items-center justify-center sm:mt-28'>
      <PatientDetails patientId={localStorage.getItem("id")}/>
    </div>

  )
}

export default Dashboard