#!/bin/bash

# 🌊 DeepBlue Cursor AI Platform Setup Script 🚢
# "We need a bigger boat!"

set -e

echo "🌊 DeepBlue Cursor AI Platform Setup 🚢"
echo "=========================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if required tools are installed
check_requirements() {
    print_status "Checking requirements..."
    
    if ! command -v node &> /dev/null; then
        print_error "Node.js is not installed. Please install Node.js 18+"
        exit 1
    fi
    
    if ! command -v npm &> /dev/null; then
        print_error "npm is not installed. Please install npm"
        exit 1
    fi
    
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed. Please install Docker"
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose is not installed. Please install Docker Compose"
        exit 1
    fi
    
    print_success "All requirements are met"
}

# Setup environment files
setup_environment() {
    print_status "Setting up environment files..."
    
    # Backend environment
    if [ ! -f backend/.env ]; then
        cp backend/env.example backend/.env
        print_success "Created backend/.env from template"
        print_warning "Please update backend/.env with your actual configuration"
    else
        print_warning "backend/.env already exists, skipping..."
    fi
    
    # Frontend environment
    if [ ! -f frontend/.env.local ]; then
        cp frontend/env.example frontend/.env.local
        print_success "Created frontend/.env.local from template"
        print_warning "Please update frontend/.env.local with your actual configuration"
    else
        print_warning "frontend/.env.local already exists, skipping..."
    fi
    
    # Root environment
    if [ ! -f .env ]; then
        cp env.example .env
        print_success "Created .env from template"
        print_warning "Please update .env with your actual configuration"
    else
        print_warning ".env already exists, skipping..."
    fi
}

# Install dependencies
install_dependencies() {
    print_status "Installing dependencies..."
    
    # Root dependencies
    print_status "Installing root dependencies..."
    npm install
    
    # Frontend dependencies
    print_status "Installing frontend dependencies..."
    cd frontend && npm install && cd ..
    
    # Backend dependencies
    print_status "Installing backend dependencies..."
    cd backend && npm install && cd ..
    
    print_success "All dependencies installed"
}

# Setup database
setup_database() {
    print_status "Setting up database..."
    
    # Start database services
    print_status "Starting database services..."
    docker-compose up -d postgres redis
    
    # Wait for database to be ready
    print_status "Waiting for database to be ready..."
    sleep 10
    
    # Run database migrations
    print_status "Running database migrations..."
    cd backend && npx prisma migrate deploy && cd ..
    
    # Generate Prisma client
    print_status "Generating Prisma client..."
    cd backend && npx prisma generate && cd ..
    
    # Seed database
    print_status "Seeding database..."
    cd backend && npm run db:seed && cd ..
    
    print_success "Database setup complete"
}

# Build applications
build_applications() {
    print_status "Building applications..."
    
    # Build frontend
    print_status "Building frontend..."
    cd frontend && npm run build && cd ..
    
    # Build backend
    print_status "Building backend..."
    cd backend && npm run build && cd ..
    
    print_success "Applications built successfully"
}

# Run tests
run_tests() {
    print_status "Running tests..."
    
    # Frontend tests
    print_status "Running frontend tests..."
    cd frontend && npm run test -- --coverage --watchAll=false && cd ..
    
    # Backend tests
    print_status "Running backend tests..."
    cd backend && npm run test && cd ..
    
    print_success "All tests passed"
}

# Main setup function
main() {
    echo "🚢 Starting DeepBlue Cursor AI Platform setup..."
    echo ""
    
    check_requirements
    setup_environment
    install_dependencies
    setup_database
    build_applications
    run_tests
    
    echo ""
    echo "🌊 DeepBlue Cursor AI Platform setup complete! 🚢"
    echo ""
    echo "Next steps:"
    echo "1. Update environment files with your configuration"
    echo "2. Start the development environment:"
    echo "   npm run dev"
    echo "3. Or start with Docker:"
    echo "   npm run docker:up"
    echo ""
    echo "Access the application:"
    echo "- Frontend: http://localhost:3000"
    echo "- Backend API: http://localhost:8000"
    echo "- Health Check: http://localhost:8000/health"
    echo ""
    echo "Default admin credentials:"
    echo "- Email: admin@deepblue.ai"
    echo "- Password: admin123"
    echo ""
    echo "🌊 We found a bigger boat! 🚢"
}

# Run main function
main "$@"
