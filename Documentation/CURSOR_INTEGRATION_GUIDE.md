# Cursor RAG Integration Guide

This guide shows how to integrate the RAG-enhanced LLM into Cursor's AI workflows for enhanced knowledge-based assistance.

## 🎯 Overview

The integration provides Cursor AI agents with access to external knowledge through RAG, enabling:
- **Knowledge-enhanced code assistance**
- **Context-aware explanations**
- **Domain-specific help**
- **Improved accuracy and relevance**

## 🚀 Quick Setup

### 1. Basic Integration (No Training Required)

```python
# In Cursor, create a new Python file: rag_cursor_helper.py
from cursor_rag_agent import get_rag_agent, quick_query

# Initialize agent (uses pre-trained model)
agent = get_rag_agent(use_trained_model=False)

# Simple query function for Cursor AI
def ask_rag(question: str) -> str:
    return quick_query(question)

# Test it
response = ask_rag("What is machine learning?")
print(response)
```

### 2. Advanced Integration (With Your Trained Model)

```python
# In Cursor, create: advanced_rag_cursor.py
from cursor_rag_agent import CursorRAGAgent

# Initialize with your trained model
agent = CursorRAGAgent(use_trained_model=True)

# Enhanced query function
def smart_ask(question: str, mode: str = "rag_enhanced") -> str:
    return agent.query(question, mode=mode)

# Test different modes
response1 = smart_ask("Explain neural networks", mode="rag_enhanced")
response2 = smart_ask("Creative ideas for AI projects", mode="creative")
```

## 🔧 Cursor AI Integration Methods

### Method 1: Direct Function Calls

In Cursor, use the AI features to call RAG functions:

```python
# Example prompt for Cursor AI:
# "Call the ask_rag function from rag_cursor_helper.py with the question 'How do transformers work?'"

# Cursor AI will generate:
from rag_cursor_helper import ask_rag
answer = ask_rag("How do transformers work?")
print(answer)
```

### Method 2: Inline AI Suggestions

1. Open a Python file in Cursor
2. Type a comment: `# Ask RAG about machine learning`
3. Use Cursor's AI to complete with RAG call

```python
# Ask RAG about machine learning
from cursor_rag_agent import quick_query
ml_explanation = quick_query("What is machine learning?")
print(ml_explanation)
```

### Method 3: Code Generation Assistance

```python
# Prompt for Cursor AI: "Generate code that uses RAG to explain Python concepts"

from cursor_rag_agent import get_rag_agent

def explain_python_concept(concept: str) -> str:
    agent = get_rag_agent()
    return agent.query(f"Explain {concept} in Python with examples")

# Usage
explanation = explain_python_concept("list comprehensions")
print(explanation)
```

## 🎛️ Available Functions

### Core Functions

```python
from cursor_rag_agent import (
    quick_query,           # Simple question answering
    quick_explain,         # Topic explanations
    quick_compare,         # Compare multiple items
    quick_code_help,       # Coding assistance
    cursor_ai_query,       # Main Cursor integration
    cursor_explain_code,   # Code explanation
    cursor_debug_code,     # Code debugging
    cursor_suggest_improvements  # Code improvements
)
```

### Agent Methods

```python
agent = get_rag_agent()

# Query methods
agent.query("What is AI?", mode="rag_enhanced")
agent.explain("neural networks", detail_level="comprehensive")
agent.compare(["Python", "JavaScript"], aspect="performance")
agent.summarize("machine learning", length="detailed")

# Coding assistance
agent.code_help("Python", "data visualization")
agent.debug_code("def func(x): return x + 1", "syntax error")
agent.brainstorm("AI applications", context="healthcare")

# Configuration
agent.update_config(verbose=True, max_context_length=3000)
agent.clear_cache()
```

## 🎯 Generation Modes

### 1. `rag_enhanced` (Default)
- Uses retrieved knowledge + model creativity
- Best for: General questions, explanations
- Example: "Explain how neural networks work"

### 2. `knowledge_only`
- Strictly uses retrieved documents
- Best for: Factual questions, summaries
- Example: "What are the types of machine learning?"

### 3. `creative`
- Creative responses inspired by knowledge
- Best for: Brainstorming, ideas
- Example: "Creative applications of AI"

### 4. `hybrid`
- Combines knowledge and model expertise
- Best for: Complex questions
- Example: "How can AI improve healthcare?"

### 5. `pure_model`
- Uses only the model (no external knowledge)
- Best for: Creative writing, general chat
- Example: "Write a story about robots"

## 💡 Cursor AI Prompts

### For Code Assistance

```
"Use the RAG agent to help me understand this Python code:
[your code here]

Call cursor_explain_code from cursor_rag_agent.py"
```

### For Debugging

```
"I'm getting an error in this code:
[error message]
[code]

Use cursor_debug_code from cursor_rag_agent.py to help debug"
```

### For Learning

```
"I want to learn about [topic]. Use the RAG agent to provide a comprehensive explanation.

Call quick_explain from cursor_rag_agent.py with '[topic]'"
```

### For Comparisons

```
"Compare [item1] and [item2] in terms of [aspect]. Use the RAG agent for detailed comparison.

Call quick_compare from cursor_rag_agent.py with ['[item1]', '[item2]']"
```

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**
   ```python
   # Fix: Ensure the file is in your project directory
   import sys
   sys.path.append('/path/to/your/project')
   from cursor_rag_agent import get_rag_agent
   ```

2. **Model Loading Issues**
   ```python
   # Fix: Use simple mode for faster setup
   agent = get_rag_agent(use_trained_model=False)
   ```

3. **Cursor AI Not Recognizing Functions**
   ```python
   # Fix: Make functions more explicit
   def cursor_ask_rag(question: str) -> str:
       """Ask RAG agent a question - for Cursor AI integration."""
       from cursor_rag_agent import quick_query
       return quick_query(question)
   ```

### Performance Tips

1. **For Speed**
   ```python
   # Use simple mode and caching
   agent = get_rag_agent(use_trained_model=False)
   agent.update_config(cache_responses=True)
   ```

2. **For Quality**
   ```python
   # Use trained model and knowledge-only mode
   agent = get_rag_agent(use_trained_model=True)
   response = agent.query("question", mode="knowledge_only")
   ```

## 📊 Monitoring and Stats

```python
# Get agent statistics
agent = get_rag_agent()
stats = agent.get_stats()

print(f"Total queries: {stats['total_queries']}")
print(f"Cache hit rate: {stats['cache_hit_rate']:.2%}")
print(f"RAG system available: {stats['rag_system_available']}")
print(f"Available modes: {stats['available_modes']}")
```

## 🎨 Advanced Usage Examples

### 1. Code Review Assistant

```python
def code_review_assistant(code: str, language: str = "python") -> str:
    """Use RAG to provide code review."""
    agent = get_rag_agent()
    
    # Get best practices
    best_practices = agent.query(
        f"What are best practices for {language}?", 
        mode="knowledge_only"
    )
    
    # Analyze code
    analysis = agent.query(
        f"Review this {language} code for improvements:\n{code}",
        mode="rag_enhanced"
    )
    
    return f"Best Practices:\n{best_practices}\n\nCode Analysis:\n{analysis}"
```

### 2. Learning Path Generator

```python
def generate_learning_path(topic: str) -> str:
    """Generate a learning path for a topic."""
    agent = get_rag_agent()
    
    # Get overview
    overview = agent.explain(topic, detail_level="simple")
    
    # Get key concepts
    concepts = agent.query(
        f"What are the key concepts to learn for {topic}?",
        mode="knowledge_only"
    )
    
    # Get resources
    resources = agent.brainstorm(f"learning resources for {topic}")
    
    return f"Learning Path for {topic}:\n\nOverview:\n{overview}\n\nKey Concepts:\n{concepts}\n\nResources:\n{resources}"
```

### 3. Documentation Generator

```python
def generate_docs(code: str, language: str = "python") -> str:
    """Generate documentation for code."""
    agent = get_rag_agent()
    
    # Explain the code
    explanation = cursor_explain_code(code, language)
    
    # Get examples
    examples = agent.query(
        f"Provide examples of {language} code similar to this:\n{code}",
        mode="rag_enhanced"
    )
    
    return f"Documentation:\n{explanation}\n\nExamples:\n{examples}"
```

## 🚀 Production Deployment

### 1. API Endpoint for Cursor

```python
# Create: cursor_rag_api.py
from fastapi import FastAPI
from cursor_rag_agent import get_rag_agent

app = FastAPI()
agent = get_rag_agent()

@app.get("/cursor-rag")
async def cursor_rag_query(q: str, mode: str = "rag_enhanced"):
    return {"response": agent.query(q, mode=mode)}

# Run: uvicorn cursor_rag_api:app --port 8002
```

### 2. Cursor Extension Integration

```python
# Create: cursor_extension.py
def cursor_extension_query(question: str) -> str:
    """Extension function for Cursor IDE."""
    try:
        from cursor_rag_agent import quick_query
        return quick_query(question)
    except Exception as e:
        return f"RAG Agent Error: {e}"
```

## 📝 Best Practices

### 1. For Cursor AI Integration
- Use explicit function names
- Add clear docstrings
- Handle errors gracefully
- Cache frequently used queries

### 2. For Performance
- Use appropriate modes for different tasks
- Enable caching for repeated queries
- Monitor response times
- Clear cache periodically

### 3. For Quality
- Use knowledge-only mode for factual questions
- Use creative mode for brainstorming
- Combine modes for complex tasks
- Validate responses for accuracy

---

This integration transforms Cursor into a knowledge-enhanced AI coding assistant, providing context-aware help based on your specific domain knowledge!



