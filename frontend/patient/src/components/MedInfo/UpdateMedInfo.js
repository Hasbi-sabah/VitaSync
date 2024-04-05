import { Formik, Form, useField } from "formik";
import React, { useState } from "react";
import { useAddPatientMedInfoByIdMutation } from '../../features/medInfo/medInfoApiSlice';
import * as Yup from "yup";

const label_style = "pl-2 text-l font-normal";
/**
 * Component for updating medical information of a patient.
 * @param edit - Flag indicating whether the component is in edit mode.
 * @param setFunction - Function to set the state of the edit mode.
 * @param medInfo - Object containing the medical information.
 * @param userId - The ID of the user.
 * @returns - The JSX element representing the component.
 */
const UpdateMedInfo = ({ edit, setFunction, medInfo, userId }) => {
  //API call
  const [addPatientMedInfoByIdMutation, { data: responseData, loading, error }] = useAddPatientMedInfoByIdMutation();
  
  // Custom input field component
  const TextInput = ({ label, ...props }) => {
    const [field] = useField(props);
    return (
      <div className="">
        <label className={`${label_style}`} htmlFor={props.id || props.name}>
          {label}
        </label>
        <input
          className="h-12 p-5 block rounded-xl w-full sm:w-[23rem] mt-1 bg-gray focus:outline-none focus:ring-2 focus:ring-lightBlue"
          {...field}
          {...props}
          disabled={!edit}
          placeholder='None'
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
    >
      <Form>
        <TextInput label={medInfo.attr} name={medInfo.label} type="text" />
      </Form>
    </Formik>
  );
};

export default UpdateMedInfo;
