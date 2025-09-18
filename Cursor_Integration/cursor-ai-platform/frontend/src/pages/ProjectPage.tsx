import React from 'react';
import { useParams } from 'react-router-dom';

export const ProjectPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();

  return (
    <div className="flex-1 flex">
      {/* File Explorer */}
      <div className="w-64 bg-editor-surface border-r border-editor-border">
        <div className="p-4">
          <h3 className="text-lg font-semibold text-editor-text mb-4">Project Files</h3>
          <div className="space-y-2">
            <div className="flex items-center p-2 hover:bg-gray-700 rounded cursor-pointer">
              <span className="mr-2">📁</span>
              <span className="text-editor-text">src</span>
            </div>
            <div className="flex items-center p-2 hover:bg-gray-700 rounded cursor-pointer">
              <span className="mr-2">📄</span>
              <span className="text-editor-text">package.json</span>
            </div>
            <div className="flex items-center p-2 hover:bg-gray-700 rounded cursor-pointer">
              <span className="mr-2">📄</span>
              <span className="text-editor-text">README.md</span>
            </div>
          </div>
        </div>
      </div>

      {/* Code Editor Area */}
      <div className="flex-1 flex flex-col">
        <div className="h-12 bg-editor-surface border-b border-editor-border flex items-center px-4">
          <span className="text-editor-text">Project: {id}</span>
        </div>
        
        <div className="flex-1 flex">
          {/* Editor */}
          <div className="flex-1 bg-editor-bg">
            <div className="h-full flex items-center justify-center">
              <div className="text-center">
                <h2 className="text-2xl font-bold text-editor-text mb-4">
                  🚧 Code Editor Coming Soon
                </h2>
                <p className="text-gray-400">
                  Monaco Editor integration will be implemented here
                </p>
              </div>
            </div>
          </div>

          {/* AI Chat Panel */}
          <div className="w-80 bg-editor-surface border-l border-editor-border">
            <div className="h-full flex flex-col">
              <div className="p-4 border-b border-editor-border">
                <h3 className="text-lg font-semibold text-editor-text">🤖 AI Assistant</h3>
              </div>
              
              <div className="flex-1 p-4">
                <div className="text-center text-gray-400">
                  <p>AI chat interface will be implemented here</p>
                </div>
              </div>
              
              <div className="p-4 border-t border-editor-border">
                <div className="flex space-x-2">
                  <input
                    type="text"
                    placeholder="Ask AI for help..."
                    className="flex-1 input-primary"
                    disabled
                  />
                  <button className="btn-primary" disabled>
                    Send
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
