import { createClient, RedisClientType } from 'redis';
import { logger } from '../utils/logger';

class RedisService {
  private static instance: RedisService;
  public client: RedisClientType;

  private constructor() {
    this.client = createClient({
      url: process.env.REDIS_URL || 'redis://localhost:6379',
      socket: {
        reconnectStrategy: (retries) => Math.min(retries * 50, 1000)
      }
    });

    this.client.on('error', (err) => {
      logger.error('Redis Client Error:', err);
    });

    this.client.on('connect', () => {
      logger.info('Redis client connected');
    });

    this.client.on('ready', () => {
      logger.info('Redis client ready');
    });

    this.client.on('end', () => {
      logger.info('Redis client disconnected');
    });
  }

  public static getInstance(): RedisService {
    if (!RedisService.instance) {
      RedisService.instance = new RedisService();
    }
    return RedisService.instance;
  }

  public static async initialize(): Promise<void> {
    const instance = RedisService.getInstance();
    
    try {
      await instance.client.connect();
      logger.info('✅ Redis connected successfully');
      
      // Test the connection
      await instance.client.ping();
      logger.info('✅ Redis health check passed');
    } catch (error) {
      logger.error('❌ Redis connection failed:', error);
      throw error;
    }
  }

  public static async disconnect(): Promise<void> {
    const instance = RedisService.getInstance();
    await instance.client.disconnect();
    logger.info('Redis disconnected');
  }

  public static async healthCheck(): Promise<boolean> {
    try {
      const instance = RedisService.getInstance();
      const result = await instance.client.ping();
      return result === 'PONG';
    } catch (error) {
      logger.error('Redis health check failed:', error);
      return false;
    }
  }

  // Session management
  public static async setSession(sessionId: string, data: any, ttl: number = 3600): Promise<void> {
    const instance = RedisService.getInstance();
    await instance.client.setEx(`session:${sessionId}`, ttl, JSON.stringify(data));
  }

  public static async getSession(sessionId: string): Promise<any> {
    const instance = RedisService.getInstance();
    const data = await instance.client.get(`session:${sessionId}`);
    return data ? JSON.parse(data) : null;
  }

  public static async deleteSession(sessionId: string): Promise<void> {
    const instance = RedisService.getInstance();
    await instance.client.del(`session:${sessionId}`);
  }

  // Cache management
  public static async setCache(key: string, data: any, ttl: number = 300): Promise<void> {
    const instance = RedisService.getInstance();
    await instance.client.setEx(`cache:${key}`, ttl, JSON.stringify(data));
  }

  public static async getCache(key: string): Promise<any> {
    const instance = RedisService.getInstance();
    const data = await instance.client.get(`cache:${key}`);
    return data ? JSON.parse(data) : null;
  }

  public static async deleteCache(key: string): Promise<void> {
    const instance = RedisService.getInstance();
    await instance.client.del(`cache:${key}`);
  }

  // AI response caching
  public static async setAIResponse(prompt: string, response: string, ttl: number = 3600): Promise<void> {
    const instance = RedisService.getInstance();
    const key = `ai:${Buffer.from(prompt).toString('base64')}`;
    await instance.client.setEx(key, ttl, response);
  }

  public static async getAIResponse(prompt: string): Promise<string | null> {
    const instance = RedisService.getInstance();
    const key = `ai:${Buffer.from(prompt).toString('base64')}`;
    return await instance.client.get(key);
  }
}

export default RedisService;
