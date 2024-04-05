import React, { useState, useEffect } from "react";
import UpdateMedInfo from "../MedInfo/UpdateMedInfo";
import Vital from "./Vital";
import Caption from "../extra/Caption";
import { useGetPatientByIdQuery } from '../../features/patient/patientApiSlice'
import { useGetPatientVitalByIdQuery } from '../../features/vital/vitalApiSlice'
import { useGetPatientMedInfoByIdQuery, useAddPatientMedInfoByIdMutation } from '../../features/medInfo/medInfoApiSlice';
import { useMediaQuery } from "react-responsive";
import { useLocation } from "react-router-dom";

const PatientDetails = ({ patientId }) => {
  const { data: patientInfo } = useGetPatientByIdQuery(patientId);
  const { data: patientMedInfo } = useGetPatientMedInfoByIdQuery(patientId);

  // Initialize state with an empty object to avoid undefined errors
  const [medDetails, setMedDetails] = useState({});

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

  // const [addPatientMedInfoById] = useAddPatientMedInfoByIdMutation();

  // useEffect(() => {
  //   if (medDetails.medicalInfo) {
  //     addPatientMedInfoById({ variables: { userId, medInfo: medDetails.medicalInfo } });
  //   }
  // }, [medDetails, addPatientMedInfoById, userId]);
  const { medicalInfo, firstName, lastName, phoneNumber, sex, age } = medDetails;
  const { allergies, conditions, notes } = medicalInfo || {};
  const currentDate = new Date();

  const { data: reqVitals } = useGetPatientVitalByIdQuery(patientId);


  const isMobile = useMediaQuery({maxWidth:640});
  const isDesktop = useMediaQuery({minWidth:1500});

  const location = useLocation()
  if (patientInfo && medicalInfo && reqVitals){
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
    console.log(patientInfo)
    const { created_at, temp, bp, bpm, weight, height, glucose, note } = sortedVitals.length > 0 ? sortedVitals[0] : {};
    return (
      <div className="w-screen sm:w-full">
        <div className={`flex ${isDesktop ? 'flex-row items-baseline' : 'flex-col items-center' }  gap-10 justify-evenly lg:pl-10`}>
          <div className="bg-white rounded-3xl relative mx-4 sm:mx-2 sm:w-[26rem] p-3 sm:p-5 px-8">
            <div className="">
              <h2 className="text-3xl font-semibold text-center">
                {firstName ? firstName : ""} {lastName ? lastName : ""}
              </h2>
              <div className="flex justify-between text-sm">
              <span>Sex: {sex}</span>
                <span>Age: {age ? age : "N/Y"}</span>
              </div>
              <div className="mt-2 mb-2">
                <p className="text-lightBlue text-center text-sm">
                  {phoneNumber ? phoneNumber : ""}
                </p>
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
                medInfo={fillDetails.notes}
                patientId={patientId}
              />
            </div>
          </div>
          {isMobile && (location.pathname === "/dashboard") && <Caption />}
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
            </div>
          </div>
        </div>
        {!isMobile && (location.pathname === "/dashboard") && <Caption />}
      </div>
    );
  }
};

export default PatientDetails;
