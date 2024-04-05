import { Outlet } from "react-router-dom";
import SideMenu from "../features/SideMenu";
import Header from "../features/Header";

/**
 * Layout Component
 * @returns Main layout component.
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

export default Layout
