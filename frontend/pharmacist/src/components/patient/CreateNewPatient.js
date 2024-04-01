import React from "react";
import * as Yup from "yup";
import { Form, Formik, useField } from "formik";
import { useAddPatientMutation } from "../../features/patient/patientApiSlice";

const label_style =
  "lg:pl-2 text-lg sm:text-xl lg:text-lg lg:text-base font-medium lg:font-normal";
const input_style =
  "block rounded-xl text-black h-12 lg:h-7 w-[100%] lg:w-60 mt-1 lg:mt-0 bg-gray focus:outline-none focus:ring-2 focus:ring-lightBlue";
const button_style =
  "h-10 w-24 px-4 py-2 text-lg rounded-md shadow-md focus:outline-none focus:ring focus:ring-gray-400";

//<input>
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

//<Textbox>
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

// checkbox
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

// Select
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

//Date
const MyDateInput = ({ label, ...props }) => {
  const [field, meta] = useField(props);
  return (
    <div className="px-2 lg:pl-8">
      <label className={`${label_style}`} htmlFor={props.id || props.name}>
        {label}
      </label>
      <input
        className={`pl-5 ${input_style} ${
          meta.touched && meta.error ? "border border-red animate-shake" : ""
        }`}
        type="date"
        {...field}
        {...props}
      />
      {meta.touched && meta.error ? (
        <div className="text-sm error pl-5 text-red">{meta.error}</div>
      ) : null}
    </div>
  );
};

const SignUpForm = ({ closeOverlay }) => {
  const [addPatient, { isLoading, isError, error }] = useAddPatientMutation();
  return (
    <Formik
      initialValues={{
        firstname: "",
        lastname: "",
        phone: "",
        cin: "",
        email: "",
        sex: "not_say",
        dob: "",
        address: "",
      }}
      validationSchema={Yup.object({
        firstname: Yup.string()
          .max(15, "Must be 15 characters or less")
          .required("Required"),
        lastname: Yup.string()
          .max(20, "Must be 20 characters or less")
          .required("Required"),
        phone: Yup.string()
          .matches(/^\d+$/, "Must be a number")
          .required("Required"),
        email: Yup.string().email("invalid email address").required("Required"),
        cin: Yup.string().required("Required"),
        sex: Yup.string()
          .oneOf(["male", "female", "others", "not_say"], "Invalid Sex")
          .required("Required"),
        dob: Yup.date().required("Required"),
        address: Yup.string(),
      })}
      onSubmit={(values, { setSubmitting, resetForm }) => {
        addPatient(values)
          .unwrap()
          .then(() => {
            alert("New patient created");
            setSubmitting(false);
            resetForm();
            alert(JSON.stringify(values, null, 2));
            closeOverlay();
          })
          .catch((error) => {
            console.error("Creation failed", error);
            setSubmitting(false);
          });
        // setTimeout(() => {
        //   alert(JSON.stringify(values, null, 2));
        //   setSubmitting(false);
        //   resetForm();
        // }, 400);
      }}
    >
      <Form className="flex mt-4 lg:mt-2 flex-col gap-3 lg:gap-4">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-3 lg:gap-4">
          <MyTextInput
            label={"First Name"}
            name="firstname"
            type="text"
            placeholder="Sabah"
          />
          <MyTextInput
            label={"Last Name"}
            name="lastname"
            type="text"
            placeholder="Hasbi"
          />

          <MyTextInput
            label={"Phone"}
            name="phone"
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
            name="cin"
            type="number"
            placeholder="01234567890123456789"
          />

          <MySelect label={"SEX"} name="sex">
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="others">Others</option>
            <option value="not_say" selected>
              Rather not say
            </option>
          </MySelect>
        </div>

        <MyDateInput label={"Date of Birth"} name="dob" />

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
  );
};

const CreateNewPatient = ({ closeOverlay }) => {
  return (
    <div className="fixed inset-0 flex justify-center items-center backdrop-blur-sm backdrop-opacity-50 z-10 overflow-auto lg:overflow-hidden">
      <div className="flex justify-center items-center lg:mt-16 sm:mt-[10%] mt-[20%] bg-lightBlue2 text-white lg:h-[85vh] rounded-xl shadow-lg w-screen sm:ml-56 lg:p-4 lg:w-auto overflow-auto">
        <div>
          <h1 className="text-2xl sm:text-3xl lg:text-xl font-semibold pt-3 lg:mt-1 text-center mb-1">
            Create Patient Account
          </h1>
          <div className="mb-12 sm:mb-5 h-[80vh] sm:h-[] sm:min-h-[60vh] overflow-auto ">
            {SignUpForm({ closeOverlay })}
          </div>
        </div>
      </div>
    </div>
  );
};

export default CreateNewPatient;
