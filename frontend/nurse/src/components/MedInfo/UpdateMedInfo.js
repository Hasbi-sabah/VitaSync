import { Formik, Form, useField } from "formik";
import React, { useState } from "react";
import * as Yup from "yup";

const label_style = "pl-2 text-l font-normal";

const UpdateMedInfo = ({ edit, setFunction, medInfo, patientId }) => {
  //<input>
  const TextInput = ({ label, ...props }) => {
    const [field] = useField(props);
    return (
      <div className="">
        <label className={`${label_style}`} htmlFor={props.id || props.name}>
          {label}
        </label>
        <input
          className="h-12 p-5 block rounded-xl w-[23rem] mt-1 bg-gray focus:outline-none focus:ring-2 focus:ring-lightBlue"
          {...field}
          {...props}
          disabled={!edit}
        />
      </div>
    );
  };

  return (
    <Formik
      initialValues={{
        [medInfo.label]: medInfo.value,
      }}
      validationSchema={Yup.object({
        [medInfo.label]: Yup.string(),
      })}
      onSubmit={(values, { setSubmitting, resetForm }) => {
        setTimeout(() => {
          // Update DB
          alert(JSON.stringify(values, null, 2));
          setSubmitting(false);
        }, 400);
      }}
    >
      <Form>
        <TextInput label={medInfo.label} name={medInfo.label} type="text" />
        {edit ? (
          <button className="" onClick={() => setFunction(false)}>
            Save
          </button>
        ) : (
          ""
        )}
      </Form>
    </Formik>
  );
};

export default UpdateMedInfo;
