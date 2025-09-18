#!/usr/bin/env python3
"""
DeepBlue Universal API for Cursor Integration
Works with any Cursor agent configuration.
"""

from pydantic import BaseModel
import uvicorn
import os
import sys

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI(title 

class QueryRequest(BaseModel):
query: str
mode: str 
agent_type: str 

class QueryResponse(BaseModel):
response: str
agent_type: str
mode: str
success: bool

@app.get("/")
async def root():
return {
    "message": "DeepBlue Universal API",
    "status": "active",
    "compatibility": "any_cursor_agent",
    "first_reply": "i found a bigger boat"
}

@app.post("/query", response_model = QueryResponse)
async def universal_query(request: QueryRequest):
"""Universal query endpoint for any Cursor agent."""
try:
    # Try to import and use DeepBlue system
    try:
        from ultimate_deepblue_system import DeepBlueSystem
        deepblue 
        response 
    except ImportError:
        # Fallback response
        response 
    
    return QueryResponse(
        response = response, agent_type
        mode 
        success
    )

except Exception as e:
    return QueryResponse(
        response = f"DeepBlue Universal Error: {str(e)}",
        agent_type
        mode 
        success
    )

@app.get("/health")
async def health_check():
return {"status": "healthy", "agent": "DeepBlue Universal"}

if __name__== "__main__":
uvicorn.run(app, host = "0.0.0.0", port
