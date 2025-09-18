import { Router } from 'express';
import { asyncHandler } from '../middleware/errorHandler';

const router = Router();

// Get active users in project
router.get('/:projectId/users', asyncHandler(async (req, res) => {
  res.json({
    success: true,
    message: 'Get active users endpoint - to be implemented',
    data: []
  });
}));

// Join collaboration session
router.post('/:projectId/join', asyncHandler(async (req, res) => {
  res.json({
    success: true,
    message: 'Join collaboration endpoint - to be implemented'
  });
}));

// Leave collaboration session
router.post('/:projectId/leave', asyncHandler(async (req, res) => {
  res.json({
    success: true,
    message: 'Leave collaboration endpoint - to be implemented'
  });
}));

export default router;
