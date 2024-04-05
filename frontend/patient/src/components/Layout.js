import { Outlet } from "react-router-dom";
import SideMenu from "../features/SideMenu";
import Header from "../features/Header";

/**
 * Layout component that renders the main layout of the application.
 * It includes a SideMenu, Header, and an Outlet for nested routes.
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
