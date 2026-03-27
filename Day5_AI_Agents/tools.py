import re

def calculator(expression):
    """
    Performs mathematical calculations for the agent.
    Supports basic arithmetic: +, -, *, /
    """
    # Remove any non-mathematical characters for safety
    expression = re.sub(r'[^-+*/0-9.()]', '', expression)
    try:
        # Evaluate the mathematical expression
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

# Example tool definition for the LLM
tools = {
    "calculator": {
        "description": "Performs mathematical calculations. Input should be a math expression.",
        "function": calculator
    }
}