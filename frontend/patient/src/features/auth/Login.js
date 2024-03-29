import { useRef, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

import { useDispatch } from "react-redux";
import { setCredentials } from "./authSlice";
import { useLoginMutation } from "./authApiSlice";

import React from "react";
import * as Yup from "yup";
import { Form, Formik, useField } from "formik";

const label_style = " pl-2 text-lg font-normal";
const input_style =
  "block rounded-xl h-7 w-60 mb-5 bg-gray focus:outline-none focus:ring-2 focus:ring-lightBlue";
const button_style =
  "h-10 w-[100%] px-4 py-2 text-lg rounded-md shadow-md focus:outline-none focus:ring focus:ring-gray-400";

//<input>
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

const Login = () => {
  const userRef = useRef();
  const errRef = useRef();
  const [user, setUser] = useState("");
  const [pwd, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");
  const navigate = useNavigate();

  const [login, { isLoading }] = useLoginMutation();
  const dispatch = useDispatch();

  useEffect(() => {
    if (userRef.current)
    userRef.current.focus();
  }, [userRef.current]);

  return (
    <div className="flex w-[100vw] h-[100vh] items-center">
      <div className="h-[100%] bg-lightBlue w-[50%] mr-auto"></div>
      <div className="w-[50%]">
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
            try {
              const userData = await login(values).unwrap();
              // console.log(userData);
              setUser(values.username);
              dispatch(setCredentials({ accessToken: userData.token, user: values.username }));
              setSubmitting(false);
              navigate("/dashboard");
              resetForm();
            } catch (err) {
              console.log(`Error : `, err);
              if (err?.originalStatus) {
                setErrMsg("No Server Response");
              } else {
                setErrMsg();
              }
              if (errMsg && errRef.current) {
                errRef.current.focus();
              }
            }
          }}
        >
          {isLoading ? (
            <h1>Loading...</h1>
          ) : (
            <div className="flex flex-col justify-center items-center">
              <p
                ref={errRef}
                className={errMsg ? "errmsg" : "hidden"}
                aria-label=""
              ></p>
              <h1 className="text-xl font-semibold">Login</h1>
              <Form className="">
                <MyTextInput label={"Username"} name="username" type="text" />
                <MyTextInput label={"Password"} name="password" type="password" />
                <button
                  className={`bg-lightBlue text-white ${button_style}`}
                  type="submit"
                >
                  Login
                </button>
              </Form>
            </div>
          )}
        </Formik>
      </div>
    </div>
  );
};

export default Login;
