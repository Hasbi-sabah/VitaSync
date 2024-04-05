import { useState } from "react";
import CreateSearchPatient from "../components/extra/CreateSearchPatient"
import QrScan from "../components/QrScanner/QrScan";
import { LookUpPatient } from "../components/extra/Searchbox";

/**
 * Dashboard component that renders the main dashboard of the application.
 * It includes a search patient component, a QR scanner component, and a patient lookup component.
 * The QR scanner and patient lookup components are conditionally rendered based on the state.
 */
const Dashboard = () => {
 const [activeQrScanner, setActiveQrScanner] = useState(false)
 const [callSearch, setCallSearch] = useState('');
 return (
    <div className='bg-gray pb-12 flex flex-col items-center justify-center'>
      <CreateSearchPatient setActiveQrScanner={setActiveQrScanner} callSearch={callSearch}/>
      {activeQrScanner && <QrScan setCallSearch={setCallSearch} setActiveQrScanner={setActiveQrScanner} />}
      {callSearch && <LookUpPatient searchQuery={callSearch} />}
    </div>
 )
}

export default Dashboard;
