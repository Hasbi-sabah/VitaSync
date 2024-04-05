import React, { useEffect, useState } from "react";
import * as Yup from "yup";
import { FieldArray, Form, Formik, useField } from "formik";
import { useAddPatientAppointmentByIdMutation } from "../../features/appointment/appointmentApiSlice"
import { useAddPatientRecordByIdMutation } from "../../features/record/recordApiSlice"
import { useAddPatientProcedureByIdMutation } from "../../features/procedure/procedureApiSlice"
import { useAddPatientPrescriptionByIdMutation } from "../../features/prescription/prescriptionApiSlice"
import { useAddPrescriptionDrugsByIdMutation } from "../../features/prescDrug/prescDrugApiSlice"
import SearchBoxSmall from "../extra/SearchboxSmall";

const label_style = "font-semibold text-lg text-left pt-6";
const input_style =
  "block rounded-xl text-sm h-10 w-64 mt-1 bg-gray focus:outline-none focus:ring-2 focus:ring-lightBlue";
const button_style =
  "sm:h-14 sm:w-28 px-4 py-2 text-lg rounded-md shadow-md focus:outline-none focus:ring focus:ring-gray-400";
const removeEmptyValues = (obj) => {
  const filteredEntries = Object.entries(obj).filter(([key, value]) => value !== '' && value.length > 0);
  return Object.fromEntries(filteredEntries);
  };
//<Textbox>
export const MyTextBoxInput = ({ label, rows = 3, formik, ...props }) => {
  const [field, meta] = useField(props);
  const [isToggled, setIsToggled] = useState(false);

  const handleToggleChange = (event) => {
     const newStatus = event.target.checked;
     setIsToggled(newStatus);
     formik.setFieldValue("status", newStatus);
  };
  return (
    <div className="rounded-lg min-h-48 w-full mt-10 p-4 bg-white text-left ">
      <label className={`${label_style}`} htmlFor={props.id || props.name}>
        {label}
      </label>
      {props.name === 'procedures' && <label class="inline-flex float-right items-center cursor-pointer">
      <p class="mr-3">{isToggled ? 'Performed' : 'Not performed'}</p>      
        <input 
          type="checkbox"
          value="" 
          className="sr-only peer"
          checked={isToggled}
          onChange={handleToggleChange} 
        />
        <div class="relative w-11 h-6 bg-gray peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-lightBlue dark:peer-focus:ring-lightBlue2 rounded-full peer dark:bg-darkBlue peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-500 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-400 peer-checked:bg-blue"></div>
        </label>}
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
  const currentDateTime = new Date().toISOString().substring(0, 16);
  return (
    <div className="text-left mt-3">
      <label className={`${label_style} text-white`} htmlFor={props.id || props.name}>
        {label}
      </label>
      <input
        className={`input px-5 ${input_style} `}
        type="datetime-local"
        min={currentDateTime}
        {...field}
        {...props}
      />
    </div>
  );
};

/**
 * Component for adding a new patient record.
 * @param userId - The ID of the user for whom the record is being added.
 * @param closeOverlay - Function to close the overlay.
 * @returns- The component for adding a new patient record.
 */
const NewPatientRecord = ({ userId, closeOverlay }) => {
  // const [drugOptions, setDrugOptions] = useState([]);
  const [vaccineOptions, setVaccineOptions] = useState([]);

  const addDrugButton = ({ handleAddDrug }, type) => (
    <div
      className="absolute top-3 right-7 bg-lightBlue2 cursor-pointer hover:bg-lightBlue h-10 p-3 flex items-center mr-2"
      onClick={() => handleAddDrug('', type, '')}
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

 //API calls
  const [addAppt, { apptInfo }] = useAddPatientAppointmentByIdMutation()
  const [addRecord, { recInfo }] = useAddPatientRecordByIdMutation()
  const [addProcedure, { proInfo }] = useAddPatientProcedureByIdMutation()
  const [addPrescription, { prescInfo }] = useAddPatientPrescriptionByIdMutation()
  const [addPrescDrug, { prescDrugInfo }] = useAddPrescriptionDrugsByIdMutation()

  const [isProcedurePerformed, setIsProcedurePerformed] = useState(false);
  const [drugOptions, setDrugOptions] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredDrugs, setFilteredDrugs] = useState([]);
  const [searchListVisibles, setSearchListVisibles] = useState([]);
  const [searchValues, setSearchValues] = useState([]);
  const toggleSearchListVisible = (index) => {
    const newSearchListVisibles = [...searchListVisibles];
    newSearchListVisibles[index] = !newSearchListVisibles[index]; // Toggle the visibility state
    setSearchListVisibles(newSearchListVisibles);
   };
  useEffect(() => {
   const results = drugOptions.filter(drug =>
     drug.commercialName.toLowerCase().includes(searchTerm.toLowerCase())
   );
   setFilteredDrugs(results);
}, [searchTerm, drugOptions]);

  // Function to update the toggle state
  const handleToggleChange = (newStatus) => {
     setIsProcedurePerformed(newStatus);
  };
  return (
    <Formik
      initialValues={{
        prescriptions: [],
        diagnosis: "",
        notes: "",
        procedures: "",
        vaccine: [],
        status: false,
        followUp: "",
      }}
      validationSchema={Yup.object({
        diagnosis: Yup.string(),
        notes: Yup.string(),
        procedures: Yup.string(),
        status: Yup.bool(),
        followUp: Yup.date(),
      })}
      onSubmit={(values, { setSubmitting, resetForm }) => {
        let recDict = {};
        let promises = []
        if (values.notes !== "") {
          recDict.notes = values.notes;
        }
        if (values.diagnosis !== "") {
          recDict.diagnosis = values.diagnosis;
          }
        if (values.procedures) {
          let proDict = {name: values.procedures, status: values.status}
          let promise = addProcedure({id: userId, data: proDict})
          .then((res) => {
            recDict['procedureId'] = res.data.id
            console.log('procedure created')
          })
          .catch((error) => {
            alert(`Procedure reation failed: ${error.data.error}`);
            setSubmitting(false);
          })
          promises.push(promise);
        }
        if (values.prescriptions.length > 0) {
          let promise = addPrescription(userId)
          .then((res) => {
            let prscDict = {}
            recDict['prescriptionId'] = res.data.id
            for (let drug of values.prescriptions) {
              prscDict['drugId'] = drug.id
              prscDict['instructions'] = drug.instructions
              addPrescDrug({id: res.data.id, data: prscDict})
              .then(() => {
                console.log('prescription created')
              })
            }
          })
          promises.push(promise)
        }
        if (promises.length > 0){
        Promise.all(promises)
          .then(() => {   
            addRecord({id: userId, data: recDict})
            .then(() => {
              // alert('rec created yay')         
              setSubmitting(false);
              resetForm();
              window.location.reload()
            })
          })
          .catch((error) => {
            alert(`Initial request failed: ${error.data.error}`);
            setSubmitting(false);
          })}
        
        if (values.followUp !== "") {
          const followUpDate = new Date(values.followUp);

          // Format the date part
          const year = followUpDate.getFullYear();
          const month = String(followUpDate.getMonth() + 1).padStart(2, '0'); // Months are 0-based in JavaScript
          const day = String(followUpDate.getDate()).padStart(2, '0');
      
          // Format the time part with AM/PM
          let hour = followUpDate.getHours();
          const minute = String(followUpDate.getMinutes()).padStart(2, '0');
          const ampm = hour >= 12 ? 'PM' : 'AM';
          hour = hour % 12 || 12; // Convert to 12-hour format and handle 0 hour
      
          // Construct the formatted string
          values.followUp = `${year}-${month}-${day} ${hour}:${minute} ${ampm}`
          addAppt({id: userId, data: {time: values.followUp}})
              .then(() => {
                setSubmitting(false);
                resetForm();
                closeOverlay();
                window.location.reload()
            })
            .catch((error) => {
              alert(`Creation failed: ${error.data.error}`);
              setSubmitting(false);
            })
        }
      }}
    >
      {(formik) => {

        const handleDosageChange = (event, index) => {
          const instructions = event.target.value;
          formik.setFieldValue(`prescriptions.${index}.instructions`, instructions);
         };
         const handleDrugSelection = (id, name, index) => {
          formik.setFieldValue(`prescriptions.${index}.drug`, name);
          formik.setFieldValue(`prescriptions.${index}.id`, id);
          toggleSearchListVisible(index)
          const newSearchValues = [...searchValues];
          newSearchValues[index] = name; // Assuming 'name' is the value you want to save
          setSearchValues(newSearchValues);
         };
        const handleAddDrug = (id='', type='', instructions='') => {
          const currentDrugs = Array.isArray(formik.values[type]) ? formik.values[type] : [];
          formik.setFieldValue(type, [
            ...currentDrugs,
            { drug: id, instructions: instructions }, // Initialize with empty values
          ]);
        };
        const handleRemoveItem = (index, arrayHelpers) => {
          arrayHelpers.remove(index);
          // Update the search bar's value for the removed item
          const newSearchValues = [...searchValues];
          newSearchValues[index] = ''; // Clear the search bar's value
          setSearchValues(newSearchValues);
         };         
        console.log(formik.values)
        return (
          <Form className="flex mt-4 flex-col gap-3">
            {/* Prescription */}
            <div className="rounded-lg min-h-18 w-full mt-10 p-4 bg-white relative">
              <h3 className="font-semibold text-lg text-left">
                Prescriptions
              </h3>

              {/* Add drug button */}
              {addDrugButton({ handleAddDrug }, "prescriptions")}
              <FieldArray name="prescriptions">
                {(arrayHelpers) => (
                  <div>
                    {formik.values.prescriptions.map((prescribe, index) => (
                      <div key={index} className="flex justify-between p-3 mt-2">
                        <div className="relative">
                        <SearchBoxSmall
                            key={prescribe.id}
                            index={index}
                            searchValue={searchValues[index] || ''}
                            setSearchValue={(value) => {
                                const newSearchValues = [...searchValues];
                                newSearchValues[index] = value;
                                setSearchValues(newSearchValues);
                            }}
                            setDrugOptions={setDrugOptions}
                            setSearchListVisible={() => toggleSearchListVisible(index)} // Pass the index to the function
                            />
                          {searchListVisibles[index] && (
                              <div className="absolute bg-white top-full left-0 w-full z-10">
                                {filteredDrugs.map((drug) => (
                                  <div
                                    key={index}
                                    name={`prescriptions.${index}.name`}
                                    className="p-2 rounded-md cursor-pointer hover:bg-gray"
                                    onClick={() => handleDrugSelection(drug.id, `${drug.commercialName} (${drug.activeIngredient}) ${drug.form}, ${drug.dose}`, index)}
                                  >
                                    {drug.commercialName} ({drug.activeIngredient}), {drug.form}, {drug.dose}
                                  </div>
                                ))}
                              </div>
                          )}
                          </div>
                        <input
                          type="text"
                          name={`prescriptions.${index}.dosage`}
                          onChange={(event) => handleDosageChange(event, index)}
                          value={prescribe.dosage}
                          className={`${input_style} p-3 h-12 w-[24rem]`}
                          placeholder="Dosage instructions"
                        />
                        <svg
                          className="cursor-pointer mt-3"
                          onClick={() => handleRemoveItem(index, arrayHelpers)}
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
            {/* Vaccine */}
            <div className="rounded-lg min-h-18 w-full mt-10 p-4 bg-white relative">
              <h3 className="font-semibold text-lg text-left ">Vaccine</h3>

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
                          placeholder="Notes"
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
            <MyTextBoxInput
              label={"Procedures"}
              name="procedures"
              type="text"
              formik={formik}
            />
            <MyTextBoxInput label={"General Notes"} name="notes" type="text" />
            <div className="flex justify-between">
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
            </div>
            
          </Form>
        );
      }}
    </Formik>
  );
};

export default NewPatientRecord;
