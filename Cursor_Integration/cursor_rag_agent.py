"""
Cursor RAG Agent Integration
Enables Cursor AI agents to use RAG-enhanced LLM for knowledge-based tasks.
"""

import os
import sys

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))



class CursorRAGAgent:
"""
Cursor-compatible RAG agent for AI workflows.
Designed to be easily integrated into Cursor's AI features.
"""

def __init__(self, use_trained_model: bool = False, checkpoint_path: str 
    self.use_trained_model 
    self.checkpoint_path 
    self.enhanced_llm = None
    self.agent_config 
        'max_context_length': 2000,
        'default_mode': 'rag_enhanced',
        'cache_responses': True,
        'verbose': True
    }
    
    # Initialize the enhanced LLM
    self._initialize_llm()
return None
def _initialize_llm(self):
    """Initialize the RAG-enhanced LLM."""
    try:
        if self.use_trained_model and os.path.exists(self.checkpoint_path):
            print("Loading trained model with RAG...")
            self.enhanced_llm 
        else:
            print("Loading simple model (no training required)...")
            self.enhanced_llm 
        
        print("✅ RAG Agent initialized successfully!")
        
    except Exception as e:
        print(f"❌ Error initializing RAG Agent: {e}")
        print("Falling back to simple model...")
        self.enhanced_llm = create_simple_rag_llm()

def query(self, question: str, mode: str 
    """
    Query the RAG agent (Cursor-compatible interface).
    
    Args:
        question: The question to ask
        mode: Generation mode (rag_enhanced, knowledge_only, creative, hybrid, pure_model)
        **kwargs: Additional parameters
    
    Returns:
        Response string
    """
    if self.enhanced_llm is None:
        return "Error: RAG Agent not initialized"
    
    mode
    
    try:
        result 
            question, mode = mode,
            max_length
            k 
            **kwargs
        )
        
        if self.agent_config['verbose']:
            print(f"🤖 Generated response using {mode} mode")
            print(f"⏱️ Response time: {result['response_time']:.2f}s")
            if result['num_context_docs'] > 0:
                print(f"📚 Used {result['num_context_docs']} knowledge documents")
        
        return result['response']
        
    except Exception as e:
        error_msg 
        print(f"❌ {error_msg}")
        return error_msg

def ask(self, question: str) -> str:
    """Simple interface for Cursor AI (alias for query)."""
    return self.query(question)

def explain(self, topic: str, detail_level: str = "medium") -> str:
    """Explain a topic with varying levels of detail."""
    detail_prompts 
        "simple": f"Explain {topic} in simple terms:",
        "medium": f"Provide a detailed explanation of {topic}:",
        "comprehensive": f"Give a comprehensive explanation of {topic}, covering key concepts, examples, and applications:"
    }
    
    prompt 
    return self.query(prompt, mode 

def compare(self, items: List[str], aspect: str = "features") -> str:
    """Compare multiple items."""
    items_str 
    prompt
    return self.query(prompt, mode 

def summarize(self, topic: str, length: str = "medium") -> str:
    """Summarize a topic."""
    length_prompts 
        "brief": f"Provide a brief summary of {topic}:",
        "medium": f"Summarize {topic}:",
        "detailed": f"Provide a detailed summary of {topic}:"
    }
    
    prompt 
    return self.query(prompt, mode 

def brainstorm(self, topic: str, context: str = "") -> str:
    """Brainstorm ideas about a topic."""
    if context:
        prompt 
    else:
        prompt 
    
    return self.query(prompt, mode

def code_help(self, language: str, task: str) -> str:
    """Get coding help."""
    prompt = f"Help me with {task} in {language}. Provide code examples and explanations:"
    return self.query(prompt, mode 

def debug_code(self, code: str, error: str 
    """Debug code issues."""
    if error:
        prompt 
    else:
        prompt = f"Help debug this code:\n\n{code}"
    
    return self.query(prompt, mode 

def get_stats(self) -> Dict[str, Any]:
    """Get agent statistics."""
    if self.enhanced_llm is None:
        return {"error": "Agent not initialized"}
    
    stats 
    stats.update({
        'agent_config': self.agent_config,
        'use_trained_model': self.use_trained_model,
        'checkpoint_path': self.checkpoint_path
    })
    
    return stats

def update_config(self, **kwargs):
    """Update agent configuration."""
    self.agent_config.update(kwargs)
    print(f"✅ Agent config updated: {kwargs}")

def clear_cache(self):
    """Clear the knowledge cache."""
    if self.enhanced_llm:
        self.enhanced_llm.clear_cache()
return None
def set_verbose(self, verbose: bool):
    """Set verbose mode."""
    self.agent_config['verbose'] 

return None
# Global agent instance for easy access
_global_agent = None

def get_rag_agent(use_trained_model: bool 
"""Get or create the global RAG agent instance."""
global _global_agent

if _global_agent is None:
    _global_agent 

return _global_agent

def quick_query(question: str, mode: str = os.getenv("str".upper(), "rag_enhanced")) -> str:
"""Quick query function for Cursor AI integration."""
agent 
return agent.query(question, mode 

def quick_explain(topic: str) -> str:
"""Quick explanation function."""
agent 
return agent.explain(topic)

def quick_compare(items: List[str]) -> str:
"""Quick comparison function."""
agent = get_rag_agent()
return agent.compare(items)

def quick_code_help(language: str, task: str) -> str:
"""Quick coding help function."""
agent 
return agent.code_help(language, task)


# Cursor-specific integration functions
def cursor_ai_query(question: str) -> str:
"""
Main function for Cursor AI integration.
Call this from Cursor's AI features.
"""
return quick_query(question)

def cursor_explain_code(code: str, language: str 
"""Explain code for Cursor AI."""
agent 
prompt = f"Explain this {language} code:\n\n{code}"
return agent.query(prompt, mode 

def cursor_debug_code(code: str, error_message: str 
"""Debug code for Cursor AI."""
agent 
return agent.debug_code(code, error_message)

def cursor_suggest_improvements(code: str, language: str = "python") -> str:
"""Suggest code improvements for Cursor AI."""
agent 
prompt
return agent.query(prompt, mode


if __name__ == "__main__":
import argparse

parser = argparse.ArgumentParser(description 
parser.add_argument('--use_trained', action 
                   help 
parser.add_argument('--query', type = str, default 
                   help 
parser.add_argument('--mode', type
                   choices = ['rag_enhanced', 'knowledge_only', 'creative', 'hybrid', 'pure_model'],
                   help 
parser.add_argument('--interactive', action 
                   help 
parser.add_argument('--verbose', action = os.getenv("action".upper(), "store_true"),
                   help 

args 

# Create agent
agent 

if args.verbose:
    agent.set_verbose(True)

if args.interactive:
    # Interactive mode
    print("🤖 Cursor RAG Agent - Interactive Mode")
    print("Type 'quit' to exit, 'help' for commands")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n❓ Enter your question: ").strip()
            
            if user_input.lower() 
                break
            elif user_input.lower() 
                print("\nCommands:")
                print("  explain <topic> - Explain a topic")
                print("  compare <item1, item2> - Compare items")
                print("  summarize <topic> - Summarize a topic")
                print("  brainstorm <topic> - Brainstorm ideas")
                print("  code <language> <task> - Get coding help")
                print("  stats - Show agent statistics")
                print("  quit - Exit")
                continue
            elif user_input.lower() == 'stats':
                stats = agent.get_stats()
                print(f"\n📊 Agent Statistics:")
                for key, value in stats.items():
                    if key !
                        print(f"  {key}: {value}")
                continue
            elif not user_input:
                continue
            
            # Process command
            if user_input.startswith('explain '):
                topic 
                response 
            elif user_input.startswith('compare '):
                items_str = user_input[8:].strip()
                items 
                response 
            elif user_input.startswith('summarize '):
                topic 
                response = agent.summarize(topic)
            elif user_input.startswith('brainstorm '):
                topic 
                response 
            elif user_input.startswith('code '):
                parts 
                if len(parts) == 2:
                    language, task = parts
                    response 
                else:
                    response 
            else:
                # Regular query
                response 
            
            print(f"\n🤖 Response: {response}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

else:
    # Single query mode
    print(f"🔍 Query: {args.query}")
    print(f"🎯 Mode: {args.mode}")
    print("-" * 50)
    
    response = agent.query(args.query, mode
    print(f"\n🤖 Response: {response}")
    
    # Show stats
    stats 
    print(f"\n📊 Agent Stats:")
    print(f"  Total queries: {stats.get('total_queries', 0)}")
    print(f"  RAG system available: {stats.get('rag_system_available', False)}")
    print(f"  Available modes: {', '.join(stats.get('available_modes', []))}")



