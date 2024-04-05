import React from "react";

/**
 * Component to display a profile card with contact information.
 * 
 * @param name - The name of the profile owner.
 * @param speciality - The specialty of the profile owner.
 * @param workNumber - The work phone number of the profile owner.
 * @param workAddress - The work address of the profile owner.
 * @returns The JSX element representing the component.
 */
const ProfileCard = ({ name, speciality, workNumber, workAddress }) => {
  /**
   * Handles the click event for the work phone number.
   * It redirects the user to the phone dialer with the work number pre-filled.
   */
    const handlePhoneClick = () => {
        window.location.href = `tel:${workNumber}`;
    };

  /**
   * Handles the click event for the work address.
   * It opens a new tab with Google Maps showing the work address.
   */
    const handleAddressClick = () => {
        window.open(`https://www.google.com/maps?q=${encodeURIComponent(workAddress)}`);
    }
  return (
    <div className="rounded-xl bg-white shadow-md h-56 w-[22rem] my-10 p-4 mx-auto">
      <h3 className="text-center text-3xl py-2 font-semibold">{name}</h3>
      <span className="text-center block text-">{speciality}</span>
      <br />
      <div>
        <div className="mb-4">
          <a href={`tel:${workNumber}`} onClick={handlePhoneClick} className="hover:text-actualLightBlue">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                fill="#000000"
                viewBox="0 0 256 256"
                className="inline mr-2"
              >
                <path d="M222.37,158.46l-47.11-21.11-.13-.06a16,16,0,0,0-15.17,1.4,8.12,8.12,0,0,0-.75.56L134.87,160c-15.42-7.49-31.34-23.29-38.83-38.51l20.78-24.71c.2-.25.39-.5.57-.77a16,16,0,0,0,1.32-15.06l0-.12L97.54,33.64a16,16,0,0,0-16.62-9.52A56.26,56.26,0,0,0,32,80c0,79.4,64.6,144,144,144a56.26,56.26,0,0,0,55.88-48.92A16,16,0,0,0,222.37,158.46ZM176,208A128.14,128.14,0,0,1,48,80,40.2,40.2,0,0,1,82.87,40a.61.61,0,0,0,0,.12l21,47L83.2,111.86a6.13,6.13,0,0,0-.57.77,16,16,0,0,0-1,15.7c9.06,18.53,27.73,37.06,46.46,46.11a16,16,0,0,0,15.75-1.14,8.44,8.44,0,0,0,.74-.56L168.89,152l47,21.05h0s.08,0,.11,0A40.21,40.21,0,0,1,176,208Z"></path>
              </svg>
              <span className="text-left text-lg">{workNumber}</span>
          </a>
        </div>
        <div>
          <a href="#" onClick={handleAddressClick} className="hover:text-actualLightBlue">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                fill="#000000"
                viewBox="0 0 256 256"
                className="inline mr-2"
              >
                <path d="M128,64a40,40,0,1,0,40,40A40,40,0,0,0,128,64Zm0,64a24,24,0,1,1,24-24A24,24,0,0,1,128,128Zm0-112a88.1,88.1,0,0,0-88,88c0,31.4,14.51,64.68,42,96.25a254.19,254.19,0,0,0,41.45,38.3,8,8,0,0,0,9.18,0A254.19,254.19,0,0,0,174,200.25c27.45-31.57,42-64.85,42-96.25A88.1,88.1,0,0,0,128,16Zm0,206c-16.53-13-72-60.75-72-118a72,72,0,0,1,144,0C200,161.23,144.53,209,128,222Z"></path>
              </svg>
              <span className="text-left text-sm">{workAddress}</span>
          </a>
        </div>
        <br />
      </div>
    </div>
  );
};

export default ProfileCard;
