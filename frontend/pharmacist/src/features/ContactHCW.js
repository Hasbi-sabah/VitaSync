import React, { useState } from "react";
import ProfileCard from "../components/extra/ProfileCard";
import { useMediaQuery } from "react-responsive";

const ContactHCW = () => {
  const dummyData = [
    {
      firstName: "Yassine",
      lastName: "Rakibi",
      speciality: "UndeadSlayer",
      workNumber: "555-555-555",
      workAddress: "Unholy studios Inc. Uranus Planet Branch",
      userId: "123",
    },
    {
      firstName: "Sabah",
      lastName: "Hasbi",
      speciality: "UndeadTamer",
      workNumber: "444-444-444",
      workAddress: "Unholy studios Inc. Venues Planet Branch",
      userId: "1234",
    },
    {
      firstName: "Williams",
      lastName: "Akanni",
      speciality: "UndeadSummoner",
      workNumber: "333-333-333",
      workAddress: "Unholy studios Inc. Mars Planet Branch",
      userId: "12345",
    },
  ];
  const [searchTerm, setSearchTerm] = useState("");
  const handleChange = (event) => {
    setSearchTerm(event.target.value);
  };
  const handleSumit = (event) => {
    event.preventDefault();
  };
  const [filterValue, setFilterValue] = useState("");
  const handleFilterChange = (event) => setFilterValue(event.target.value);
  const isMobile = useMediaQuery({ maxWidth: 1000 });
  const isMeduim = useMediaQuery({ maxWidth: 1425 });
  return (
    <div className="bg-gray mt-16 pb-12 sm:mt-28 lg:mt-32">
      <h2 className="text-center text-2xl py-4 font-semibold">
        Find a healthcare worker
      </h2>
      <form onSubmit={handleSumit} className="flex justify-evenly">
        <input
          type="search"
          placeholder="hcw..."
          value={searchTerm}
          onChange={handleChange}
          className="p-2 text-base"
        />
        <select name="roles" onChange={handleFilterChange} className="">
          <option className="text-xs" value="">
            role
          </option>
          <option className="text-xs" value="Doctor">
            Doctor
          </option>
          <option className="text-xs" value="nurse">
            Nurse
          </option>
        </select>
        <button
          className="bg-lightBlue text-white rounded-lg w-20 hover:bg-blue"
          type="submit"
        >
          Search
        </button>
      </form>
      <div
        className={`grid ${
          isMobile ? "grid-cols-1" : isMeduim ? "grid-cols-2" : "grid-cols-3"
        } gap-4`}
      >
        {dummyData
          .filter(
            (hcwFilter) =>
              filterValue === "" || hcwFilter.speciality === filterValue
          )
          .map((hcw) => (
            <div key={hcw.userId}>
              <ProfileCard
                name={`${hcw.firstName} ${hcw.lastName}`}
                speciality={hcw.speciality}
                workNumber={hcw.workNumber}
                workAddress={hcw.workAddress}
              />
            </div>
          ))}
      </div>
    </div>
  );
};

export default ContactHCW;
