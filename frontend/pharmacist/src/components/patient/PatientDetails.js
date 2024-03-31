import React, { useState, useEffect } from "react";
import UpdateMedInfo from "../MedInfo/UpdateMedInfo";
import Vital from "./Vital";
import Caption from "../extra/Caption";
import { useMediaQuery } from "react-responsive";
import { useLocation } from "react-router-dom";

const PatientDetails = ({ patientId }) => {
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

  const isMobile = useMediaQuery({maxWidth:640});

  const location = useLocation()
  return (
    <div className="w-screen sm:w-[100%]">
      <div className="flex flex-col lg:flex-row justify-evenly sm:items-center lg:items-baseline">
        <div className="bg-white rounded-3xl relative mx-4 sm:mx-2 sm:w-[26rem] p-3 sm:p-5 px-8">
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
          <div className="relative w-full text-left pt-3">
            <UpdateMedInfo
              medInfo={fillDetails.allergies}
              patientId={patientId}
            />
          </div>
          <div className="relative w-[100%] text-left pt-3">
            <UpdateMedInfo
              medInfo={fillDetails.conditions}
              patientId={patientId}
            />
          </div>
          <div className="relative w-[100%] text-left pt-3">
            <UpdateMedInfo
              medInfo={fillDetails.note}
              patientId={patientId}
            />
          </div>
        </div>
        {isMobile && (location.pathname === "/dashboard") && <Caption />}
        <div className="bg-white rounded-3xl mx-auto relative lg:w-[43rem] lg:h-[20rem] p-5 mt-8 lg:mt-0">
          <p className="text-2xl font-meduim text-left">Lastest Vitals</p>
          <div className="grid gap-4 grid-cols-2 lg:grid-cols-3 mt-5 text-left">
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
      {!isMobile && (location.pathname === "/dashboard") && <Caption />}
    </div>
  );
};

export default PatientDetails;
