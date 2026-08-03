import { Link } from "react-router-dom";

export default function Sidebar() {

    return (

        <aside className="w-64 bg-slate-900 text-white h-screen">

            <div className="text-2xl font-bold p-6">

                AI Interview

            </div>

            <nav>

                <Link

                    className="block px-6 py-4 hover:bg-slate-800"

                    to="/dashboard"

                >

                    Dashboard

                </Link>

                <Link

                    className="block px-6 py-4 hover:bg-slate-800"

                    to="/resume"

                >

                    Resume

                </Link>

                <Link

                    className="block px-6 py-4 hover:bg-slate-800"

                    to="/interviews"

                >

                    Interviews

                </Link>

            </nav>

        </aside>

    );

}