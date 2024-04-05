import React, { useState } from 'react';

/**
 * ToggleSwitch component provides a custom toggle switch UI.
 * This component uses React's useState hook to manage the toggle state.
 * @returns {JSX.Element} The rendered ToggleSwitch component.
 */
const ToggleSwitch = () => {
  /**
    * State to track the toggle switch's checked state.
    * Initialized to false, indicating the switch is off by default.
    */
  const [isChecked, setIsChecked] = useState(false);

  /**
    * Handler function to toggle the checked state of the switch.
    * This function is called when the switch is clicked.
    */
  const handleToggle = () => {
    setIsChecked(!isChecked);
  };

  /**
    * Render the ToggleSwitch component.
    * It includes a label, an input of type checkbox, and two divs for styling the switch.
    * The checked state of the input and the styling of the switch are controlled by the isChecked state.
    */
  return (
    <label className="flex items-center cursor-pointer">
      <div className="relative">
        <input
          type="checkbox"
          checked={isChecked}
          onChange={handleToggle}
          className="sr-only"
        />
        <div className="toggle-switch-toggle-line w-10 h-4 bg-gray rounded-full shadow-inner"></div>
        <div className={`toggle-switch-toggle-dot absolute w-6 h-6 rounded-full shadow top-0 left-0 ${isChecked ? 'transform translate-x-full bg-actualLightBlue' : 'bg-red'}`}></div>
      </div>
    </label>
  );
};

export default ToggleSwitch;
