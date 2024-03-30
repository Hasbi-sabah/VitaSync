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
      <label className={`${label_style} text-white`} htmlFor={props.id || props.name}>
        {label}
      </label>
      <input
        className={`input px-5 ${input_style} `}
        type="date"
        {...field}
        {...props}
      />
    </div>
  );
};

const NewPatientRecord = ({ closeOverlay }) => {
  const [drugOptions, setDrugOptions] = useState([]);
  const [vaccineOptions, setVaccineOptions] = useState([]);

  // API calls
  const fetchDrugs = async () => {};
  const fetchVaccine = async () => {};

  useEffect(() => {
    // Fetch drugs from API
    fetchDrugs().then((data) => setDrugOptions(sampleDrugs));
    fetchVaccine().then((data) => setVaccineOptions(sampleVaccines));
  }, []);

  const sampleDrugs = [
    { id: 1, name: "Drug A" },
    { id: 2, name: "Drug B" },
    { id: 3, name: "Drug C" },
    // Add more sample drugs as needed
  ];
  const sampleVaccines = [
    { id: 1, name: "Vaccine A" },
    { id: 2, name: "Vaccine B" },
    { id: 3, name: "Vaccine C" },
  ];

  const addDrugButton = ({ handleAddDrug}, type ) => (
    <div
      className="absolute top-3 right-7 bg-lightBlue2 cursor-pointer hover:bg-lightBlue h-10 p-3 flex items-center mr-2"
      onClick={() => handleAddDrug(type)}
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
      <p className="text-white text-lg pl-2">Add drug</p>
    </div>
  );
  return (
    <Formik
      initialValues={{
        prescriptions: [],
        diagnosis: "",
        notes: "",
        procedures: "",
        vaccine: [],
        followUp: "",
      }}
      validationSchema={Yup.object({
        diagnosis: Yup.string().required("Required"),
        notes: Yup.string(),
        procedures: Yup.string(),
        followUp: Yup.date(),
      })}
      onSubmit={(values, { setSubmitting, resetForm }) => {
        setTimeout(() => {
          alert(JSON.stringify(values, null, 2));
          setSubmitting(false);
          resetForm();
        }, 400);
      }}
    >
      {(formik) => {
        const handleAddDrug = (type) => {
          formik.setFieldValue(type, [
            ...formik.values[type],
            { drug: "", dosage: "" }, // Initialize with empty values
          ]);
        };
        return (
          <Form className="flex mt-4 flex-col gap-3">
            {/* Prescription */}
            <div className="rounded-lg min-h-48 w-full mt-10 p-4 bg-white relative">
              <h3 className="font-semibold text-lg text-left pt-6">
                Prescriptions
              </h3>

              {/* Add drug button */}
              {addDrugButton({ handleAddDrug }, "prescriptions")}

              <FieldArray name="prescriptions">
                {(arrayHelpers) => (
                  <div>
                    {formik.values.prescriptions.map((prescribe, index) => (
                      <div key={index} className="flex justify-between p-3">
                        <div>
                          {index + 1}.
                          <select
                            className={`${input_style} inline ml-4 pl-2`}
                            name={`prescriptions.${index}.drug`}
                            onChange={formik.handleChange}
                            value={prescribe.drug}
                          >
                            <option value="">Select drug</option>
                            {drugOptions.map((drug) => (
                              <option key={drug.id} value={drug.id}>
                                {drug.name}
                              </option>
                            ))}
                          </select>
                        </div>
                        <input
                          type="text"
                          name={`prescriptions.${index}.dosage`}
                          onChange={formik.handleChange}
                          value={prescribe.dosage}
                          className={`${input_style} p-3 h-12 w-[24rem]`}
                          placeholder="Dosage instructions"
                        />
                        <svg
                          className="cursor-pointer"
                          onClick={() => arrayHelpers.remove(index)}
                          xmlns="http://www.w3.org/2000/svg"
                          width="32"
                          height="32"
                          fill="#ff0000"
                          viewBox="0 0 256 256"
                        >
                          <path d="M216,48H176V40a24,24,0,0,0-24-24H104A24,24,0,0,0,80,40v8H40a8,8,0,0,0,0,16h8V208a16,16,0,0,0,16,16H192a16,16,0,0,0,16-16V64h8a8,8,0,0,0,0-16ZM96,40a8,8,0,0,1,8-8h48a8,8,0,0,1,8,8v8H96Zm96,168H64V64H192ZM112,104v64a8,8,0,0,1-16,0V104a8,8,0,0,1,16,0Zm48,0v64a8,8,0,0,1-16,0V104a8,8,0,0,1,16,0Z"></path>
                        </svg>
                      </div>
                    ))}
                  </div>
                )}
              </FieldArray>
            </div>

            <MyTextBoxInput label={"Diagnosis"} name="diagnosis" type="text" />
            <MyTextBoxInput label={"Notes"} name="notes" type="text" />
            <MyTextBoxInput
              label={"Procedures"}
              name="procedures"
              type="text"
            />

            {/* Vaccine */}
            <div className="rounded-lg min-h-48 w-full mt-10 p-4 bg-white relative">
              <h3 className="font-semibold text-lg text-left pt-6">Vaccine</h3>

              {/* Add drug button */}
              {addDrugButton({ handleAddDrug }, "vaccine")}

              <FieldArray name="vaccine">
                {(arrayHelpers) => (
                  <div>
                    {formik.values.vaccine.map((prescribe, index) => (
                      <div key={index} className="flex justify-between p-3">
                        <div>
                          {index + 1}.
                          <select
                            className={`${input_style} inline ml-4 pl-2`}
                            name={`vaccine.${index}.drug`}
                            onChange={formik.handleChange}
                            value={prescribe.drug}
                          >
                            <option value="">Select vaccine</option>
                            {vaccineOptions.map((drug) => (
                              <option key={drug.id} value={drug.id}>
                                {drug.name}
                              </option>
                            ))}
                          </select>
                        </div>
                        <textarea
                          type="text"
                          name={`vaccine.${index}.dosage`}
                          onChange={formik.handleChange}
                          value={prescribe.dosage}
                          className={`resize-none input p-3 bg-gray block rounded-md w-[20rem] mt-1 focus:outline-none focus:ring-2 focus:ring-lightBlue`}
                          rows={4}
                          placeholder="Vaccine instructions"
                        />
                        <svg
                          className="cursor-pointer"
                          onClick={() => arrayHelpers.remove(index)}
                          xmlns="http://www.w3.org/2000/svg"
                          width="32"
                          height="32"
                          fill="#ff0000"
                          viewBox="0 0 256 256"
                        >
                          <path d="M216,48H176V40a24,24,0,0,0-24-24H104A24,24,0,0,0,80,40v8H40a8,8,0,0,0,0,16h8V208a16,16,0,0,0,16,16H192a16,16,0,0,0,16-16V64h8a8,8,0,0,0,0-16ZM96,40a8,8,0,0,1,8-8h48a8,8,0,0,1,8,8v8H96Zm96,168H64V64H192ZM112,104v64a8,8,0,0,1-16,0V104a8,8,0,0,1,16,0Zm48,0v64a8,8,0,0,1-16,0V104a8,8,0,0,1,16,0Z"></path>
                        </svg>
                      </div>
                    ))}
                  </div>
                )}
              </FieldArray>
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
