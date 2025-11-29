import requests

BASE_URL ="http://mcilab.alignmentandsafety.ir:46306/v1" 

USERNAME_AS_API_KEY = "mcilab_8_pM7$tL2!qK8"  #این قسمت را با ناک کاربری مناسب پر کنید

def get_llm_response(question: str):
    
    base_url_no_v1 = BASE_URL.rsplit('/', 1)[0]
    full_url = base_url_no_v1 + "/v1/chat/completions_sync"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {USERNAME_AS_API_KEY}"
    }
    
    payload = {
        "messages": [{"role": "user", "content": question}]
    }
    
    try:
        response = requests.post(full_url, headers=headers, json=payload, timeout=60.0)
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content']

    except requests.exceptions.HTTPError as e:
        error_detail = "Unknown Error"
        try:
            error_detail = e.response.json().get("detail", str(e))
        except:
            error_detail = e.response.reason
            
        return f"HTTP Error {e.response.status_code}: {error_detail}"
        
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    test_prompt = "لطفا یک جمله انگیزشی در مورد برنامه نویسی بنویسید."
        
    response_text = get_llm_response(test_prompt)
    
    print("\n✅ Response:")
    print(response_text)