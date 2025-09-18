import { Server as SocketIOServer, Socket } from 'socket.io';
import { logger } from '../utils/logger';
import RedisService from './RedisService';

interface UserSocket extends Socket {
  userId?: string;
  projectId?: string;
}

class SocketService {
  private io: SocketIOServer;
  private connectedUsers: Map<string, UserSocket> = new Map();

  constructor(io: SocketIOServer) {
    this.io = io;
  }

  public initialize(): void {
    this.io.on('connection', (socket: UserSocket) => {
      logger.info(`User connected: ${socket.id}`);

      // Handle user authentication
      socket.on('authenticate', async (data: { userId: string, projectId: string }) => {
        try {
          socket.userId = data.userId;
          socket.projectId = data.projectId;
          
          // Join project room
          socket.join(data.projectId);
          
          // Store user connection
          this.connectedUsers.set(socket.id, socket);
          
          // Update collaboration session
          await this.updateCollaborationSession(data.userId, data.projectId, socket.id);
          
          // Notify others in the project
          socket.to(data.projectId).emit('user_joined', {
            userId: data.userId,
            socketId: socket.id,
            timestamp: new Date().toISOString()
          });

          logger.info(`User ${data.userId} authenticated and joined project ${data.projectId}`);
        } catch (error) {
          logger.error('Authentication error:', error);
          socket.emit('auth_error', { message: 'Authentication failed' });
        }
      });

      // Handle cursor position updates
      socket.on('cursor_update', async (data: { line: number, column: number }) => {
        if (socket.userId && socket.projectId) {
          // Update cursor position in Redis
          await RedisService.setCache(
            `cursor:${socket.userId}:${socket.projectId}`,
            { line: data.line, column: data.column },
            60 // 1 minute TTL
          );

          // Broadcast to other users in the project
          socket.to(socket.projectId).emit('cursor_update', {
            userId: socket.userId,
            position: data,
            timestamp: new Date().toISOString()
          });
        }
      });

      // Handle file changes
      socket.on('file_change', async (data: { fileId: string, content: string, changes: any }) => {
        if (socket.userId && socket.projectId) {
          // Broadcast to other users in the project
          socket.to(socket.projectId).emit('file_change', {
            fileId: data.fileId,
            content: data.content,
            changes: data.changes,
            userId: socket.userId,
            timestamp: new Date().toISOString()
          });
        }
      });

      // Handle chat messages
      socket.on('chat_message', async (data: { message: string, type?: string }) => {
        if (socket.userId && socket.projectId) {
          const messageData = {
            id: `msg_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
            userId: socket.userId,
            projectId: socket.projectId,
            content: data.message,
            type: data.type || 'user',
            timestamp: new Date().toISOString()
          };

          // Broadcast to all users in the project (including sender)
          this.io.to(socket.projectId).emit('chat_message', messageData);
        }
      });

      // Handle typing indicators
      socket.on('typing_start', () => {
        if (socket.userId && socket.projectId) {
          socket.to(socket.projectId).emit('typing_start', {
            userId: socket.userId,
            timestamp: new Date().toISOString()
          });
        }
      });

      socket.on('typing_stop', () => {
        if (socket.userId && socket.projectId) {
          socket.to(socket.projectId).emit('typing_stop', {
            userId: socket.userId,
            timestamp: new Date().toISOString()
          });
        }
      });

      // Handle disconnection
      socket.on('disconnect', async () => {
        logger.info(`User disconnected: ${socket.id}`);
        
        if (socket.userId && socket.projectId) {
          // Remove from collaboration session
          await this.removeCollaborationSession(socket.userId, socket.projectId);
          
          // Notify others in the project
          socket.to(socket.projectId).emit('user_left', {
            userId: socket.userId,
            socketId: socket.id,
            timestamp: new Date().toISOString()
          });
        }
        
        // Remove from connected users
        this.connectedUsers.delete(socket.id);
      });
    });

    logger.info('Socket.io service initialized');
  }

  private async updateCollaborationSession(userId: string, projectId: string, socketId: string): Promise<void> {
    try {
      // Store in Redis for quick access
      await RedisService.setCache(
        `collaboration:${userId}:${projectId}`,
        {
          socketId,
          lastSeen: new Date().toISOString(),
          isActive: true
        },
        3600 // 1 hour TTL
      );
    } catch (error) {
      logger.error('Error updating collaboration session:', error);
    }
  }

  private async removeCollaborationSession(userId: string, projectId: string): Promise<void> {
    try {
      await RedisService.deleteCache(`collaboration:${userId}:${projectId}`);
    } catch (error) {
      logger.error('Error removing collaboration session:', error);
    }
  }

  // Get connected users for a project
  public getConnectedUsers(projectId: string): string[] {
    const users: string[] = [];
    
    this.connectedUsers.forEach((socket) => {
      if (socket.projectId === projectId && socket.userId) {
        users.push(socket.userId);
      }
    });
    
    return [...new Set(users)]; // Remove duplicates
  }

  // Send notification to specific user
  public sendToUser(userId: string, event: string, data: any): void {
    this.connectedUsers.forEach((socket) => {
      if (socket.userId === userId) {
        socket.emit(event, data);
      }
    });
  }

  // Send notification to all users in a project
  public sendToProject(projectId: string, event: string, data: any): void {
    this.io.to(projectId).emit(event, data);
  }

  // Get server statistics
  public getStats(): { connectedUsers: number, totalSockets: number } {
    return {
      connectedUsers: new Set([...this.connectedUsers.values()].map(s => s.userId)).size,
      totalSockets: this.connectedUsers.size
    };
  }
}

export { SocketService };
