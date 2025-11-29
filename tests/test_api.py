from modules.api_client import get_llm_response

def test_api_connection():
    print("Running API test...")

    result = get_llm_response("سلام! این یک تست اولیه API است.")

    assert isinstance(result, str), "API response is not string!"
    assert len(result) > 0, "API returned empty response!"

    print("API TEST PASSED ✓")
    print("Sample Response:", result[:60])
