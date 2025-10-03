import React, { useState } from 'react';
import axios from 'axios';

function Upload({ setSummaries, setSessionId, setError, setIsLoading }) {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    setError('');
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setError('Please select a file to upload.');
      return;
    }
    if (selectedFile.type !== 'application/pdf') {
      setError('Only PDF files are allowed.');
      return;
    }
    const formData = new FormData();
    formData.append('file', selectedFile);
    setIsLoading(true);
    setError('');
    try {
      const response = await axios.post('http://localhost:8000/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      if (response.data?.pages) {
        setSummaries(response.data.pages);
        setSessionId(response.data.session_id);
      } else {
        setError('Received an invalid response format from the API.');
      }
    } catch (err) {
      console.error("Upload failed:", err);
      setError('Upload failed. Please ensure the backend is running and check the console.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto bg-gray-800 p-8 rounded-xl shadow-lg border border-cyan-500/30">
      <h2 className="text-2xl font-semibold mb-4 text-center">Upload a Document</h2>
      <p className="text-gray-400 text-center mb-6">
        Select a PDF file to summarize and ask questions.
      </p>
      <div className="flex flex-col items-center">
        <input
          type="file"
          accept=".pdf"
          onChange={handleFileChange}
          className="mb-4 text-sm text-gray-400 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-cyan-700 file:text-cyan-100 hover:file:bg-cyan-600"
        />
        <button
          onClick={handleUpload}
          disabled={!selectedFile}
          className="bg-cyan-600 text-white font-bold py-3 px-8 rounded-full hover:bg-cyan-500 transition duration-300 ease-in-out shadow-lg shadow-cyan-500/20 disabled:bg-gray-600 disabled:cursor-not-allowed"
        >
          Generate Summary
        </button>
      </div>
    </div>
  );
}

export default Upload;

