import { useState } from "react";
import CreateSearchPatient from "../components/extra/CreateSearchPatient"
import QrScan from "../components/QrScanner/QrScan";

const Dashboard = () => {
  const [activeQrScanner, setActiveQrScanner] = useState(false)
  return (
    <div className='bg-gray mt-16 pb-12 flex flex-col items-center justify-center sm:mt-28'>
      <CreateSearchPatient setActiveQrScanner={setActiveQrScanner} />
      {activeQrScanner && <QrScan />}
    </div>
  )
}

export default Dashboard