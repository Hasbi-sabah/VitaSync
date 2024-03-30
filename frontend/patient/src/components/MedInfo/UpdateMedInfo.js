import { Formik, Form, useField } from "formik";

const label_style = "pl-2 text-l font-normal";

const UpdateMedInfo = ({ medInfo }) => {
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
          disabled={true}
        />
      </div>
    );
  };

  return (
    medInfo.value && <Formik
      initialValues={{
        [medInfo.label]: medInfo.value,
      }}
    >
      <Form>
        <TextInput label={medInfo.label} name={medInfo.label} type="text" />
      </Form>
    </Formik>
  );
};

export default UpdateMedInfo;
