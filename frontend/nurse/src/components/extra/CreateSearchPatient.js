import { useState } from "react";
import CreateNewPatient from "../patient/CreateNewPatient";
import Searchbox from "./Searchbox";

const CreateSearchPatient = () => {
  const [showAddPatient, setShowAddPatient] = useState(false);
  const handleOnClick = () => {
    setShowAddPatient(true);
  };

  const closeOverlay = () => {
    setShowAddPatient(false);
  };
  return (
      <div className="mt-32 sm:mt-24 lg:mt-32 flex flex-col justify-center lg:flex-row items-center gap-5 sm:gap-8 sm:ml-56 lg:ml-64 lg:gap-52">
        {showAddPatient && <CreateNewPatient closeOverlay={closeOverlay} />}
        <button onClick={handleOnClick} className='uppercase bg-blue text-white h-16 w-72 rounded-[20px] relative font-semibold text-base hover:bg-lightBlue'>
          <span className="absolute top-3 left-5">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="#ffffff" viewBox="0 0 256 256"><path d="M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm0,192a88,88,0,1,1,88-88A88.1,88.1,0,0,1,128,216Zm48-88a8,8,0,0,1-8,8H136v32a8,8,0,0,1-16,0V136H88a8,8,0,0,1,0-16h32V88a8,8,0,0,1,16,0v32h32A8,8,0,0,1,176,128Z"></path></svg>
          </span>
          <span className="pl-8">Add new patient</span>
        </button>
        <Searchbox/>
      </div>
  )
}

export default CreateSearchPatient;
