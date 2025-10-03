import React, { useState } from 'react';
import axios from 'axios';

function Chat({ sessionId }) {
  const [query, setQuery] = useState('');
  const [language, setLanguage] = useState('English');
  const [answer, setAnswer] = useState('');
  const [isAsking, setIsAsking] = useState(false);
  const [chatError, setChatError] = useState('');

  const handleAsk = async () => {
    if (!query.trim()) {
      setChatError('Please enter a question.');
      return;
    }
    setIsAsking(true);
    setChatError('');
    setAnswer('');
    try {
      const response = await axios.post('http://localhost:8000/ask', {
        session_id: sessionId,
        query: query,
        language: language,
      });
      if (response.data?.answer) {
        setAnswer(response.data.answer);
      } else {
        setChatError('Received an invalid response from the Q&A API.');
      }
    } catch (err) {
      console.error("Ask failed:", err);
      setChatError('Failed to get an answer. Please try again.');
    } finally {
      setIsAsking(false);
    }
  };

  return (
    <div className="bg-gray-800 p-6 rounded-xl shadow-lg border border-cyan-500/30">
      <h2 className="text-3xl font-bold mb-4 text-cyan-400 border-b-2 border-gray-700 pb-2">Ask a Question</h2>
      <div className="space-y-4">
        <textarea
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask a question about the document in any language..."
          className="w-full p-3 bg-gray-700 rounded-md text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-cyan-500"
          rows="3"
        />
        <div className="flex items-center space-x-4">
          <select value={language} onChange={(e) => setLanguage(e.target.value)} className="p-3 bg-gray-700 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-cyan-500">
            <option>English</option>
            <option>Hindi</option>
            <option>Spanish</option>
            <option>French</option>
          </select>
          <button onClick={handleAsk} disabled={isAsking} className="flex-grow bg-cyan-600 text-white font-bold py-3 px-8 rounded-full hover:bg-cyan-500 transition duration-300 disabled:bg-gray-600">
            {isAsking ? 'Thinking...' : 'Get Answer'}
          </button>
        </div>
      </div>
      {chatError && <p className="text-red-400 mt-4">{chatError}</p>}
      {answer && (
        <div className="mt-6 bg-gray-900 p-4 rounded-lg">
          <h3 className="text-xl font-semibold text-cyan-500 mb-2">Answer:</h3>
          <p className="text-gray-300 whitespace-pre-wrap">{answer}</p>
        </div>
      )}
    </div>
  );
}

export default Chat;

