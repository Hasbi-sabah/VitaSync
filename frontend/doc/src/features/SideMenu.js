import MediaQuery, { useMediaQuery } from "react-responsive";
import MenuItem from "../components/MenuItem";
import { useState } from "react";

const SideMenu = () => {
  const [toggle, setToggle] = useState(false);
  const isMobile = useMediaQuery({maxWidth:640});
  return (
    <div>
        {isMobile && (
          <span 
            onClick={() => setToggle(!toggle)} className="text-black text-3xl flex pl-6 pt-2 h-14 fixed z-[55]"
          >
            &#x2630;
          </span>
        )}
      {(toggle && isMobile) && (
        <div className="sm:w-64 w-20 bg-blue fixed left-0 top-14 sm:top-0 h-screen sm:pt-[10vh] z-50 sm:z-40">
          <MenuItem label="dashboard"/>
          <MenuItem label="patients"/>
          <MenuItem label="records"/>
          <MenuItem label="logout"/>
      </div>
      )}
      {!isMobile && <div className="sm:w-64 w-20 bg-blue fixed left-0 top-14 sm:top-0 h-screen sm:pt-[10vh] z-50 sm:z-40">
          <MenuItem label="dashboard"/>
          <MenuItem label="patients"/>
          <MenuItem label="records"/>
          <MenuItem label="logout"/>
      </div>
      }
    </div>
  )
}

export default SideMenu;
