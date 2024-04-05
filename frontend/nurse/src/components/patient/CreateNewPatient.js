import React, { useState } from "react";
import * as Yup from "yup";
import { Form, Formik, useField } from "formik";
import { useAddPatientMutation } from "../../features/patient/patientApiSlice";
import ViewPatient from "./ViewPatient";


  const label_style = "lg:pl-2 text-lg sm:text-xl lg:text-lg lg:text-base font-medium lg:font-normal";
  const input_style =
    "block rounded-xl text-black h-12 lg:h-10 w-[100%] lg:w-60 mt-1 lg:mt-0 bg-gray focus:outline-none focus:ring-2 focus:ring-lightBlue";
  const button_style =
    "h-10 w-24 px-4 py-2 text-lg rounded-md shadow-md focus:outline-none focus:ring focus:ring-gray-400";

/**
 * The text input component for forms.
 * @param label - The label for the input.
 * @param rows - The number of rows for the textarea (optional).
 * @param props - The props object.
 * @returns - The text input component.
 */
  export const MyTextInput = ({ label, ...props }) => {
    const [field, meta] = useField(props);
    return (
      <div className="px-2 lg:px-8">
        <label className={`${label_style}`} htmlFor={props.id || props.name}>
          {label}
        </label>
        <input
          className={`p-5 ${input_style} ${
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

/**
 * The text input component for forms.
 * @param label - The label for the input.
 * @param rows - The number of rows for the textarea (optional).
 * @param props - The props object.
 * @returns - The text input component.
 */
  export const MyTextBoxInput = ({ label, rows = 3, ...props }) => {
    const [field, meta] = useField(props);
    return (
      <div className="px:2 lg:px-8">
        <label className={`${label_style}`} htmlFor={props.id || props.name}>
          {label}
        </label>
        <textarea
        // "block rounded-xl h-12 lg:h-7 w-[100%] lg:w-60 mt-1 bg-gray focus:outline-none focus:ring-2 focus:ring-lightBlue"
          className={`resize-none p-5 border block rounded-md w-[100%] lg:w- mt-1 text-black focus:outline-none focus:ring-2 focus:ring-lightBlue ${
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

  /**
 * The checkbox input component for forms.
 * @param props - The props object.
 * @returns - The checkbox input component.
 */
  export const MyCheckBox = ({ children, ...props }) => {
    const [field, meta] = useField({ ...props, type: "checkbox" });
    return (
      <div className="pl-2 lg:pl-6">
        <label className={`checkbox-input ${label_style}`}>
          <input
            className={`p-5 ${input_style} ${
              meta.touched && meta.error ? "border border-red animate-shake" : ""
            }`}
            type="checkbox"
            {...field}
            {...props}
          />
          {children}
        </label>
        {meta.touched && meta.error ? (
          <div className="error">{meta.error}</div>
        ) : null}
      </div>
    );
  };

/**
 * The select input component for forms.
 * @param props - The props object.
 * @param props.label - The label for the select input.
 * @returns- The select input component.
 */
  export const MySelect = ({ label, ...props }) => {
    const [field, meta] = useField(props);
    return (
      <div className="px-2 lg:pl-8">
        <label className={`${label_style}`} htmlFor={props.id || props.name}>
          {label}
        </label>
        <select className={`pl-5 ${input_style} `} {...field} {...props} />
        {meta.touched && meta.error ? (
          <div className="error">{meta.error}</div>
        ) : null}
      </div>
    );
  };

/**
 * The select input component for forms.
 * @param props - The props object.
 * @param props.label - The label for the select input.
 * @returns- The select input component.
 */
  const MyDateInput = ({ label, ...props }) => {
    const [field, meta] = useField(props);
    const currentDateTime = new Date().toISOString().substring(0, 10);
    return (
      <div className="px-2 lg:pl-8">
        <label className={`${label_style}`} htmlFor={props.id || props.name}>
          {label}
        </label>
        <input
          className={`p-5 ${input_style} ${
            meta.touched && meta.error ? "border border-red animate-shake" : ""
          }`}
          type="date"
          max={currentDateTime}
          {...field}
          {...props}
        />
        {meta.touched && meta.error ? (
          <div className="text-sm error pl-5 text-red">{meta.error}</div>
        ) : null}
      </div>
    );
  };

/**
 * The sign-up form component.
 * @param {Object} props - The props object.
 * @param {Function} props.closeOverlay - The function to close the overlay.
 * @param {Function} props.setPatientId - The function to set the patient ID.
 * @returns {JSX.Element} - The sign-up form component.
 */
  const SignUpForm = ({ closeOverlay, setPatientId }) => {
    const [addPatient, { isLoading, isError, error }] = useAddPatientMutation();
    const [key, setKey] = useState(0); // Keep this for forcing re-render
   
    const handleSubmit = (values, { setSubmitting, resetForm }) => {
       addPatient(values)
         .unwrap()
         .then((res) => {
           setPatientId(res.id); // Use the prop function to update the state in CreateNewPatient
           setKey(prevKey => prevKey + 1); // Force a re-render
           setSubmitting(false);
           resetForm();
          //  closeOverlay();
         })
         .catch((error) => {
           alert(`Creation failed: ${error.data.error}`);
           setSubmitting(false);
         });
    };
    return (
      <div key={key}>
      <Formik
        initialValues={{
          firstName: "",
          lastName: "",
          phoneNumber: "",
          CIN: "",
          username: "",
          email: "",
          sex: "not_say",
          birthDate: "",
          address: "",
        }}
        validationSchema={Yup.object({
          firstName: Yup.string()
            .max(15, "Must be 15 characters or less")
            .required("Required"),
          lastName: Yup.string()
            .max(20, "Must be 20 characters or less")
            .required("Required"),
          phoneNumber: Yup.string()
            .required("Required"),
          email: Yup.string().email("invalid email address").required("Required"),
          CIN: Yup.string()
            .required("Required"),
          sex: Yup.string()
            .oneOf(["male", "female", "others", "not_say"], "Invalid Sex")
            .required("Required"),
          birthDate: Yup.date().required("Required"),
          username: Yup.string(),
          address: Yup.string().required("Required"),
        })}
        onSubmit={handleSubmit}
      >
        <Form className="flex mt-4 lg:mt-2 flex-col gap-3 lg:gap-4">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-3 lg:gap-4">
            <MyTextInput
              label={"First Name"}
              name="firstName"
              type="text"
              placeholder="Sabah"
            />
            <MyTextInput
              label={"Last Name"}
              name="lastName"
              type="text"
              placeholder="Hasbi"
            />

            <MyTextInput
              label={"Phone"}
              name="phoneNumber"
              type="text"
              placeholder="(406) 123-4567"
            />
            <MyTextInput
              label={"Email Address"}
              name="email"
              type="email"
              placeholder="test@example.com"
            />

            <MyTextInput
              label={"CIN"}
              name="CIN"
              type="text"
              placeholder="01234567890123456789"
            />

            <MyTextInput
              label={"Username"}
              name="username"
              type="username"
              placeholder="Username"
            />

            <MySelect label={"SEX"} name="sex">
              <option value="male">Male</option>
              <option value="female">Female</option>
              <option value="others">Others</option>
              <option value="not_say" defaultValue>
                Rather not say
              </option>
            </MySelect>
            <MyDateInput label={"Date of Birth"} name="birthDate" />
          </div>
          <MyTextBoxInput
            label={"Address"}
            name="address"
            type="text"
            placeholder="No. 0, Test Str, Example Estate"
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
              Create
            </button>
          </div>
        </Form>
      </Formik>
      </div>
    );
  };

/**
 * The component to create a new patient account.
 * @param closeOverlay - The function to close the overlay.
 * @returns - The component to create a new patient account.
 */
  const CreateNewPatient = ({ closeOverlay }) => {
    const [patientId, setPatientId] = useState(null);
   
    return (
      <>
         <div className="fixed inset-0 flex justify-center items-center backdrop-blur-sm backdrop-opacity-50 z-10 overflow-auto lg:overflow-hidden">
           <div className="flex justify-center items-center lg:mt-16 bg-lightBlue2 text-white lg:h-[85vh] rounded-xl shadow-lg w-screen sm:ml-56 lg:p-4 lg:w-auto overflow-auto">
             <div>
               <h1 className="text-2xl sm:text-3xl lg:text-xl font-semibold pt-5 lg:mt-1 text-center mb-1">Create Patient Account</h1>
               <div className="mb-12 sm:mb-5 h-[70vh] sm:h-[] sm:min-h-[60vh] overflow-auto ">
                 {/* Pass setPatientId as a prop */}
                 <SignUpForm closeOverlay={closeOverlay} setPatientId={setPatientId} />
               </div>
             </div>
           </div>
         </div>
         <div>
           {patientId && (
             <ViewPatient closeOverlay={closeOverlay} userId={patientId} />
           )}
         </div>
      </>
     );
   };

  export default CreateNewPatient;
