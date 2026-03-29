import json
import re


def parse_response(raw_response: str) -> dict:
    """
    解析模型返回结果：
    1. 先尝试直接按 JSON 解析
    2. 如果失败，尝试从 ```json ... ``` 代码块中提取
    3. 如果还失败，尝试从文本中截取第一个 { ... } JSON 对象
    4. 最后兜底返回解析失败结果
    """

    default_result = {
        "summary": "解析失败",
        "category": "未知",
        "assets": [],
        "sentiment": "未知",
        "impact": "解析失败",
        "logic_chain": "解析失败",
        "risk_level": "未知"
    }

    if not raw_response or not raw_response.strip():
        return default_result

    raw_response = raw_response.strip()

    # 1. 直接解析
    try:
        result = json.loads(raw_response)
        if isinstance(result, dict):
            return result
    except Exception:
        pass

    # 2. 提取 ```json ... ``` 代码块中的 JSON
    try:
        match = re.search(r"```json\s*(\{.*?\})\s*```", raw_response, re.DOTALL)
        if match:
            json_text = match.group(1)
            result = json.loads(json_text)
            if isinstance(result, dict):
                return result
    except Exception:
        pass

    # 3. 提取普通文本中的第一个 JSON 对象
    try:
        match = re.search(r"(\{.*\})", raw_response, re.DOTALL)
        if match:
            json_text = match.group(1)
            result = json.loads(json_text)
            if isinstance(result, dict):
                return result
    except Exception:
        pass

    # 4. 最终兜底
    return {
        "summary": "解析失败",
        "category": "未知",
        "assets": [],
        "sentiment": "未知",
        "impact": raw_response[:200],
        "logic_chain": raw_response[:500],
        "risk_level": "未知"
    }
