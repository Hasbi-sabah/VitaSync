import PatientDetails from "../components/patient/PatientDetails"

const Dashboard = () => {
  return (
    <div className='bg-gray mt-16 pb-12 flex flex-col items-center justify-center sm:ml-60 sm:mt-28 lg:ml-40 lg:mt-32'>
      <PatientDetails />
    </div>

  )
}

export default Dashboard