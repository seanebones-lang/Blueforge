-- 🌊 DeepBlue Cursor AI Platform Database Initialization 🚢
-- "We need a bigger boat!"

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS cursor_ai_db;

-- Use the database
\c cursor_ai_db;

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Create custom types
CREATE TYPE user_role AS ENUM ('owner', 'admin', 'member', 'viewer');
CREATE TYPE ai_model_type AS ENUM ('gpt-4', 'claude-3', 'ollama', 'groq');
CREATE TYPE message_type AS ENUM ('user', 'assistant', 'system');

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_projects_owner ON projects(owner_id);
CREATE INDEX IF NOT EXISTS idx_project_members_user ON project_members(user_id);
CREATE INDEX IF NOT EXISTS idx_project_members_project ON project_members(project_id);
CREATE INDEX IF NOT EXISTS idx_project_files_project ON project_files(project_id);
CREATE INDEX IF NOT EXISTS idx_project_files_path ON project_files(project_id, path);
CREATE INDEX IF NOT EXISTS idx_collaboration_sessions_project ON collaboration_sessions(project_id);
CREATE INDEX IF NOT EXISTS idx_collaboration_sessions_user ON collaboration_sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_ai_interactions_user ON ai_interactions(user_id);
CREATE INDEX IF NOT EXISTS idx_ai_interactions_project ON ai_interactions(project_id);
CREATE INDEX IF NOT EXISTS idx_ai_interactions_created_at ON ai_interactions(created_at);
CREATE INDEX IF NOT EXISTS idx_chat_messages_project ON chat_messages(project_id);
CREATE INDEX IF NOT EXISTS idx_chat_messages_user ON chat_messages(user_id);

-- Create full-text search indexes
CREATE INDEX IF NOT EXISTS idx_projects_search ON projects USING gin(to_tsvector('english', name || ' ' || COALESCE(description, '')));
CREATE INDEX IF NOT EXISTS idx_files_search ON project_files USING gin(to_tsvector('english', name || ' ' || content));

-- Create triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_projects_updated_at BEFORE UPDATE ON projects FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_project_files_updated_at BEFORE UPDATE ON project_files FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Create function to clean up inactive collaboration sessions
CREATE OR REPLACE FUNCTION cleanup_inactive_sessions()
RETURNS void AS $$
BEGIN
    UPDATE collaboration_sessions 
    SET is_active = false 
    WHERE last_seen < NOW() - INTERVAL '1 hour';
END;
$$ language 'plpgsql';

-- Create function to get project statistics
CREATE OR REPLACE FUNCTION get_project_stats(project_uuid UUID)
RETURNS TABLE(
    file_count BIGINT,
    total_size BIGINT,
    member_count BIGINT,
    last_activity TIMESTAMP
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        COUNT(pf.id) as file_count,
        COALESCE(SUM(pf.size), 0) as total_size,
        COUNT(DISTINCT pm.user_id) as member_count,
        MAX(GREATEST(pf.updated_at, cs.last_seen)) as last_activity
    FROM projects p
    LEFT JOIN project_files pf ON p.id = pf.project_id
    LEFT JOIN project_members pm ON p.id = pm.project_id
    LEFT JOIN collaboration_sessions cs ON p.id = cs.project_id
    WHERE p.id = project_uuid
    GROUP BY p.id;
END;
$$ language 'plpgsql';

-- Create function to search projects and files
CREATE OR REPLACE FUNCTION search_content(search_term TEXT, user_uuid UUID)
RETURNS TABLE(
    type TEXT,
    id UUID,
    name TEXT,
    content TEXT,
    rank REAL
) AS $$
BEGIN
    RETURN QUERY
    (
        -- Search projects
        SELECT 
            'project'::TEXT as type,
            p.id,
            p.name,
            COALESCE(p.description, '') as content,
            ts_rank(to_tsvector('english', p.name || ' ' || COALESCE(p.description, '')), plainto_tsquery('english', search_term)) as rank
        FROM projects p
        JOIN project_members pm ON p.id = pm.project_id
        WHERE pm.user_id = user_uuid
        AND to_tsvector('english', p.name || ' ' || COALESCE(p.description, '')) @@ plainto_tsquery('english', search_term)
        
        UNION ALL
        
        -- Search files
        SELECT 
            'file'::TEXT as type,
            pf.id,
            pf.name,
            pf.content,
            ts_rank(to_tsvector('english', pf.name || ' ' || pf.content), plainto_tsquery('english', search_term)) as rank
        FROM project_files pf
        JOIN projects p ON pf.project_id = p.id
        JOIN project_members pm ON p.id = pm.project_id
        WHERE pm.user_id = user_uuid
        AND to_tsvector('english', pf.name || ' ' || pf.content) @@ plainto_tsquery('english', search_term)
    )
    ORDER BY rank DESC;
END;
$$ language 'plpgsql';

-- Insert initial admin user (password: 'admin123' - change in production!)
INSERT INTO users (id, email, username, password, first_name, last_name, is_active)
VALUES (
    uuid_generate_v4(),
    'admin@deepblue.ai',
    'admin',
    '$2a$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', -- 'admin123'
    'DeepBlue',
    'Admin',
    true
) ON CONFLICT (email) DO NOTHING;

-- Create default project for admin
INSERT INTO projects (id, name, description, owner_id, is_public)
SELECT 
    uuid_generate_v4(),
    'Welcome to DeepBlue',
    'Your first project in the DeepBlue Cursor AI Platform',
    u.id,
    false
FROM users u 
WHERE u.email = 'admin@deepblue.ai'
ON CONFLICT DO NOTHING;

-- Add admin as member of their default project
INSERT INTO project_members (id, project_id, user_id, role)
SELECT 
    uuid_generate_v4(),
    p.id,
    u.id,
    'owner'::user_role
FROM projects p
JOIN users u ON p.owner_id = u.id
WHERE u.email = 'admin@deepblue.ai'
ON CONFLICT (project_id, user_id) DO NOTHING;

-- Create sample files for the default project
INSERT INTO project_files (id, project_id, name, path, content, file_type, size)
SELECT 
    uuid_generate_v4(),
    p.id,
    'README.md',
    '/README.md',
    '# Welcome to DeepBlue Cursor AI Platform 🚢

This is your first project! Here you can:

- Write and edit code with AI assistance
- Collaborate in real-time with team members
- Get intelligent code completions
- Debug with AI help
- Translate natural language to code

## Getting Started

1. Create a new file by clicking the + button
2. Start coding with AI assistance
3. Invite team members to collaborate
4. Use the AI chat for help

Happy coding! 🌊',
    'md',
    LENGTH('# Welcome to DeepBlue Cursor AI Platform 🚢

This is your first project! Here you can:

- Write and edit code with AI assistance
- Collaborate in real-time with team members
- Get intelligent code completions
- Debug with AI help
- Translate natural language to code

## Getting Started

1. Create a new file by clicking the + button
2. Start coding with AI assistance
3. Invite team members to collaborate
4. Use the AI chat for help

Happy coding! 🌊')
FROM projects p
JOIN users u ON p.owner_id = u.id
WHERE u.email = 'admin@deepblue.ai'
AND p.name = 'Welcome to DeepBlue'
ON CONFLICT (project_id, path) DO NOTHING;

-- Create a sample JavaScript file
INSERT INTO project_files (id, project_id, name, path, content, file_type, size)
SELECT 
    uuid_generate_v4(),
    p.id,
    'app.js',
    '/app.js',
    '// DeepBlue Cursor AI Platform - Sample App
console.log("🌊 Welcome to DeepBlue! 🚢");

// AI-powered code assistance example
function greetUser(name) {
    return `Hello, ${name}! Ready to code with AI assistance?`;
}

// Export for use in other files
module.exports = {
    greetUser
};',
    'js',
    LENGTH('// DeepBlue Cursor AI Platform - Sample App
console.log("🌊 Welcome to DeepBlue! 🚢");

// AI-powered code assistance example
function greetUser(name) {
    return `Hello, ${name}! Ready to code with AI assistance?`;
}

// Export for use in other files
module.exports = {
    greetUser
};')
FROM projects p
JOIN users u ON p.owner_id = u.id
WHERE u.email = 'admin@deepblue.ai'
AND p.name = 'Welcome to DeepBlue'
ON CONFLICT (project_id, path) DO NOTHING;

-- Grant permissions
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO cursor_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO cursor_user;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO cursor_user;

-- Success message
SELECT '🌊 DeepBlue Cursor AI Platform Database Initialized Successfully! 🚢' as message;
