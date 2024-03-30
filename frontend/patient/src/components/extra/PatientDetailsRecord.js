import React, { useState, useEffect } from "react";
import UpdateMedInfo from "../MedInfo/UpdateMedInfo";
import Caption from "../extra/Caption";
import { useMediaQuery } from "react-responsive";
import { useLocation } from "react-router-dom";
import Vital from "../patient/Vital";

const PatientDetailsRecord = ({ data }) => {
  // API call for vitals
//   console.log("Details", data)
  const reqVitals = {}; //status, temp, bp, bpm, weight, height, glucose, notes
  const { status, temp, bp, bpm, weight, height, glucose, notes } = reqVitals;

  return (
    <div className="w-screen sm:w-full">
      <div className="grid sm:items-center lg:items-baseline">
        <div className="bg-white rounded-3xl mx-auto relative lg:w-[43rem] lg:h-[20rem] p-5 mt-8 lg:mt-0">
          <p className="text-2xl font-meduim text-center">Recorded Vitals</p>
          <hr />
          <div className="grid gap-4 grid-cols-2 lg:grid-cols-3 mt-5 text-left">
            {/* API call to get the vitals */}
            <Vital
              Vitalreading={"90 °F"}
              vitalName={"Temperature"}
              currentDate={"Today"}
            />
            <Vital
              Vitalreading={"120/80 mm hg"}
              vitalName={"Blood Pressure"}
              currentDate={"Today"}
            />
            <Vital
              Vitalreading={"70 bpm"}
              vitalName={"Hearth rate"}
              currentDate={"Today"}
            />
            <Vital
              Vitalreading={"70 kg"}
              vitalName={"Weight"}
              currentDate={"10/28/12"}
            />
            <Vital
              Vitalreading={"173 cm"}
              vitalName={"Height"}
              currentDate={"3/4/16"}
            />
            <Vital
              Vitalreading={"80 mg/dL"}
              vitalName={"Blood Glucose"}
              currentDate={"9/18/16"}
            />
          </div>
        </div>
        <div className="bg-white rounded-lg mt-5 w-full">
            <h2 className="text-center text-2xl font-meduim">Prescriptions</h2>
            <hr />
            <div className="table w-full">
                <div className="table-header-group w-full">
                    <div className="table-row w-full bg-gray">
                        <div className="table-cell text-center">Drug</div>
                        <div className="table-cell text-center">Dosage</div>
                    </div>
                </div>
                <div className="table-row-group w-full">
                {data.prescriptions && (data.prescriptions).map((item, idx) =>
                    <div className="table-row w-full" key={idx}>
                        <div className="table-cell text-center">{item.drug}</div>
                        <div className="table-cell text-left">{item.dosage}</div>
                    </div>
                )}
                </div>
            </div>
        </div>
        <div className="bg-white rounded-sm mx-auto w-full mt-5 ">
            <h2 className="text-center text-2xl font-meduim">Diagnosis</h2>
            <hr />
            {data.diagnosis}
        </div>
        <div className="bg-white rounded-sm mx-auto w-full mt-5 ">
            <h2 className="text-center text-2xl font-meduim">Notes</h2>
            <hr />
            {data.notes}
        </div>
        <div className="bg-white rounded-sm mx-auto w-full mt-5 ">
            <h2 className="text-center text-2xl font-meduim">Procedures</h2>
            <hr />
            {data.procedures}
        </div>
        <div className="bg-white rounded-sm mx-auto w-full mt-5 ">
            <h2 className="text-center text-2xl font-meduim">Vaccine</h2>
            <hr />
            <div className="table w-full">
                <div className="table-header-group w-full">
                    <div className="table-row w-full bg-gray">
                        <div className="table-cell text-center">Drug</div>
                        <div className="table-cell text-center">Dosage</div>
                    </div>
                </div>
                <div className="table-row-group w-full">
                {data.vaccine && (data.vaccine).map((item, idx) =>
                    <div className="table-row w-full" key={idx}>
                        <div className="table-cell text-center">{item.drug}</div>
                        <div className="table-cell text-left">{item.dosage}</div>
                    </div>
                )}
                </div>
            </div>
        </div>
        <div className="bg-white rounded-sm mx-auto w-full mt-5 ">
            <h2 className="text-center text-2xl font-meduim">Follow Up Date</h2>
            <hr />
            {data.followUp}
        </div>
      </div>
    </div>
  );
};

export default PatientDetailsRecord;
