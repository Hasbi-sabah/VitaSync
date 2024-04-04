import { useState } from "react";
import CreateSearchPatient from "../components/extra/CreateSearchPatient"
import QrScan from "../components/QrScanner/QrScan";
import { LookUpPatient } from "../components/extra/Searchbox";

const Dashboard = () => {
  const [activeQrScanner, setActiveQrScanner] = useState(false)
  const [callSearch, setCallSearch] = useState('');
  return (
    <div className='bg-gray pb-12 flex flex-col items-center justify-center'>
      <CreateSearchPatient setActiveQrScanner={setActiveQrScanner} />
      {activeQrScanner && <QrScan setCallSearch={setCallSearch} setActiveQrScanner={setActiveQrScanner} />}
      {callSearch && <LookUpPatient searchQuery={callSearch} />}
    </div>
  )
}

export default Dashboard