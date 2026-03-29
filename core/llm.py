import requests
import logging

def call_model(prompt: str) -> str:
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "qwen2.5:7b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=30)

        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            logging.error(response.text)
            return "模型调用失败"

    except Exception as e:
        logging.error(str(e))
        return "模型请求异常"
