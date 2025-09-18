import React from 'react';

interface LayoutProps {
  children: React.ReactNode;
}

export const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="min-h-screen bg-editor-bg text-editor-text">
      <div className="flex h-screen">
        {/* Sidebar */}
        <aside className="w-64 bg-editor-surface border-r border-editor-border">
          <div className="p-4">
            <h1 className="text-xl font-bold text-primary-500">
              🌊 DeepBlue 🚢
            </h1>
            <p className="text-sm text-gray-400">
              Cursor AI Platform
            </p>
          </div>
          
          {/* Navigation will go here */}
          <nav className="p-4">
            <div className="space-y-2">
              <button className="w-full text-left px-3 py-2 rounded-md hover:bg-gray-700 transition-colors">
                📁 Projects
              </button>
              <button className="w-full text-left px-3 py-2 rounded-md hover:bg-gray-700 transition-colors">
                ⚙️ Settings
              </button>
            </div>
          </nav>
        </aside>

        {/* Main Content */}
        <main className="flex-1 flex flex-col">
          {children}
        </main>
      </div>
    </div>
  );
};
