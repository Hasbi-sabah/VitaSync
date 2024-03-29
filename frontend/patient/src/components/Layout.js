import { Outlet } from "react-router-dom";
import SideMenu from "../features/SideMenu";
import Header from "../features/Header";

const Layout = () => {
    return (
        <main className='App bg-gray min-h-screen flex'>
          <section className='relative lg:w-64 sm:w-56'>
            <SideMenu />
            <Header />
          </section>
          <section className='flex-grow'>
            <Outlet />
          </section>
        </main>
      );
}

export default Layout
