from tools import tools

# A simplified REACT prompt structure
PROMPT_TEMPLATE = """
You are an AI agent that can use tools. 
When solving problems, follow this format:

Thought: reasoning about the task
Action: tool to use (one of: {tool_names})
Action Input: input to the tool
Observation: result from the tool

Repeat until the problem is solved. Finally return:
Final Answer: answer to the user

User question: {query}
"""

def run_agent(query):
    print(f"Query: {query}")
    
    # In a real scenario, this would involve a call to an LLM like Gemini.
    # Here we simulate the reasoning loop described in the assignment.
    
    # Example logic for a math query
    if any(char in query for char in "+*/-"):
        print("Thought: I need to perform a calculation.")
        print("Action: calculator")
        
        # Extract expression (simplified)
        expression = query.replace("What is ", "").replace("?", "").strip()
        print(f"Action Input: {expression}")
        
        result = tools["calculator"]["function"](expression)
        print(f"Observation: {result}")
        
        print(f"Final Answer: {result}")
    else:
        # For non-tool queries
        print("Thought: I can answer this directly without tools.")
        print(f"Final Answer: This is a general response to: {query}")
    print("-" * 20)

if __name__ == "__main__":
    # Test queries
    test_queries = [
        "What is 12 * 7?",
        "What is 100/5?",
        "Explain what embeddings are.",
        "What is 9*9?",
        "What is 5 + 12?"
    ]
    
    for q in test_queries:
        run_agent(q)