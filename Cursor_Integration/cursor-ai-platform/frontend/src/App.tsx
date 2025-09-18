import { Routes, Route } from 'react-router-dom'
import { useAuthStore } from '@stores/authStore'
import { useEffect } from 'react'
import { Layout } from '@components/Layout'
import { LoginPage } from '@pages/LoginPage'
import { DashboardPage } from '@pages/DashboardPage'
import { ProjectPage } from '@pages/ProjectPage'
import { SettingsPage } from '@pages/SettingsPage'
import { LoadingSpinner } from '@components/ui/LoadingSpinner'

function App() {
  const { user, isLoading, checkAuth } = useAuthStore()

  useEffect(() => {
    checkAuth()
  }, [checkAuth])

  if (isLoading) {
    return (
      <div className="min-h-screen bg-editor-bg flex items-center justify-center">
        <LoadingSpinner size="lg" />
      </div>
    )
  }

  if (!user) {
    return <LoginPage />
  }

  return (
    <Layout>
      <Routes>
        <Route path="/" element={<DashboardPage />} />
        <Route path="/project/:id" element={<ProjectPage />} />
        <Route path="/settings" element={<SettingsPage />} />
      </Routes>
    </Layout>
  )
}

export default App
