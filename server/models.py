import requests
import json

GPT4_API_URL = "https://api.openai.com/v1/chat/completions"  # 请确认这是正确的 API 地址
GPT4_API_TOKEN = ""  # 您提供的 token

def summarize_with_gpt4(text, max_length=200):
    try:
        headers = {
            "Authorization": f"Bearer {GPT4_API_TOKEN}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "gpt-4",
            "messages": [
                {"role": "system", "content": f"Summarize the following text in no more than {max_length} characters:"},
                {"role": "user", "content": text}
            ],
            "max_tokens": max_length
        }
        
        response = requests.post(GPT4_API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # 如果请求失败，这将引发一个异常
        
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        raise Exception(f"Error in GPT-4 API call: {str(e)}")

# 删除了其他模型的函数