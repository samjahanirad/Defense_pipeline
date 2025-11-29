from modules.api_client import get_llm_response

def pipeline(user_input: str):
    """
    Simple base pipeline:
    1) Receive user input
    2) Send it directly to LLM (MCI API)
    3) Return the model's raw response
    """
    response = get_llm_response(user_input)
    return response
