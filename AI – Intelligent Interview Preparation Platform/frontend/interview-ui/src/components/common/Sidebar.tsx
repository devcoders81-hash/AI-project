import { Link, useLocation } from "react-router-dom";
import { LayoutDashboard, FileText, Users, Sparkles } from "lucide-react";

export default function Sidebar() {
    const location = useLocation();

    const menuItems = [
        {
            name: "Dashboard",
            path: "/dashboard",
            icon: LayoutDashboard,
        },
        {
            name: "Resume",
            path: "/resume",
            icon: FileText,
        },
        {
            name: "Interviews",
            path: "/interviews",
            icon: Users,
        },
        {
            name: "Profile",
            path: "/profile",
            icon: Users,
        },
    ];

    const getResume=() => {
        const resumeId = location.pathname.split("/")[3];
        return resumeId;
    }

    return (
        <aside className="w-72 min-h-screen bg-gradient-to-b from-slate-950 via-slate-900 to-slate-800 text-white shadow-xl">
            
            {/* Logo */}
            <div className="flex items-center gap-3 px-6 py-6 border-b border-slate-700">
                <div className="p-2 rounded-xl bg-indigo-600">
                    <Sparkles size={24} />
                </div>

                <h1 className="text-2xl font-bold tracking-wide">
                    AI Interview
                </h1>
            </div>


            {/* Navigation */}
            <nav className="mt-6 px-4 space-y-2">
                {menuItems.map((item) => {
                    if (item.name === "Resume") {
                        getResume();
                    }
                    const Icon = item.icon;
                    const active = location.pathname === item.path;

                    return (
                        <Link
                            key={item.path}
                            to={item.path}
                            className={`
                                flex items-center gap-4 px-5 py-3 rounded-xl
                                transition-all duration-300 group
                                ${
                                    active
                                    ? "bg-indigo-600 text-white shadow-lg shadow-indigo-500/30"
                                    : "text-slate-300 hover:bg-slate-800 hover:text-white"
                                }
                            `}
                        >
                            <Icon
                                size={22}
                                className={`
                                    transition-transform duration-300
                                    group-hover:scale-110
                                `}
                            />

                            <span className="font-medium">
                                {item.name}
                            </span>
                        </Link>
                    );
                })}
            </nav>


            {/* Footer */}
            <div className="absolute bottom-0 w-72 p-6 text-sm text-slate-400">
                © 2026 AI Interview
            </div>

        </aside>
    );
}