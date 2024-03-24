import React, { useState, useEffect } from "react";
import UpdateMedInfo from "../MedInfo/UpdateMedInfo";
import Vital from "./Vital";

const PatientDetails = ({ userId, closeOverlay }) => {
  // API call to /patient/id ASK SABAH TO INCLUDE EMAIL
  const currentDate = new Date();
  const reqPatientDetails = {
    medicalInfo: { allergies: "Peanut", conditions: "", note: "" },
    firstName: "Williams",
    lastName: "AKANNI",
    phoneNumber: "123456789",
    sex: "Male",
    age: "24",
    email: "test@example.com",
  };
  const [medDetails, setMedDetails] = useState(reqPatientDetails);
  let medInfo = reqPatientDetails.medicalInfo; // will return {}
  const firstName = reqPatientDetails.firstName;
  const lastName = reqPatientDetails.lastName;
  const phoneNumber = reqPatientDetails.phoneNumber;
  const sex = reqPatientDetails.sex;
  const age = reqPatientDetails.birthDate; //Calculate age
  const email = reqPatientDetails.email; //TABLE NEEDS TO BE UPDATED
  let known_allergies = medInfo.allergies;
  let conditions = medInfo.conditions; //DB condition spelling
  let note = medInfo.note;
  useEffect(() => {
    // POST /patient/id update medicalInfo
  }, [medDetails]);

  // API call for vitals
  const reqVitals = {}; //status, temp, bp, bpm, weight, height, glucose, notes
  const { status, temp, bp, bpm, weight, height, glucose, notes } = reqVitals;

  const fillDetails = {
    allergies: { label: "Known Allergies", value: known_allergies },
    conditions: { label: "Conditions", value: conditions },
    note: { label: "Note", value: note },
  };

  const [editAllergies, setEditAllergies] = useState(false);
  const [editConditions, setEditConditions] = useState(false);
  const [editNote, setEditNote] = useState(false);
  const handleEdit = (key) => {
    console.log(key);
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
  return (
    <div className="w-screen sm:w-[60rem]">
      <div className="flex flex-col sm:flex-row gap-11">
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
              <p className="text-lightBlue text-left text-sm">{email ? email : ""}</p>
            </div>
          </div>
          <div className="h-9 w-[23rem] rounded-xl bg-gray flex justify-between items-center px-2 text-sm">
            <span>Last vistied</span>
            <span>{/*Get last visit date*/}03/10/24</span>
            <span>{/*Get last visit time*/}11:20am</span>
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
              medInfo={fillDetails.note}
              userId={userId}
            />
            {editButton("note")}
          </div>
        </div>
        <div className="bg-white rounded-3xl relative sm:w-[43rem] sm:h-[20rem] p-5">
          <p className="text-2xl font-meduim text-left">Lastest Vitals</p>
          <div className="grid gap-4 grid-cols-2 sm:grid-cols-3 mt-5 text-left">
            {/* API call to get the vitals */}
            <Vital
              Vitalreading={"90 °F"}
              vitalName={"Temperature"}
              currentDate={"Today"}
            ></Vital>
            <Vital
              Vitalreading={"120/80 mm hg"}
              vitalName={"Blood Pressure"}
              currentDate={"Today"}
            ></Vital>
            <Vital
              Vitalreading={"70 bpm"}
              vitalName={"Hearth rate"}
              currentDate={"Today"}
            ></Vital>
            <Vital
              Vitalreading={"70 kg"}
              vitalName={"Weight"}
              currentDate={"10/28/12"}
            ></Vital>
            <Vital
              Vitalreading={"173 cm"}
              vitalName={"Height"}
              currentDate={"3/4/16"}
            ></Vital>
            <Vital
              Vitalreading={"80 mg/dL"}
              vitalName={"Blood Glucose"}
              currentDate={"9/18/16"}
            ></Vital>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PatientDetails;
