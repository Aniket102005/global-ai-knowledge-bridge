import React, { useState } from 'react';
import Upload from './components/Upload';
import Summary from './components/Summary';
import Chat from './components/Chat';

function App() {
  const [summaries, setSummaries] = useState([]);
  const [sessionId, setSessionId] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleReset = () => {
    setSummaries([]);
    setSessionId('');
    setError('');
    setIsLoading(false);
  };

  return (
    <div className="bg-gray-900 text-white min-h-screen font-sans">
      <div className="container mx-auto p-4 md:p-8">
        <header className="text-center mb-10">
          <h1 className="text-4xl md:text-5xl font-bold text-cyan-400">
            Global AI Knowledge Bridge 🌐
          </h1>
          <p className="text-gray-400 mt-2">
            Simplifying complex knowledge, in any language.
          </p>
        </header>

        <main>
          {isLoading && (
            <div className="flex justify-center items-center mt-10">
              <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-cyan-400"></div>
              <p className="ml-4 text-lg">The AI is working its magic...</p>
            </div>
          )}

          {error && (
            <div className="bg-red-900 border border-red-700 text-red-300 px-4 py-3 rounded-lg relative mt-6 max-w-3xl mx-auto" role="alert">
              <strong className="font-bold">Error: </strong>
              <span className="block sm:inline">{error}</span>
            </div>
          )}

          {!isLoading && !error && (
            <>
              {summaries.length === 0 ? (
                <Upload 
                  setSummaries={setSummaries}
                  setSessionId={setSessionId}
                  setError={setError}
                  setIsLoading={setIsLoading}
                />
              ) : (
                <div className="max-w-4xl mx-auto space-y-8">
                  <Summary pages={summaries} />
                  <Chat sessionId={sessionId} />
                  <div className="text-center mt-8">
                    <button 
                      onClick={handleReset}
                      className="bg-gray-700 text-white font-bold py-2 px-6 rounded-full hover:bg-gray-600 transition duration-300"
                    >
                      Upload Another Document
                    </button>
                  </div>
                </div>
              )}
            </>
          )}
        </main>
      </div>
    </div>
  );
}

export default App;

