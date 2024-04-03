import { useState } from "react";
import CreateSearchPatient from "../components/extra/CreateSearchPatient"
import QrScan from "../components/QrScanner/QrScan";
import { LookUpPatient } from "../components/extra/Searchbox";

const Dashboard = () => {
  const [activeQrScanner, setActiveQrScanner] = useState(false)
  const [callSearch, setCallSearch] = useState('');
  return (
    <div className='bg-gray mt-16 pb-12 flex flex-col items-center justify-center sm:mt-28'>
      <CreateSearchPatient setActiveQrScanner={setActiveQrScanner} callSearch={callSearch}/>
      {activeQrScanner && <QrScan setCallSearch={setCallSearch} setActiveQrScanner={setActiveQrScanner} />}
      {callSearch && <LookUpPatient searchQuery={callSearch} />}
    </div>
  )
}

export default Dashboard