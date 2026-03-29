import json
import os
from datetime import datetime

HISTORY_FILE = "data/history.json"


def get_timestamp() -> str:
    """
    获取当前时间字符串
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def ensure_history_file() -> None:
    """
    确保 history.json 文件存在
    """
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)


def save_to_history(result: dict) -> None:
    """
    保存分析结果到本地 JSON
    """
    ensure_history_file()

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            data = []

    except (json.JSONDecodeError, FileNotFoundError):
        data = []

    data.append(result)

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_history() -> list:
    """
    读取历史记录
    """
    ensure_history_file()

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            return data
        return []

    except (json.JSONDecodeError, FileNotFoundError):
        return []
