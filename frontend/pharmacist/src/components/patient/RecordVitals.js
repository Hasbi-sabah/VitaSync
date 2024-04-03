import { Form, Formik, useField} from 'formik';
import React, { useState, useEffect  } from 'react';
import * as Yup from "yup";
import { useAddPatientVitalByIdMutation } from "../../features/vital/vitalApiSlice";
import LoadingScreen from '../LoadingScreen'; // Adjust the import path as necessary

const label_style = "lg:pl-2 text-lg sm:text-base lg:text-base lg:text-base font-medium lg:font-normal w-32 ";
const input_style =
 "rounded-lg text-right text-black h-6 lg:h-8 w-[50%] lg:w-[50%] mt-1 lg:mt-0 bg-gray focus:outline-none focus:ring-2 focus:ring-lightBlue";
const button_style =
 "h-10 w-24 px-4 mx-4 py-2 mb-4 text-lg rounded-md shadow-md focus:outline-none focus:ring focus:ring-gray-400";

export const MyTextInput = ({ label, ...props }) => {
    const [field, meta] = useField(props);
    return (
      <div className="px-3 lg:px-5 flex text-right justify-between items-center ">
        <label className={`${label_style}`} htmlFor={props.id || props.name}>
          {label}
        </label>
        <input
          className={`p-2 ${input_style} ${
            meta.touched && meta.error ? "border border-red animate-shake" : ""
          }`}
          {...field}
          {...props}
        />
        {meta.touched && meta.error ? (
          <div className="error pl-5 text-sm text-red">{meta.error}</div>
        ) : null}
      </div>
    );
};

export const MyTextBoxInput = ({ label, rows = 3, ...props }) => {
    const [field, meta] = useField(props);
    return (
      <div className="px:2 lg:px-8">
        <label className={`${label_style} `} htmlFor={props.id || props.name}>
          {label}
        </label>
        <textarea
          className={`resize-none p-5 border rounded-md w-[100%] lg:w- mt-1 text-black focus:outline-none focus:ring-2 focus:ring-lightBlue ${
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

const RecordVitals = ({closeOverlay, patientId}) => {
 const [ addVital, { data: vitalInfo, loading }] = useAddPatientVitalByIdMutation();
 const [isLoading, setIsLoading] = useState(true); // Initialize isLoading to true
 const removeEmptyValues = (obj) => {
    const filteredEntries = Object.entries(obj).filter(([key, value]) => value !== '');
    return Object.fromEntries(filteredEntries);
   };

 useEffect(() => {
    if (!loading) {
      setIsLoading(false); // Set isLoading to false once the mutation is not loading
    }
 }, [loading]);

 return (
    <div className='fixed inset-0 flex justify-center items-center backdrop-blur-sm backdrop:bg-opacity-50 z-10'>
        <div className='bg-white rounded-md '>
            <h1 className='text-xl font-semibold p-6'>Record Vitals</h1>
            {isLoading ? (
              <LoadingScreen />
            ) : (
              <Formik
                 initialValues={{
                      temp: "",
                      bp: "",
                      bpm: "",
                      weight: "",
                      height: "",
                      glucose: "",
                      custom: "",
                      note: "",
                 }}
                 validationSchema={Yup.object({
                      temp: Yup.number(),
                      bp: Yup.string(),
                      bpm: Yup.number(),
                      weight: Yup.number(),
                      height: Yup.number(),
                      glucose: Yup.number(),
                      custom: Yup.string(),
                      note: Yup.string(),
                 })}
                 onSubmit={(values, { setSubmitting, resetForm }) => {
                    addVital([patientId, removeEmptyValues(values)]).unwrap()
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
                 }}
              >
                 <Form className='flex flex-col w-[32rem] gap-4'>
                      <MyTextInput
                          label={"Temperature"}
                          name="temp"
                          type="text"
                          placeholder="°C"
                      />
                      <MyTextInput
                          label={"Blood Pressure"}
                          name="bp"
                          type="text"
                          placeholder="mm hd"
                      />
                      <MyTextInput
                          label={"Heart Rate"}
                          name="bpm"
                          type="text"
                          placeholder="bpm"
                      />
                      <MyTextInput
                          label={"Weight"}
                          name="weight"
                          type="text"
                          placeholder="kg"
                      />
                      <MyTextInput
                          label={"Height"}
                          name="height"
                          type="text"
                          placeholder="cm"
                      />
                      <MyTextInput
                          label={"Blood Glucose"}
                          name="glucose"
                          type="text"
                          placeholder="mg/dL"
                      />
                      <MyTextBoxInput
                          label={"Custom"}
                          name="custom"
                          type="text"
                          placeholder="Custom"
                      />
                      <MyTextBoxInput
                          label={"Note"}
                          name="note"
                          type="text"
                          placeholder="Note"
                      />
                      <div className="flex justify-evenly lg:justify-end gap-5">
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
                          Save
                      </button>
                      </div>
                 </Form>
              </Formik>
            )}
        </div>
    </div>
 )
}

export default RecordVitals;