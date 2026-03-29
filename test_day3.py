# test_day3.py

from core.prompt import build_prompt
from core.llm import call_model
from core.parser import parse_response

text = "美联储官员表示通胀仍然较高，年内降息可能推迟"

prompt = build_prompt(text)

print("=== Prompt ===")
print(prompt)

response = call_model(prompt)

print("=== 模型返回 ===")
print(response)

result = parse_response(response)

print("=== 解析结果 ===")
print(result)
