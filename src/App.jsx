import React from "react";
import Caa_page from "./components/Caa_page";

const App = () => {
  return (
    <>
      <div className="min-h-screen bg-gray-100 flex flex-col items-center">
        <header className="w-full bg-white shadow-md">
          <nav className="container mx-auto flex items-center justify-between py-4 px-6">
            <div className="text-xl font-bold">Spam Analyser</div>
            <button className="bg-gray-800 text-white px-4 py-2 rounded-md">
              Shibam Chakraborty
            </button>
          </nav>
        </header>

        <main className="flex-grow flex flex-col items-center justify-center px-6">
          <h1 className="text-4xl font-bold text-center text-gray-800 leading-tight mb-4">
            CAA: Strengthening <br /> Web Security, Preventing Data Breaches
          </h1>
          <p className="text-gray-600 text-center max-w-xl mb-8">
            Learn how the Certificate Authority Authorization (CAA) helps
            protect your website from unauthorized certificate issuers. This
            comprehensive guide explains the CAA's role in ensuring that only
            trusted Certificate Authorities (CAs) can issue certificates for
            your domain. By implementing CAA, you can enhance the security of
            your website, mitigate risks of data breaches, and ensure that your
            users' information remains protected. Stay ahead of cyber threats
            and boost your web security knowledge today!
          </p>
          <button className="bg-red-500 text-white px-6 py-3 rounded-md shadow-md hover:bg-red-600">
            User Guidelines
          </button>
        </main>
      </div>
      <Caa_page />
    </>
  );
};

export default App;
