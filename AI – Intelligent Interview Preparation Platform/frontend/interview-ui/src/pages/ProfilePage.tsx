import { useEffect, useState } from "react";
import { getProfile } from "../api/userApi";
import ProfileCard from "../components/profile/ProfileCard";
import type { User } from "../types/user";

export default function ProfilePage() {
  const [user, setUser] = useState<User>();

  useEffect(() => {
    loadProfile();
  }, []);

  async function loadProfile() {
    try {
      const response = await getProfile();
      setUser(response);
    } catch (error) {
      console.error(error);
    }
  }

  if (!user) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-indigo-100 via-white to-purple-100">
        <div className="text-center">
          <div className="mx-auto h-12 w-12 animate-spin rounded-full border-4 border-indigo-500 border-t-transparent"></div>
          <p className="mt-4 text-lg font-medium text-gray-600">
            Loading profile...
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-100 via-indigo-50 to-purple-100 py-10 px-4">
      <div className="mx-auto max-w-6xl">
        {/* Header */}
        <div className="mb-8 rounded-3xl bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-500 p-8 text-white shadow-2xl">
          <h1 className="text-4xl font-bold">My Profile</h1>
          <p className="mt-2 text-indigo-100">
            Manage your personal information and account settings.
          </p>
        </div>

        {/* Profile Card */}
        <div className="overflow-hidden rounded-3xl bg-white shadow-2xl ring-1 ring-gray-200">
          <ProfileCard user={user} />
        </div>
      </div>
    </div>
  );
}