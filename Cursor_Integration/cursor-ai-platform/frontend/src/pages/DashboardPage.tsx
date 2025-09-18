import React from 'react';
import { useAuthStore } from '@stores/authStore';

export const DashboardPage: React.FC = () => {
  const { user } = useAuthStore();

  return (
    <div className="flex-1 p-8">
      <div className="max-w-6xl mx-auto">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-editor-text mb-2">
            Welcome back, {user?.firstName || user?.username}! 👋
          </h1>
          <p className="text-gray-400">
            Ready to build amazing things with AI assistance?
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          <div className="card">
            <div className="flex items-center mb-4">
              <div className="w-12 h-12 bg-primary-600 rounded-lg flex items-center justify-center mr-4">
                📁
              </div>
              <div>
                <h3 className="text-lg font-semibold text-editor-text">Projects</h3>
                <p className="text-gray-400 text-sm">Manage your code projects</p>
              </div>
            </div>
            <button className="btn-primary w-full">
              View Projects
            </button>
          </div>

          <div className="card">
            <div className="flex items-center mb-4">
              <div className="w-12 h-12 bg-green-600 rounded-lg flex items-center justify-center mr-4">
                🤖
              </div>
              <div>
                <h3 className="text-lg font-semibold text-editor-text">AI Assistant</h3>
                <p className="text-gray-400 text-sm">Get help with your code</p>
              </div>
            </div>
            <button className="btn-primary w-full">
              Open AI Chat
            </button>
          </div>

          <div className="card">
            <div className="flex items-center mb-4">
              <div className="w-12 h-12 bg-purple-600 rounded-lg flex items-center justify-center mr-4">
                👥
              </div>
              <div>
                <h3 className="text-lg font-semibold text-editor-text">Collaborate</h3>
                <p className="text-gray-400 text-sm">Work together in real-time</p>
              </div>
            </div>
            <button className="btn-primary w-full">
              Start Collaboration
            </button>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="card">
            <h3 className="text-lg font-semibold text-editor-text mb-4">Recent Projects</h3>
            <div className="space-y-3">
              <div className="flex items-center p-3 bg-gray-800 rounded-lg">
                <div className="w-8 h-8 bg-blue-600 rounded flex items-center justify-center mr-3">
                  📄
                </div>
                <div className="flex-1">
                  <p className="text-editor-text font-medium">Welcome to DeepBlue</p>
                  <p className="text-gray-400 text-sm">Last modified 2 hours ago</p>
                </div>
                <button className="text-primary-500 hover:text-primary-400">
                  Open
                </button>
              </div>
            </div>
          </div>

          <div className="card">
            <h3 className="text-lg font-semibold text-editor-text mb-4">Quick Actions</h3>
            <div className="space-y-3">
              <button className="w-full text-left p-3 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors">
                <div className="flex items-center">
                  <span className="mr-3">➕</span>
                  <span className="text-editor-text">Create New Project</span>
                </div>
              </button>
              <button className="w-full text-left p-3 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors">
                <div className="flex items-center">
                  <span className="mr-3">📁</span>
                  <span className="text-editor-text">Import Project</span>
                </div>
              </button>
              <button className="w-full text-left p-3 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors">
                <div className="flex items-center">
                  <span className="mr-3">🔗</span>
                  <span className="text-editor-text">Join Project</span>
                </div>
              </button>
            </div>
          </div>
        </div>

        <div className="mt-8 text-center text-gray-500">
          <p>🌊 DeepBlue Cursor AI Platform - "We need a bigger boat!" 🚢</p>
        </div>
      </div>
    </div>
  );
};
