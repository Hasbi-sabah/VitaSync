/**
 * Imports the Link component from react-router-dom for navigation.
 * @module Public
 */
import { Link } from "react-router-dom";

/**
 * Renders the public component with a header, main content, and footer.
 * @function
 * @returns {JSX.Element} The JSX element representing the public component.
 */
const Public = () => {
    /**
     * The JSX structure for the public component.
     * @constant
     * @type {JSX.Element}
     */
    const dummy = (
        <section className="m-0 p-0 relative bg-gray">
            <header className="fixed top-0 left-0 h-20 w-full items-center flex bg-lightBlue text-white">
                <span className="ml-auto pr-10 text-lg">
                    <Link to="/login">Login</Link>
                </span>
            </header>
            <main className="pt-20">
                <section className="h-[80vh] bg-white"></section>
            </main>
            <footer className="absolute h-20 bottom-0 left-0 text-white w-full bg-lightBlue">
                <span>Footer</span>
            </footer>
        </section>
    );
    return dummy;
};

/**
 * Exports the Public component.
 * @exports Public
 */
export default Public;
