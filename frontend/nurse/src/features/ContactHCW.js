import React, { useState, useEffect } from "react";
import ProfileCard from "../components/extra/ProfileCard";
import { useMediaQuery } from "react-responsive";
import { useGetHcwQuery } from './hcw/hcwApiSlice';

const ContactHCW = () => {
  const { data: hcwList } = useGetHcwQuery();
  console.log(hcwList);
  const [searchTerm, setSearchTerm] = useState("");

  const handleSumit = (event) => {
    event.preventDefault();
  };
  const [roleFilter, setRoleFilter] = useState("");
  const [specialityFilter, setSpecialityFilter] = useState("");
  const [availableRoles, setAvailableRoles] = useState([]);
  const [availableSpecialities, setAvailableSpecialities] = useState([]);

  useEffect(() => {
    if (hcwList) {
      setAvailableRoles([...new Set(hcwList.map(hcw => hcw.role))]);
      setAvailableSpecialities([...new Set(hcwList.map(hcw => hcw.speciality))]);
    }
  }, [hcwList]);

  const handleFilterChange = (event) => {
    const { name, value } = event.target;
    if (name === "roles") {
       setRoleFilter(value);
      if (hcwList) {
        setAvailableSpecialities([...new Set(hcwList.filter(hcw => hcw.role === value).map(hcw => hcw.speciality))]);
      }
    } else if (name === "speciality") {
       setSpecialityFilter(value);
      if (hcwList) {
        setAvailableRoles([...new Set(hcwList.filter(hcw => hcw.speciality === value).map(hcw => hcw.role))]);
      }
    }
    }
  
  const handleReset = (event) => {
    setRoleFilter("");
    setSpecialityFilter("")
      if (hcwList) {
      setAvailableSpecialities([...new Set(hcwList.map(hcw => hcw.speciality))]);
      setAvailableRoles([...new Set(hcwList.map(hcw => hcw.role))]);
    }
  };
  const isMobile = useMediaQuery({ maxWidth: 1000 });
  const isMeduim = useMediaQuery({ maxWidth: 1425 });
  if (hcwList) {
    return (
      <div className="bg-gray mt-16 pb-12 sm:mt-28 lg:mt-32">
        <h2 className="text-center text-2xl py-4 font-semibold">
          Find a healthcare worker
        </h2>
        <form onSubmit={handleSumit} className="flex justify-evenly">
          <select name="roles" onChange={handleFilterChange} className="min-w-48 min-h-12 text-center">
          <option className="text-s" value="">
              Role: All
            </option>
            {availableRoles.map((role) => (
              <option key={role} className="text-s" value={role}>
                {role}
              </option>
            ))}
          </select>
          <select name="speciality" onChange={handleFilterChange} className="min-w-48 text-center">
            <option className="text-s" value="">
              Speciality: All
            </option>
            {availableSpecialities.map((speciality) => (
              <option key={speciality} className="text-s" value={speciality}>
                {speciality}
              </option>
            ))}
          </select>
          <button
            className="bg-lightBlue text-white rounded-lg w-48 hover:bg-blue"
            onClick={handleReset}
            type="reset"
          >
            Reset Filters
          </button>
        </form>
        <div
          className={`grid ${
            isMobile ? "grid-cols-1" : isMeduim ? "grid-cols-2" : "grid-cols-3"
          } gap-4`}
        >
          {hcwList
           .filter(
              (hcwFilter) =>
                (roleFilter === "" || hcwFilter.role === roleFilter) &&
                (specialityFilter === "" || hcwFilter.speciality === specialityFilter)
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
  }
};

export default ContactHCW;
