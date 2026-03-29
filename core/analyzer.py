from core.prompt import build_prompt
from core.llm import call_model
from core.parser import parse_response
from core.utils import save_to_history, get_timestamp


def analyze_news(input_text: str) -> dict:
    """
    完整分析流程：
    输入新闻 -> Prompt -> 模型 -> 解析 -> 补全字段 -> 保存结果 -> 返回结果
    """
    try:
        # 1. 构建 Prompt
        prompt = build_prompt(input_text)

        # 2. 调用模型
        raw_response = call_model(prompt)

        # 3. 解析模型输出
        result = parse_response(raw_response)

        # 4. 兜底处理 assets 字段，确保一定是 list
        assets = result.get("assets", [])
        if isinstance(assets, str):
            assets = [x.strip() for x in assets.split(",") if x.strip()]
        elif not isinstance(assets, list):
            assets = []

        # 5. 统一最终返回结构
        final_result = {
            "input_text": input_text,
            "summary": result.get("summary", "无法确定"),
            "category": result.get("category", "无法确定"),
            "assets": assets,
            "sentiment": result.get("sentiment", "无法确定"),
            "impact": result.get("impact", "无法确定"),
            "logic_chain": result.get("logic_chain", "无法确定"),
            "risk_level": result.get("risk_level", "无法确定"),
            "timestamp": get_timestamp()
        }

        # 6. 保存历史记录
        save_to_history(final_result)

        return final_result

    except Exception as e:
        error_result = {
            "input_text": input_text,
            "summary": "解析失败",
            "category": "未知",
            "assets": [],
            "sentiment": "未知",
            "impact": "解析失败",
            "logic_chain": f"错误信息：{str(e)}",
            "risk_level": "未知",
            "timestamp": get_timestamp()
        }

        save_to_history(error_result)
        return error_result
