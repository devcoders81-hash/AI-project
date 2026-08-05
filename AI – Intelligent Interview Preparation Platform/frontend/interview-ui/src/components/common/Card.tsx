import type { ReactNode } from "react";

interface Props {
    title: string;
    value: string;
    icon?: ReactNode;
}

export default function Card({
    title,
    value,
    icon,
}: Props) {
    return (
        <div className="
            bg-white 
            rounded-2xl 
            shadow-md 
            p-6
            hover:shadow-lg
            transition
        ">
            <div className="
                flex 
                justify-between 
                items-center 
                text-indigo-600
                mb-4
            ">
                {icon}
            </div>

            <p className="text-gray-500 text-sm">
                {title}
            </p>

            <h2 className="
                text-4xl 
                font-bold 
                mt-3 
                text-slate-900
            ">
                {value}
            </h2>
        </div>
    );
}