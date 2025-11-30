import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.api_client import get_llm_response


def test_api_connection():
    result = get_llm_response("سلام! این یک تست اولیه API است.")
    assert result is not None
    print("Response:", result)


if __name__ == "__main__":
    test_api_connection()
