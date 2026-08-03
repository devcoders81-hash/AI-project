import Sidebar from "../components/common/Sidebar";

import { Outlet } from "react-router-dom";

export default function DashboardLayout(){

    return(

        <div className="flex">

            <Sidebar/>

            <main className="flex-1 bg-slate-100 min-h-screen">

                <Outlet/>

            </main>

        </div>

    )

}