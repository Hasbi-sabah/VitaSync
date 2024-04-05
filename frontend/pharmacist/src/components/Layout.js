import { Outlet } from "react-router-dom";
import SideMenu from "../features/SideMenu";
import Header from "../features/Header";

/**
 * Layout component provides the main structure for the application.
 * It includes a SideMenu, Header, and an Outlet for rendering child components.
 * This component uses Tailwind CSS for styling.
 * @returns {JSX.Element} The rendered Layout component, including the SideMenu, Header, and an Outlet for child components.
 */
const Layout = () => {
    return (
        <main className='App bg-gray min-h-screen flex'>
          <SideMenu />
          <Header />
          <section className='lg:ml-72 sm:ml-56 flex-grow'>
            <Outlet />
          </section>
        </main>
      );
}

export default Layout;
