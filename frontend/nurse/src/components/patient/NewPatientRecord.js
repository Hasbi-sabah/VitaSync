import React, { useEffect, useState } from "react";
import * as Yup from "yup";
import { FieldArray, Form, Formik, useField } from "formik";

const label_style = "font-semibold text-lg text-left pt-6";
const input_style =
  "block rounded-xl text-sm h-10 w-64 mt-1 bg-gray focus:outline-none focus:ring-2 focus:ring-lightBlue";
const button_style =
  "sm:h-14 sm:w-28 px-4 py-2 text-lg rounded-md shadow-md focus:outline-none focus:ring focus:ring-gray-400";

//<Textbox>
export const MyTextBoxInput = ({ label, rows = 3, ...props }) => {
  const [field, meta] = useField(props);
  return (
    <div className="rounded-lg min-h-48 w-full mt-10 p-4 bg-white text-left ">
      <label className={`${label_style}`} htmlFor={props.id || props.name}>
        {label}
      </label>
      <hr className="text-[#909090] pt-3" />
      <textarea
        className={`resize-none input p-3 bg-gray block rounded-md w-full mt-1 focus:outline-none focus:ring-2 focus:ring-lightBlue ${
          meta.touched && meta.error ? "border border-red animate-shake" : ""
        }`}
        rows={rows}
        {...field}
        {...props}
        disabled={true}
      />
      {meta.touched && meta.error ? (
        <div className="error">{meta.error}</div>
      ) : null}
    </div>
  );
};

//Date
const MyDateInput = ({ label, ...props }) => {
  const [field] = useField(props);
  return (
    <div className="text-left mt-3">
      <label
        className={`${label_style} text-white`}
        htmlFor={props.id || props.name}
      >
        {label}
      </label>
      <input
        className={`input px-5 ${input_style} `}
        type="date"
        {...field}
        {...props}
        disabled={true}
      />
    </div>
  );
};

/**
 * Component for adding a new patient record.
 * @param closeOverlay - Function to close the overlay.
 * @returns- The component for adding a new patient record.
 */
const NewPatientRecord = ({ closeOverlay }) => {
  useEffect(() => {
    // Fetch patient's record from API
  }, []);

  const diagnosisSample = "diagnosis";
  const notesSample = "notes";
  const proceduresSample = "procedures sample";
  const followUpSample = new Date("2024-12-03");
  const PrescriptionSample = [
    { drug: "drug1", dosage: "prescription 1" },
    { drug: "drug3", dosage: "prescription 3" },
    { drug: "drug2", dosage: "prescription 2" },
  ];

  const vaccineSample = [
    { drug: "vaccine 1", dosage: "Vaccine note" },
    { drug: "vaccine 2", dosage: "Vaccine note" },
    { drug: "vaccine 3", dosage: "Vaccine note" },
  ];

  return (
    <Formik
      initialValues={{
        prescriptions: PrescriptionSample,
        diagnosis: diagnosisSample,
        notes: notesSample,
        procedures: proceduresSample,
        vaccine: vaccineSample,
        followUp: followUpSample.toISOString().split('T')[0],
      }}
      validationSchema={Yup.object({
        diagnosis: Yup.string().required("Required"),
        notes: Yup.string(),
        procedures: Yup.string(),
        followUp: Yup.date(),
      })}
    >
      {(formik) => {
        return (
          <Form className="flex mt-4 flex-col gap-3">
            {/* Prescription */}
            <div className="rounded-lg min-h-48 w-full mt-10 p-4 bg-white relative">
              <h3 className="font-semibold text-lg text-left pt-6">
                Prescriptions
              </h3>
              <FieldArray>
                {() => (
                  <div>
                    {PrescriptionSample.map((prescribe) => (
                      <div className="flex justify-between p-3">
                        <div></div>
                        <input
                          type="text"
                          name="prescription"
                          value={prescribe.drug}
                          className={`${input_style} p-3 h-12 w-[24rem]`}
                          disabled={true}
                        />
                        <input
                          type="text"
                          name="prescriptions_dosage"
                          value={prescribe.dosage}
                          className={`${input_style} p-3 h-12 w-[24rem]`}
                          disabled={true}
                        />
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="32"
                          height="32"
                          fill="#00ff00"
                          viewBox="0 0 256 256"
                          onClick={""}
                          className="hover:cursor-pointer"
                        >
                          <path d="M229.66,77.66l-128,128a8,8,0,0,1-11.32,0l-56-56a8,8,0,0,1,11.32-11.32L96,188.69,218.34,66.34a8,8,0,0,1,11.32,11.32Z"></path>
                        </svg>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="32"
                          height="32"
                          fill="#ff0000"
                          viewBox="0 0 256 256"
                          onClick={""}
                          className="hover:cursor-pointer"
                        >
                          <path d="M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm88,104a87.56,87.56,0,0,1-20.41,56.28L71.72,60.4A88,88,0,0,1,216,128ZM40,128A87.56,87.56,0,0,1,60.41,71.72L184.28,195.6A88,88,0,0,1,40,128Z"></path>
                        </svg>
                      </div>
                    ))}
                  </div>
                )}
              </FieldArray>
            </div>

            <MyTextBoxInput label={"Diagnosis"} name="diagnosis" type="text" />
            <MyTextBoxInput
              label={"Procedures"}
              name="procedures"
              type="text"
            />

            {/* Vaccine */}
            <div className="rounded-lg min-h-48 w-full mt-10 p-4 bg-white relative">
              <h3 className="font-semibold text-lg text-left pt-6">Vaccine</h3>

              <FieldArray>
                {() => (
                  <div>
                    {vaccineSample.map((vaccine) => (
                      <div className="flex justify-between p-3">
                        <div></div>
                        <input
                          type="text"
                          name="prescription"
                          value={vaccine.drug}
                          className={`${input_style} p-3 h-12 w-[24rem]`}
                          disabled={true}
                        />
                        <input
                          type="text"
                          name="prescriptions_dosage"
                          value={vaccine.dosage}
                          className={`${input_style} p-3 h-12 w-[24rem]`}
                          disabled={true}
                        />
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="32"
                          height="32"
                          fill="#00ff00"
                          viewBox="0 0 256 256"
                          onClick={""}
                          className="hover:cursor-pointer"
                        >
                          <path d="M229.66,77.66l-128,128a8,8,0,0,1-11.32,0l-56-56a8,8,0,0,1,11.32-11.32L96,188.69,218.34,66.34a8,8,0,0,1,11.32,11.32Z"></path>
                        </svg>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="32"
                          height="32"
                          fill="#ff0000"
                          viewBox="0 0 256 256"
                          onClick={""}
                          className="hover:cursor-pointer"
                        >
                          <path d="M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm88,104a87.56,87.56,0,0,1-20.41,56.28L71.72,60.4A88,88,0,0,1,216,128ZM40,128A87.56,87.56,0,0,1,60.41,71.72L184.28,195.6A88,88,0,0,1,40,128Z"></path>
                        </svg>
                      </div>
                    ))}
                  </div>
                )}
              </FieldArray>
              <MyTextBoxInput label={"General Notes"} name="notes" type="text" />
            </div>

            <MyDateInput label={"Follow Up"} name="followUp" />

            <div className="my-5 flex sm:justify-end sm:gap-5 justify-evenly">
              <button
                className={`bg-white text-black ${button_style}`}
                onClick={closeOverlay}
              >
                Close
              </button>
              <button
                className={`bg-lightBlue text-white ${button_style}`}
                type="submit"
              >
                Create
              </button>
            </div>
          </Form>
        );
      }}
    </Formik>
  );
};

export default NewPatientRecord;
