import React from "react";
import Vital from "../patient/Vital";

const PatientDetailsVital = ({ data }) => {
  // API call for vitals
//   console.log("Details", data)
  const { created_at, temp, bp, bpm, weight, height, glucose, notes } = data;

  return (
    <div className="w-screen sm:w-full">
      <div className="grid sm:items-center lg:items-baseline">
        <div className="bg-white rounded-3xl mx-auto relative lg:w-[43rem] lg:h-[20rem] p-5 mt-8 lg:mt-0">
          <p className="text-2xl font-meduim text-center">Recorded Vitals</p>
          <hr />
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
};

export default PatientDetailsVital;
