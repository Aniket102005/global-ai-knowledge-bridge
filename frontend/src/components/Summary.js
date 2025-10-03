import React from 'react';

function Summary({ pages }) {
  return (
    <div className="bg-gray-800 p-6 rounded-xl shadow-lg border border-cyan-500/30">
      <h2 className="text-3xl font-bold mb-4 text-cyan-400 border-b-2 border-gray-700 pb-2">
        Document Summaries
      </h2>
      <div className="space-y-4">
        {pages.map((page, index) => (
          <div key={index}>
            <h3 className="text-xl font-semibold text-cyan-300">Page {page.page}</h3>
            <p className="text-gray-300 whitespace-pre-wrap">{page.summary}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Summary;

