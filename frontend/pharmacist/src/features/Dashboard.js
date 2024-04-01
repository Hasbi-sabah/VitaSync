import { useState } from "react";
import CreateSearchPatient from "../components/extra/CreateSearchPatient"
import QrScan from "../components/QrScanner/QrScan";
import Searchbox, { LookUp } from "../components/extra/Searchbox";

const Dashboard = () => {
  const [activeQrScanner, setActiveQrScanner] = useState(false)
  const [callSearch, setCallSearch] = useState('');
  return (
    <div className='bg-gray mt-16 pb-12 flex flex-col items-center justify-center sm:mt-28'>
      <CreateSearchPatient setActiveQrScanner={setActiveQrScanner} />
      {activeQrScanner && <QrScan setCallSearch={setCallSearch} setActiveQrScanner={setActiveQrScanner} />}
      {callSearch && <LookUp searchQuery={callSearch} />}
    </div>
  )
}

export default Dashboard