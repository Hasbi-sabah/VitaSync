import React, { useState, useEffect } from 'react';
import UpdateMedInfo from "../MedInfo/UpdateMedInfo";
import Vital from "./Vital";
import { useGetPatientByIdQuery } from '../../features/patient/patientApiSlice'
import { useGetPatientVitalByIdQuery } from '../../features/vital/vitalApiSlice'
import { useGetPatientMedInfoByIdQuery, useAddPatientMedInfoByIdMutation } from '../../features/medInfo/medInfoApiSlice';
import RecordVitals from "./RecordVitals";
import LoadingScreen from '../../components/LoadingScreen';
import { useMediaQuery } from 'react-responsive';

/**
 * PatientDetails Component
 * @param userId - The ID of the patient.
 * @param closeOverlay - Function to close the overlay.
 * @returns PatientDetails component.
 */
const PatientDetails = ({ userId, closeOverlay }) => {
  // Fetch patient details
  const { data: patientInfo, isLoading: isPatientInfoLoading } = useGetPatientByIdQuery(userId);
  const { data: patientMedInfo, isLoading: isPatientMedInfoLoading } = useGetPatientMedInfoByIdQuery(userId);
  const { data: reqVitals, isLoading: isVitalsLoading } = useGetPatientVitalByIdQuery(userId);

  // Check if screen size is mobile
   const isMobile = useMediaQuery({ maxWidth: 400 });

  // Initialize state with an empty object to avoid undefined errors
  const [medDetails, setMedDetails] = useState({});

  const [isLoading, setIsLoading] = useState(true); // Initialize isLoading to true

  // Calculate age based on birth date
  useEffect(() => {
    if (patientInfo && patientMedInfo) {
      const calculateAge = (dob) => {
        const birthDate = new Date(dob);
        const currentDate = new Date();
        let age = currentDate.getFullYear() - birthDate.getFullYear();
        const monthDifference = currentDate.getMonth() - birthDate.getMonth();
        if (monthDifference < 0 || (monthDifference === 0 && currentDate.getDate() < birthDate.getDate())) {
          age--;
        }
        return age;
      };
      const reqPatientDetails = {
        medicalInfo: { allergies: patientMedInfo.allergies, conditions: patientMedInfo.conditions, notes: patientMedInfo.notes },
        firstName: patientInfo.firstName,
        lastName: patientInfo.lastName,
        phoneNumber: patientInfo.phoneNumber,
        sex: patientInfo.sex,
        age: calculateAge(patientInfo.birthDate),
      };
      setMedDetails(reqPatientDetails);
    }
  }, [patientInfo, patientMedInfo]);

  // Set loading state when data is fetched
  useEffect(() => {
    if (!isPatientInfoLoading || !isPatientMedInfoLoading || !isVitalsLoading) {
      setIsLoading(false)
    }}, [isPatientInfoLoading, isPatientMedInfoLoading, isVitalsLoading]);

  // Destructure medical details
  const { medicalInfo, firstName, lastName, phoneNumber, sex, age } = medDetails;
  const { allergies, conditions, notes } = medicalInfo || {};
  const currentDate = new Date();

  const [editAllergies, setEditAllergies] = useState(false);
  const [editConditions, setEditConditions] = useState(false);
  const [editNote, setEditNote] = useState(false);
  const handleEdit = (key) => {
    if (key === "allergies") setEditAllergies(true);
    else if (key === "conditions") setEditConditions(true);
    else if (key === "note") setEditNote(true);
  };

  const editButton = (type) => (
    <svg
    className="absolute top-3 right-0 hover:cursor-pointer"
    onClick={() => handleEdit(type)}
    xmlns="http://www.w3.org/2000/svg"
    width="24"
    height="20"
    fill="#000000"
    viewBox="0 0 256 256"
  >
    <path d="M227.31,73.37,182.63,28.68a16,16,0,0,0-22.63,0L36.69,152A15.86,15.86,0,0,0,32,163.31V208a16,16,0,0,0,16,16H92.69A15.86,15.86,0,0,0,104,219.31L227.31,96a16,16,0,0,0,0-22.63ZM51.31,160l90.35-90.35,16.68,16.69L68,176.68ZM48,179.31,76.69,208H48Zm48,25.38L79.31,188l90.35-90.35h0l16.68,16.69Z"></path>
  </svg>
  );
  const [addVitals, setAddVitals] = useState(false)

  const handleAddVital = () => {
    setAddVitals(true);
  };

  const closeVitalsOverlay = () => {
    setAddVitals(false);
  }
  if (isLoading) {
    return <LoadingScreen />;
  }
  if (medicalInfo && reqVitals){
    const fillDetails = {
      allergies: { attr: "Known Allergies", label: "allergies", value: allergies },
      conditions: { attr: "Conditions", label: "conditions", value: conditions },
      notes: { attr: "Note", label: "notes", value: notes },
    };
    const sortedVitals = reqVitals.slice().sort((a, b) => {
      const dateA = new Date(a.created_at.replace(' at ', ' '));
      const dateB = new Date(b.created_at.replace(' at ', ' '));
      return dateB - dateA;
    });
    console.log(sortedVitals)
    const { created_at, temp, bp, bpm, weight, height, glucose, note } = sortedVitals.length > 0 ? sortedVitals[0] : {};

    // Render patient details
    return (
      <div className="w-full">
        <div className="flex flex-col justify-center flex-wrap items-center lg:flex-row gap-11 w-full">
          <div className="bg-white rounded-3xl relative w-[90%] sm:w-[26rem] mx-0 sm:mx-2 p-3 sm:p-5">
            <div className="">
              <h2 className="text-3xl pb-5 font-semibold text-center">
                {firstName ? firstName : ""} {lastName ? lastName : ""}
              </h2>
              <div className="flex justify-around text-sm">
                <span>Sex: {sex}</span>
                <span>Age: {age ? age : "N/Y"}</span>
              </div>
              <div className="mt-2 mb-2">
                <p className="text-lightBlue text-center text-sm">
                  {phoneNumber ? phoneNumber : ""}
                </p>
              </div>
            </div>
            <div className="relative w-full sm:w-[23rem] text-left pt-3">
              <UpdateMedInfo
                edit={editAllergies}
                setFunction={setEditAllergies}
                medInfo={fillDetails.allergies}
                userId={userId}
              />
              {editButton("allergies")}
            </div>
            <div className="relative w-full sm:w-[23rem] text-left pt-3">
              <UpdateMedInfo
                edit={editConditions}
                setFunction={setEditConditions}
                medInfo={fillDetails.conditions}
                userId={userId}
              />
              {editButton("conditions")}
            </div>
            <div className="relative w-full sm:w-[23rem] text-left pt-3">
              <UpdateMedInfo
                edit={editNote}
                setFunction={setEditNote}
                medInfo={fillDetails.notes}
                userId={userId}
              />
              {editButton("note")}
            </div>
          </div>
          <div className="bg-white rounded-3xl w-full min-h-10 mx-auto relative lg:w-[43rem] p-5">
            <p className="text-2xl font-meduim text-left">Latest Vitals</p>
            <div className="grid gap-4 grid-cols-2 lg:grid-cols-3 mt-5 text-left">
              {/* API call to get the vitals */}
              {created_at ? (
              <>
              <Vital
                Vitalreading={temp + " °C"}
                vitalName={"Temperature"}
                currentDate={created_at}
              ></Vital>
              <Vital
                Vitalreading={bp + " mm hg"}
                vitalName={"Blood Pressure"}
                currentDate={created_at}
              ></Vital>
              <Vital
                Vitalreading={bpm + " bpm"}
                vitalName={"Hearth rate"}
                currentDate={created_at}
              ></Vital>
              <Vital
                Vitalreading={weight + " kg"}
                vitalName={"Weight"}
                currentDate={created_at}
              ></Vital>
              <Vital
                Vitalreading={height + " cm"}
                vitalName={"Height"}
                currentDate={created_at}
              ></Vital>
              <Vital
                Vitalreading={glucose + " mg/dL"}
                vitalName={"Blood Glucose"}
                currentDate={created_at}
              ></Vital>
              </>):("No available vitals!")}
              {addVitals && <RecordVitals closeOverlay={closeVitalsOverlay} patientId={userId}/>}
              <div
                className="absolute top-3 right-7 bg-lightBlue2 cursor-pointer hover:bg-lightBlue h-10 p-3 flex items-center mr-2"
                onClick={() => handleAddVital()}
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="32"
                    height="32"
                    fill="#ffffff"
                    viewBox="0 0 256 256"
                  >
                    <path d="M228,128a12,12,0,0,1-12,12H140v76a12,12,0,0,1-24,0V140H40a12,12,0,0,1,0-24h76V40a12,12,0,0,1,24,0v76h76A12,12,0,0,1,228,128Z"></path>
                  </svg>
                  {!isMobile && <p className="text-white text-lg pl-2">Record Vitals</p>}
                </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
};

export default PatientDetails;
