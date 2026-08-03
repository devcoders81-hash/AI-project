import { Outlet } from "react-router-dom";

export default function AuthLayout() {
    return (
        <div className="min-h-screen bg-slate-100 flex justify-center items-center">
            <Outlet />
        </div>
    );
}