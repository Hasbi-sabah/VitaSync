import React, { useState } from 'react';

const ToggleSwitch = () => {
  const [isChecked, setIsChecked] = useState(false);

  const handleToggle = () => {
    setIsChecked(!isChecked);
  };

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