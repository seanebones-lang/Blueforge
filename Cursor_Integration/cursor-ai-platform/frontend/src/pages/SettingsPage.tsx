import React from 'react';

export const SettingsPage: React.FC = () => {
  return (
    <div className="flex-1 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-editor-text mb-8">Settings</h1>
        
        <div className="space-y-8">
          {/* User Profile */}
          <div className="card">
            <h2 className="text-xl font-semibold text-editor-text mb-4">Profile</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  Username
                </label>
                <input
                  type="text"
                  className="input-primary w-full"
                  placeholder="Your username"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  Email
                </label>
                <input
                  type="email"
                  className="input-primary w-full"
                  placeholder="Your email"
                />
              </div>
              <button className="btn-primary">
                Save Changes
              </button>
            </div>
          </div>

          {/* AI Settings */}
          <div className="card">
            <h2 className="text-xl font-semibold text-editor-text mb-4">AI Preferences</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  Default AI Model
                </label>
                <select className="input-primary w-full">
                  <option value="gpt-4">GPT-4</option>
                  <option value="claude-3">Claude 3</option>
                  <option value="ollama">Ollama (Local)</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  Code Completion
                </label>
                <div className="space-y-2">
                  <label className="flex items-center">
                    <input type="checkbox" className="mr-2" defaultChecked />
                    <span className="text-editor-text">Enable AI code completion</span>
                  </label>
                  <label className="flex items-center">
                    <input type="checkbox" className="mr-2" defaultChecked />
                    <span className="text-editor-text">Enable inline suggestions</span>
                  </label>
                </div>
              </div>
            </div>
          </div>

          {/* Editor Settings */}
          <div className="card">
            <h2 className="text-xl font-semibold text-editor-text mb-4">Editor</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  Theme
                </label>
                <select className="input-primary w-full">
                  <option value="dark">Dark</option>
                  <option value="light">Light</option>
                  <option value="auto">Auto</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  Font Size
                </label>
                <input
                  type="range"
                  min="12"
                  max="24"
                  defaultValue="14"
                  className="w-full"
                />
              </div>
            </div>
          </div>

          {/* Danger Zone */}
          <div className="card border-red-500">
            <h2 className="text-xl font-semibold text-red-400 mb-4">Danger Zone</h2>
            <div className="space-y-4">
              <button className="btn-secondary border-red-500 text-red-400 hover:bg-red-900/20">
                Delete Account
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
