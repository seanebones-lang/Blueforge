import express from 'express'
import { createServer } from 'http'
import { Server as SocketIOServer } from 'socket.io'
import cors from 'cors'
import helmet from 'helmet'
import compression from 'compression'
import morgan from 'morgan'
import rateLimit from 'express-rate-limit'
import dotenv from 'dotenv'

// Import routes
import authRoutes from './routes/auth'
import projectRoutes from './routes/projects'
import fileRoutes from './routes/files'
import aiRoutes from './routes/ai'
import collaborationRoutes from './routes/collaboration'

// Import middleware
import { errorHandler } from './middleware/errorHandler'
import { authMiddleware } from './middleware/auth'
import { logger } from './utils/logger'

// Import services
import { SocketService } from './services/SocketService'
import { DatabaseService } from './services/DatabaseService'
import { RedisService } from './services/RedisService'

// Load environment variables
dotenv.config()

const app = express()
const server = createServer(app)
const io = new SocketIOServer(server, {
  cors: {
    origin: process.env.FRONTEND_URL || 'http://localhost:3000',
    methods: ['GET', 'POST'],
    credentials: true
  }
})

const PORT = process.env.PORT || 8000

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP, please try again later.'
})

// Middleware
app.use(helmet())
app.use(compression())
app.use(morgan('combined', { stream: { write: (message) => logger.info(message.trim()) } }))
app.use(limiter)
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:3000',
  credentials: true
}))
app.use(express.json({ limit: '10mb' }))
app.use(express.urlencoded({ extended: true, limit: '10mb' }))

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    memory: process.memoryUsage(),
    version: process.env.npm_package_version || '1.0.0'
  })
})

// API routes
app.use('/api/auth', authRoutes)
app.use('/api/projects', authMiddleware, projectRoutes)
app.use('/api/files', authMiddleware, fileRoutes)
app.use('/api/ai', authMiddleware, aiRoutes)
app.use('/api/collaboration', authMiddleware, collaborationRoutes)

// Socket.io connection handling
const socketService = new SocketService(io)
socketService.initialize()

// Error handling middleware (must be last)
app.use(errorHandler)

// 404 handler
app.use('*', (req, res) => {
  res.status(404).json({
    success: false,
    message: 'Route not found',
    path: req.originalUrl
  })
})

// Initialize services
async function initializeServices() {
  try {
    // Initialize database
    await DatabaseService.initialize()
    logger.info('Database initialized successfully')

    // Initialize Redis
    await RedisService.initialize()
    logger.info('Redis initialized successfully')

    // Start server
    server.listen(PORT, () => {
      logger.info(`🌊 DeepBlue Cursor AI Platform Backend running on port ${PORT}`)
      logger.info(`🚢 We need a bigger boat! 🚢`)
    })
  } catch (error) {
    logger.error('Failed to initialize services:', error)
    process.exit(1)
  }
}

// Graceful shutdown
process.on('SIGTERM', () => {
  logger.info('SIGTERM received, shutting down gracefully')
  server.close(() => {
    logger.info('Process terminated')
    process.exit(0)
  })
})

process.on('SIGINT', () => {
  logger.info('SIGINT received, shutting down gracefully')
  server.close(() => {
    logger.info('Process terminated')
    process.exit(0)
  })
})

// Start the server
initializeServices()
