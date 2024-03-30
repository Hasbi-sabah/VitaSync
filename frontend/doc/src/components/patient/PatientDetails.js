import React, { useState, useEffect } from 'react';
import UpdateMedInfo from "../MedInfo/UpdateMedInfo";
import Vital from "./Vital";
import { useGetPatientByIdQuery } from '../../features/patient/patientApiSlice'
import { useGetPatientVitalByIdQuery } from '../../features/vital/vitalApiSlice'
import { useGetPatientMedInfoByIdQuery, useAddPatientMedInfoByIdMutation } from '../../features/medInfo/medInfoApiSlice';

const PatientDetails = ({ userId, closeOverlay }) => {
  const { data: patientInfo } = useGetPatientByIdQuery(userId);
  const { data: patientMedInfo } = useGetPatientMedInfoByIdQuery(userId);

  // Initialize state with an empty object to avoid undefined errors
  const [medDetails, setMedDetails] = useState({});

  useEffect(() => {
    if (patientInfo && patientMedInfo) {
      const reqPatientDetails = {
        medicalInfo: { allergies: patientMedInfo.allergies, conditions: patientMedInfo.conditions, notes: patientMedInfo.notes },
        firstName: patientInfo.firstName,
        lastName: patientInfo.lastName,
        phoneNumber: patientInfo.phoneNumber,
        sex: patientInfo.sex,
        age: patientInfo.birthDate,
      };
      setMedDetails(reqPatientDetails);
    }
  }, [patientInfo, patientMedInfo]);

  // const [addPatientMedInfoById] = useAddPatientMedInfoByIdMutation();

  // useEffect(() => {
  //   if (medDetails.medicalInfo) {
  //     addPatientMedInfoById({ variables: { userId, medInfo: medDetails.medicalInfo } });
  //   }
  // }, [medDetails, addPatientMedInfoById, userId]);
  const { medicalInfo, firstName, lastName, phoneNumber, sex, age } = medDetails;
  const { allergies, conditions, notes } = medicalInfo || {};
  const currentDate = new Date();

  const { data: reqVitals } = useGetPatientVitalByIdQuery(userId);

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
  if (medicalInfo && reqVitals){
    const fillDetails = {
      allergies: { attr: "Known Allergies", label: "allergies", value: allergies },
      conditions: { attr: "Conditions", label: "conditions", value: conditions },
      notes: { attr: "Note", label: "notes", value: notes },
    };
    const { created_at, temp, bp, bpm, weight, height, glucose, note } = reqVitals.length > 0 ? reqVitals[0] : {};
    return (
      <div className="w-screen sm:w-[100%] lg:w-[60rem]">
        <div className="flex flex-col lg:flex-row gap-11">
          <div className="bg-white rounded-3xl relative mx-0 sm:mx-2 sm:w-[26rem] p-3 sm:p-5">
            <div className="">
              <h2 className="text-3xl font-semibold text-center">
                {firstName ? firstName : ""} {lastName ? lastName : ""}
              </h2>
              <div className="flex justify-between text-sm">
                <span>{sex}</span>
                <span>Age {age ? age : ""}</span>
              </div>
              <div className="mt-2 mb-2">
                <p className="text-lightBlue text-left text-sm">
                  {phoneNumber ? phoneNumber : ""}
                </p>
              </div>
            </div>
            <div className="relative w-[23rem] text-left pt-3">
              <UpdateMedInfo
                edit={editAllergies}
                setFunction={setEditAllergies}
                medInfo={fillDetails.allergies}
                userId={userId}
              />
              {editButton("allergies")}
            </div>
            <div className="relative w-[23rem] text-left pt-3">
              <UpdateMedInfo
                edit={editConditions}
                setFunction={setEditConditions}
                medInfo={fillDetails.conditions}
                userId={userId}
              />
              {editButton("conditions")}
            </div>
            <div className="relative w-[23rem] text-left pt-3">
              <UpdateMedInfo
                edit={editNote}
                setFunction={setEditNote}
                medInfo={fillDetails.notes}
                userId={userId}
              />
              {editButton("note")}
            </div>
          </div>
          <div className="bg-white rounded-3xl mx-auto relative lg:w-[43rem] lg:h-[20rem] p-5">
            <p className="text-2xl font-meduim text-left">Lastest Vitals</p>
            <div className="grid gap-4 grid-cols-2 lg:grid-cols-3 mt-5 text-left">
              {/* API call to get the vitals */}
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
            </div>
          </div>
        </div>
      </div>
    );
  }
};

export default PatientDetails;
