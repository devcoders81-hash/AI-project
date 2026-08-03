import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../api/authApi";
import { useAuthStore } from "../store/authStore";

export default function Login() {


    const navigate = useNavigate();

    const [email,setEmail]=useState("");

    const [password,setPassword]=useState("");

    const [loading,setLoading]=useState(false);

    const handleLogin=async()=>{

        try{

            setLoading(true);

            const response=await login({

                email,

                password,

            });

            useAuthStore.getState().setToken(
                response.access_token,
            );

            localStorage.setItem(
                "token",
                response.access_token,
            );

            navigate("/dashboard");

        }

        catch(error){

            console.log(error);

            alert("Invalid Credentials");

        }

        finally{

            setLoading(false);

        }

    }

    return (
        <div className="bg-white rounded-xl shadow-lg p-8 w-[420px]">

            <h1 className="text-3xl font-bold text-center mb-8">
                Login
            </h1>

            {/* Email */}

            <div className="mb-5">

                <label
                    htmlFor="email"
                    className="block text-sm font-medium mb-2"
                >
                    Email Address
                </label>

                <input
                    id="email"
                    type="email"
                    placeholder="Enter your email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="w-full border border-gray-300 rounded-lg px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                />

            </div>

            {/* Password */}

            <div className="mb-8">

                <label
                    htmlFor="password"
                    className="block text-sm font-medium mb-2"
                >
                    Password
                </label>

                <input
                    id="password"
                    type="password"
                    placeholder="Enter your password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="w-full border border-gray-300 rounded-lg px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                />

            </div>

            <button onClick={handleLogin} disabled={loading}
                className="w-full bg-blue-600 hover:bg-blue-700 text-white rounded-lg py-3 font-semibold transition"
            >
                {

                loading

                ?

                "Logging in..."

                :

                "Login"

                }
            </button>

        </div>
    );
}