import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Import our layout and page components
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import Batches from './pages/Batches';
import Marketplace from './pages/Marketplace'; // The import is here

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-slate-50 flex">
        {/* The Sidebar navigation stays fixed on the left */}
        <Sidebar />

        {/* The Main Content area dynamically changes based on the URL */}
        <main className="flex-1 ml-64 p-8 min-h-screen overflow-y-auto">
          <Routes>
            {/* Live Pages */}
            <Route path="/" element={<Dashboard />} />
            <Route path="/batches" element={<Batches />} />
            {/* Here is the missing route to link your new page! */}
            <Route path="/marketplace" element={<Marketplace />} />
            
            {/* Catch-all for modules we haven't built yet (Sensors, Analytics, etc.) */}
            <Route path="*" element={
              <div className="flex flex-col items-center justify-center h-[70vh] text-slate-400 animate-fadeIn">
                <span className="text-6xl block mb-4">🚧</span>
                <h2 className="text-2xl font-bold text-slate-600 mb-2">Module Under Construction</h2>
                <p className="text-sm">This interface segment is preparing for incoming components.</p>
              </div>
            } />
          </Routes>
          
        </main>
      </div>
    </Router>
  );
}

export default App;