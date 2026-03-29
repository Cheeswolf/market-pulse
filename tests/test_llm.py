from core.llm import call_model

prompt = "请用一句话总结：美联储可能推迟降息，对市场有什么影响？"

result = call_model(prompt)

print("模型返回：")
print(result)
