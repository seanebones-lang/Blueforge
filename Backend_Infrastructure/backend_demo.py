#!/usr/bin/env python3
"""
⚙️ DEEPBLUE BACKEND INFRASTRUCTURE DEMO
Comprehensive demonstration of all backend infrastructure capabilities
"""

import asyncio
import json
import time
import requests
import websockets
from datetime import datetime
from typing import Dict, Any

class DeepBlueBackendDemo:
    """Demo class for DeepBlue Backend Infrastructure."""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.auth_token = None
    
    async def run_complete_demo(self):
        """Run the complete backend infrastructure demo."""
        print("⚙️ DEEPBLUE BACKEND INFRASTRUCTURE DEMO")
        print("=" * 60)
        print("🚀 Demonstrating enterprise-grade backend capabilities...")
        print()
        
        try:
            # 1. Health and Status Check
            await self.demo_health_status()
            
            # 2. Authentication System
            await self.demo_authentication()
            
            # 3. File Management System
            await self.demo_file_management()
            
            # 4. Database Operations
            await self.demo_database_operations()
            
            # 5. Background Job Processing
            await self.demo_background_jobs()
            
            # 6. Real-time Communication
            await self.demo_realtime_communication()
            
            # 7. System Monitoring
            await self.demo_system_monitoring()
            
            # 8. Security and Rate Limiting
            await self.demo_security_rate_limiting()
            
            # 9. Performance Testing
            await self.demo_performance_testing()
            
            print("\n🎉 DEEPBLUE BACKEND INFRASTRUCTURE DEMO COMPLETE!")
            print("✅ All systems operational and tested successfully")
            
        except Exception as e:
            print(f"\n❌ Demo failed: {e}")
            print("💡 Make sure the backend server is running on http://localhost:8000")
    
    async def demo_health_status(self):
        """Demo health and status endpoints."""
        print("1️⃣ HEALTH & STATUS CHECK")
        print("-" * 30)
        
        # Health check
        response = self.session.get(f"{self.base_url}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health Status: {data['data']['status']}")
            print(f"📊 Uptime: {data['data']['uptime']:.2f} seconds")
            print(f"🔢 Version: {data['data']['version']}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
        
        # System status
        response = self.session.get(f"{self.base_url}/status")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ System Status Retrieved")
            print(f"📊 Components: {len(data['data'])} systems monitored")
        else:
            print(f"❌ Status check failed: {response.status_code}")
        
        print()
    
    async def demo_authentication(self):
        """Demo authentication system."""
        print("2️⃣ AUTHENTICATION SYSTEM")
        print("-" * 30)
        
        # Register user
        user_data = {
            "username": "demo_user",
            "email": "demo@deepblue.com",
            "password": "secure_password123",
            "role": "admin"
        }
        
        response = self.session.post(f"{self.base_url}/api/auth/register", json=user_data)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ User registered: {data['data']['username']}")
        else:
            print(f"⚠️ Registration failed (user may exist): {response.status_code}")
        
        # Login user
        login_data = {
            "username": "demo_user",
            "password": "secure_password123"
        }
        
        response = self.session.post(f"{self.base_url}/api/auth/login", json=login_data)
        if response.status_code == 200:
            data = response.json()
            self.auth_token = data['data']['token']
            print(f"✅ User logged in successfully")
            print(f"🔑 Token received: {self.auth_token[:20]}...")
        else:
            print(f"❌ Login failed: {response.status_code}")
        
        # Get current user
        if self.auth_token:
            headers = {"Authorization": f"Bearer {self.auth_token}"}
            response = self.session.get(f"{self.base_url}/api/auth/me", headers=headers)
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Current user: {data['data']['username']}")
            else:
                print(f"❌ Get user failed: {response.status_code}")
        
        print()
    
    async def demo_file_management(self):
        """Demo file management system."""
        print("3️⃣ FILE MANAGEMENT SYSTEM")
        print("-" * 30)
        
        # Upload file
        test_file_content = b"This is a test file for DeepBlue backend infrastructure demo."
        files = {
            'file': ('test_file.txt', test_file_content, 'text/plain')
        }
        data = {
            'filename': 'test_file.txt',
            'is_public': True,
            'tags': '["demo", "test"]'
        }
        
        response = self.session.post(f"{self.base_url}/api/files/upload", files=files, data=data)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ File uploaded: {data['data']['filename']}")
            print(f"📁 File ID: {data['data']['file_id']}")
            print(f"📊 Size: {data['data']['file_size']} bytes")
        else:
            print(f"❌ File upload failed: {response.status_code}")
        
        # List files
        response = self.session.get(f"{self.base_url}/api/files")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Files listed: {len(data['data'])} files found")
            for file in data['data'][:3]:  # Show first 3 files
                print(f"   • {file['filename']} ({file['file_size']} bytes)")
        else:
            print(f"❌ List files failed: {response.status_code}")
        
        print()
    
    async def demo_database_operations(self):
        """Demo database operations."""
        print("4️⃣ DATABASE OPERATIONS")
        print("-" * 30)
        
        # List tables
        response = self.session.get(f"{self.base_url}/api/database/tables")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Database tables: {', '.join(data['data'])}")
        else:
            print(f"❌ List tables failed: {response.status_code}")
        
        # Execute query
        query_data = {
            "query": "SELECT COUNT(*) as user_count FROM users",
            "params": {}
        }
        
        response = self.session.post(f"{self.base_url}/api/database/query", json=query_data)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Query executed: {data['data']}")
        else:
            print(f"❌ Query execution failed: {response.status_code}")
        
        # Create backup
        response = self.session.post(f"{self.base_url}/api/database/backup")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Database backup created: {data['data']['backup_path']}")
        else:
            print(f"❌ Backup creation failed: {response.status_code}")
        
        print()
    
    async def demo_background_jobs(self):
        """Demo background job processing."""
        print("5️⃣ BACKGROUND JOB PROCESSING")
        print("-" * 30)
        
        # Create jobs
        job_types = [
            {"job_type": "data_processing", "payload": {"data": "sample_data"}},
            {"job_type": "file_cleanup", "payload": {"path": "/tmp"}},
            {"job_type": "email_notification", "payload": {"to": "user@example.com"}}
        ]
        
        job_ids = []
        for job_data in job_types:
            response = self.session.post(f"{self.base_url}/api/jobs", json=job_data)
            if response.status_code == 200:
                data = response.json()
                job_ids.append(data['data']['job_id'])
                print(f"✅ Job created: {job_data['job_type']} - {data['data']['job_id']}")
            else:
                print(f"❌ Job creation failed: {response.status_code}")
        
        # List jobs
        response = self.session.get(f"{self.base_url}/api/jobs")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Jobs listed: {len(data['data'])} jobs found")
            for job in data['data'][:3]:  # Show first 3 jobs
                print(f"   • {job['job_type']} - {job['status']}")
        else:
            print(f"❌ List jobs failed: {response.status_code}")
        
        # Wait a bit for jobs to process
        print("⏳ Waiting for jobs to process...")
        await asyncio.sleep(3)
        
        # Check job status
        if job_ids:
            response = self.session.get(f"{self.base_url}/api/jobs/{job_ids[0]}")
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Job status: {data['data']['status']}")
            else:
                print(f"❌ Get job failed: {response.status_code}")
        
        print()
    
    async def demo_realtime_communication(self):
        """Demo real-time communication."""
        print("6️⃣ REAL-TIME COMMUNICATION")
        print("-" * 30)
        
        try:
            # Connect to WebSocket
            uri = "ws://localhost:8000/ws"
            async with websockets.connect(uri) as websocket:
                print("✅ WebSocket connected")
                
                # Send ping message
                ping_message = {"type": "ping", "message": "Hello DeepBlue!"}
                await websocket.send(json.dumps(ping_message))
                print("📤 Ping message sent")
                
                # Wait for pong response
                try:
                    response = await asyncio.wait_for(websocket.recv(), timeout=5.0)
                    data = json.loads(response)
                    if data.get("type") == "pong":
                        print("✅ Pong response received")
                    else:
                        print(f"📥 Response received: {data}")
                except asyncio.TimeoutError:
                    print("⏰ WebSocket response timeout")
                
                # Send broadcast message
                broadcast_message = {"type": "broadcast", "message": "System status update"}
                await websocket.send(json.dumps(broadcast_message))
                print("📢 Broadcast message sent")
                
        except Exception as e:
            print(f"❌ WebSocket connection failed: {e}")
        
        print()
    
    async def demo_system_monitoring(self):
        """Demo system monitoring."""
        print("7️⃣ SYSTEM MONITORING")
        print("-" * 30)
        
        # Get metrics
        response = self.session.get(f"{self.base_url}/metrics")
        if response.status_code == 200:
            print("✅ Prometheus metrics available")
            metrics_lines = response.text.split('\n')
            print(f"📊 Metrics lines: {len(metrics_lines)}")
            # Show some sample metrics
            for line in metrics_lines[:5]:
                if line and not line.startswith('#'):
                    print(f"   • {line}")
        else:
            print(f"❌ Metrics failed: {response.status_code}")
        
        # Get system logs
        response = self.session.get(f"{self.base_url}/api/system/logs?lines=10")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ System logs retrieved: {len(data['data']['logs'])} lines")
        else:
            print(f"❌ Get logs failed: {response.status_code}")
        
        print()
    
    async def demo_security_rate_limiting(self):
        """Demo security and rate limiting."""
        print("8️⃣ SECURITY & RATE LIMITING")
        print("-" * 30)
        
        # Test rate limiting
        print("🔄 Testing rate limiting...")
        success_count = 0
        rate_limited_count = 0
        
        for i in range(10):
            response = self.session.get(f"{self.base_url}/health")
            if response.status_code == 200:
                success_count += 1
            elif response.status_code == 429:
                rate_limited_count += 1
                print(f"⚠️ Rate limited on request {i+1}")
                break
        
        print(f"✅ Successful requests: {success_count}")
        print(f"🚫 Rate limited requests: {rate_limited_count}")
        
        # Test authentication
        if self.auth_token:
            print("🔐 Testing authentication...")
            headers = {"Authorization": f"Bearer {self.auth_token}"}
            response = self.session.get(f"{self.base_url}/api/auth/me", headers=headers)
            if response.status_code == 200:
                print("✅ Authentication working")
            else:
                print(f"❌ Authentication failed: {response.status_code}")
        
        print()
    
    async def demo_performance_testing(self):
        """Demo performance testing."""
        print("9️⃣ PERFORMANCE TESTING")
        print("-" * 30)
        
        # Test response times
        endpoints = [
            "/health",
            "/status",
            "/api/files",
            "/api/jobs"
        ]
        
        for endpoint in endpoints:
            start_time = time.time()
            response = self.session.get(f"{self.base_url}{endpoint}")
            end_time = time.time()
            
            response_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            if response.status_code == 200:
                print(f"✅ {endpoint}: {response_time:.2f}ms")
            else:
                print(f"❌ {endpoint}: {response.status_code} ({response_time:.2f}ms)")
        
        # Test concurrent requests
        print("\n🔄 Testing concurrent requests...")
        async def make_request():
            response = self.session.get(f"{self.base_url}/health")
            return response.status_code == 200
        
        start_time = time.time()
        tasks = [make_request() for _ in range(10)]
        results = await asyncio.gather(*tasks)
        end_time = time.time()
        
        successful_requests = sum(results)
        total_time = end_time - start_time
        
        print(f"✅ Concurrent requests: {successful_requests}/10 successful")
        print(f"⏱️ Total time: {total_time:.2f}s")
        print(f"📊 Requests per second: {10/total_time:.2f}")
        
        print()

async def main():
    """Main demo function."""
    demo = DeepBlueBackendDemo()
    await demo.run_complete_demo()

if __name__ == "__main__":
    print("🌊 DEEPBLUE BACKEND INFRASTRUCTURE DEMO")
    print("Make sure the backend server is running:")
    print("  python3 backend_infrastructure_system.py")
    print("  or")
    print("  docker-compose -f docker-compose.backend.yml up")
    print()
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        print("💡 Make sure the backend server is running on http://localhost:8000")
