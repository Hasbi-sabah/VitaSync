import React, { useRef, useState } from "react";
import { useLoginMutation } from "./authApiSlice";
import * as Yup from "yup";
import { Form, Formik, useField } from "formik";
import LoadingScreen from '../../components/LoadingScreen';


const label_style = " pl-2 text-lg font-normal";
const input_style =
  "block rounded-xl h-7 w-60 mb-1 bg-gray focus:outline-none focus:ring-2 focus:ring-lightBlue";
const button_style =
  "h-10 w-[100%] px-4 py-2 text-lg rounded-md shadow-md focus:outline-none focus:ring focus:ring-gray-400";

/**
 * Custom text input component for the login form.
 * This component uses Formik's useField hook for form state management and validation.
 * @param {Object} props - The props object containing label and other input attributes.
 * @returns {JSX.Element} The rendered text input field with validation and error handling.
 */
const MyTextInput = ({ label, ...props }) => {
  const [field, meta] = useField(props);
  return (
    <div className="">
      <label className={`${label_style}`} htmlFor={props.id || props.name}>
        {label}
      </label>
      <input
        autoComplete="off"
        className={`input p-5 ${input_style} ${
          meta.touched && meta.error ? "border border-red animate-shake" : ""
        }`}
        {...field}
        {...props}
      />
      {meta.touched && meta.error ? (
        <div className="error pl-5 text-red">{meta.error}</div>
      ) : null}
    </div>
  );
};

/**
 * Component for user login.
 * 
 * This component provides a login form for users to authenticate.
 */
const Login = () => {
  const errRef = useRef();
  const [errMsg, setErrMsg] = useState("");
  const [errCode, setErrCode] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const [login] = useLoginMutation();

  // Environment variable links
  const authLink = process.env.REACT_APP_AUTH_URL;
  const docLink = process.env.REACT_APP_DOC_URL;
  const nurseLink = process.env.REACT_APP_NUR_URL;
  const patientLink = process.env.REACT_APP_PAT_URL;
  const pharmacyLink = process.env.REACT_APP_PHA_URL;
  
  /**
   * Handles the redirection of the user after successful login based on their role.
   * @param {string} userId - The ID of the logged-in user.
   * @param {string} role - The role of the logged-in user.
   * @param {string} token - The authentication token for the logged-in user.
   * @param {string} username - The username of the logged-in user.
   * @returns {null} This function does not return anything. It performs a side effect of redirecting the user.
   */
  const handleRedirect = (userId, role, token, username) => {
    const params = `token=${token}&role=${role}&id=${userId}&username=${username}`;
    setIsLoading(false);
    if (role === "doctor" || role === "admin")
      window.location.href = `${docLink}/dashboard?${params}`;
    else if (role === "nurse")
      window.location.href = `${nurseLink}/dashboard?${params}`;
    else if (role === "patient")
      window.location.href = `${patientLink}/dashboard?${params}`;
    else if (role === "pharmacist")
      window.location.href = `${pharmacyLink}/dashboard?${params}`;
    else window.location.href = `${authLink}/dashboard?${params}`;
    return null;
  }

  // Render loading screen if loading
  if (isLoading) {
    return <LoadingScreen />;
  }
  return (
    <div className="flex w-[100vw] h-[100vh] items-center">
      <div className="h-[100%] bg-lightBlue sm:w-[50%] mr-auto"></div>
      <div className="w-full sm:w-[50%]">
        <Formik
          initialValues={{
            username: "",
            password: "",
          }}
          validationSchema={Yup.object({
            username: Yup.string().required("Field Required"),
            password: Yup.string().required("Field Required"),
          })}
          onSubmit={async (values, { setSubmitting, resetForm }) => {
            setIsLoading(true);
            try {
              const userData = await login(values).unwrap();
              handleRedirect(userData.id, userData.role, userData.token);
              resetForm();
            } catch (err) {
              setIsLoading(false);
              if (err?.originalStatus) {
                setErrCode(err?.status)
                setErrMsg("No Server Response");
              } else {
                // console.log(err);
                setErrCode(err?.status)
                setErrMsg(err.data.error);
              }
              if (errMsg && errRef.current) {
                errRef.current.focus();
              }
            }
          }}
        >
            <div className="flex flex-col justify-center items-center">
              <h1 className="text-xl font-semibold p-5">Login</h1>
              <Form className="">
                <div className={"mb-5"}>
                  <MyTextInput label={"Username"} name="username" type="text" />
                  {(errMsg) ? <span
                    ref={errRef}
                    className={`${errMsg ? "errmsg" : "hidden"} text-red error pl-5`}
                    aria-label=""
                  > Wrong credentials</span> : ""}
                </div>
                <div className={"mb-5"}>
                  <MyTextInput
                    label={"Password"}
                    name="password"
                    type="password"
                  />
                </div>
                <button
                  className={`bg-lightBlue text-white ${button_style}`}
                  type="submit"
                >
                  Login
                </button>
              </Form>
            </div>
        </Formik>
      </div>
    </div>
  );
};

export default Login;
