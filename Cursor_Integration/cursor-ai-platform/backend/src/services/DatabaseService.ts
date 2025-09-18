import { PrismaClient } from '@prisma/client';
import { logger } from '../utils/logger';

class DatabaseService {
  private static instance: DatabaseService;
  public prisma: PrismaClient;

  private constructor() {
    this.prisma = new PrismaClient({
      log: [
        {
          emit: 'event',
          level: 'query',
        },
        {
          emit: 'event',
          level: 'error',
        },
        {
          emit: 'event',
          level: 'info',
        },
        {
          emit: 'event',
          level: 'warn',
        },
      ],
    });

    // Log database queries in development
    if (process.env.NODE_ENV === 'development') {
      this.prisma.$on('query', (e) => {
        logger.debug(`Query: ${e.query}`);
        logger.debug(`Params: ${e.params}`);
        logger.debug(`Duration: ${e.duration}ms`);
      });
    }

    this.prisma.$on('error', (e) => {
      logger.error('Database error:', e);
    });

    this.prisma.$on('info', (e) => {
      logger.info('Database info:', e.message);
    });

    this.prisma.$on('warn', (e) => {
      logger.warn('Database warning:', e.message);
    });
  }

  public static getInstance(): DatabaseService {
    if (!DatabaseService.instance) {
      DatabaseService.instance = new DatabaseService();
    }
    return DatabaseService.instance;
  }

  public static async initialize(): Promise<void> {
    const instance = DatabaseService.getInstance();
    
    try {
      await instance.prisma.$connect();
      logger.info('✅ Database connected successfully');
      
      // Test the connection
      await instance.prisma.$queryRaw`SELECT 1`;
      logger.info('✅ Database health check passed');
    } catch (error) {
      logger.error('❌ Database connection failed:', error);
      throw error;
    }
  }

  public static async disconnect(): Promise<void> {
    const instance = DatabaseService.getInstance();
    await instance.prisma.$disconnect();
    logger.info('Database disconnected');
  }

  public static async healthCheck(): Promise<boolean> {
    try {
      const instance = DatabaseService.getInstance();
      await instance.prisma.$queryRaw`SELECT 1`;
      return true;
    } catch (error) {
      logger.error('Database health check failed:', error);
      return false;
    }
  }
}

export default DatabaseService;
