import { useNavigate } from "react-router-dom";
import type { User } from "../../types/user";

interface Props {
  user: User;
}

const name = (user: User) => `${user.first_name} ${user.last_name}`;

export default function ProfileCard({ user }: Props) {
  const navigate = useNavigate();
  return (
    <div className="p-8">
      <div className="flex flex-col items-center gap-8 md:flex-row">
        {/* Avatar */}
        <div className="relative">
          <img
            src={
              "https://ui-avatars.com/api/?name=" +
              name(user) +
              "&background=random"
            }
            alt={name(user)}
            className="h-40 w-40 rounded-full border-4 border-indigo-500 object-cover shadow-xl"
          />

          <span className="absolute bottom-3 right-3 h-5 w-5 rounded-full border-2 border-white bg-green-500"></span>
        </div>

        {/* User Info */}
        <div className="flex-1">
          <h2 className="text-3xl font-bold text-gray-800">
            {user.first_name} {user.last_name}
          </h2>

          <p className="mt-2 text-gray-500">{user.email}</p>

          <div className="mt-6 grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div className="rounded-xl bg-gray-50 p-4 shadow-sm">
              <p className="text-sm text-gray-500">Username</p>
              <p className="font-semibold">
                {user.first_name} {user.last_name}
              </p>
            </div>

            <div className="rounded-xl bg-gray-50 p-4 shadow-sm">
              <p className="text-sm text-gray-500">Email</p>
              <p className="font-semibold">{user.email}</p>
            </div>

            {/* <div className="rounded-xl bg-gray-50 p-4 shadow-sm">
              <p className="text-sm text-gray-500">Phone</p>
              <p className="font-semibold">{user.phone}</p>
            </div>

            <div className="rounded-xl bg-gray-50 p-4 shadow-sm">
              <p className="text-sm text-gray-500">Location</p>
              <p className="font-semibold">{user.location}</p>
            </div> */}
          </div>

          <div className="mt-8 flex gap-4">
            <button className="rounded-xl bg-indigo-600 px-6 py-3 font-semibold text-white transition hover:bg-indigo-700">
              Edit Profile
            </button>

            <button className="rounded-xl border border-gray-300 px-6 py-3 font-semibold transition hover:bg-gray-100">
              Change Password
            </button>
            <button
              onClick={() => navigate("/dashboard")}
              className="rounded-xl border border-gray-300 px-6 py-3 font-semibold transition hover:bg-gray-100"
            >
              ← Dashboard
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
