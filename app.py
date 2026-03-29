import streamlit as st
from core.analyzer import analyze_news
from core.utils import load_history

st.set_page_config(page_title="MarketPulse", page_icon="📈", layout="wide")

if "history" not in st.session_state:
    st.session_state["history"] = load_history()

st.title("📈 MarketPulse：AI 市场情绪与新闻分析助手")
st.caption("输入一段财经新闻，系统将自动输出结构化分析结果。")

st.divider()

input_text = st.text_area(
    "请输入财经新闻内容：",
    height=180,
    placeholder="例如：美联储官员表示通胀仍然较高，年内降息可能推迟"
)

analyze_button = st.button("开始分析")

if analyze_button:
    if not input_text.strip():
        st.warning("请输入新闻内容后再进行分析。")
    else:
        try:
            with st.spinner("AI 正在分析中..."):
                result = analyze_news(input_text)

            st.session_state["history"] = load_history()

            st.divider()
            st.subheader("📌 分析结果")

            st.write(f"**摘要：** {result.get('summary', '无')}")
            st.write(f"**类别：** {result.get('category', '无')}")

            assets = result.get("assets", [])
            if isinstance(assets, list):
                assets_text = ", ".join(assets) if assets else "无"
            else:
                assets_text = str(assets)

            st.write(f"**影响资产：** {assets_text}")

            sentiment = result.get("sentiment", "无")
            if sentiment == "偏多":
                st.success(f"市场情绪：{sentiment}")
            elif sentiment == "偏空":
                st.error(f"市场情绪：{sentiment}")
            else:
                st.warning(f"市场情绪：{sentiment}")

            st.write(f"**利多利空：** {result.get('impact', '无')}")
            st.write(f"**风险等级：** {result.get('risk_level', '无')}")
            st.markdown("**逻辑链：**")
            st.write(result.get("logic_chain", "无"))

        except Exception:
            st.error("分析失败，请检查模型状态或稍后重试。")

if st.session_state["history"]:
    st.divider()
    st.subheader("📜 历史记录")

    for i, item in enumerate(reversed(st.session_state["history"]), start=1):
        summary = item.get("summary", "无摘要")
        timestamp = item.get("timestamp", "无时间")

        with st.expander(f"记录 {i} | {timestamp} | {summary}"):
            st.write(f"**原文：** {item.get('input_text', '无')}")
            st.write(f"**类别：** {item.get('category', '无')}")
            st.write(f"**情绪：** {item.get('sentiment', '无')}")
            st.write(f"**风险等级：** {item.get('risk_level', '无')}")

            assets = item.get("assets", [])
            if isinstance(assets, list):
                assets_text = ", ".join(assets) if assets else "无"
            else:
                assets_text = str(assets)

            st.write(f"**影响资产：** {assets_text}")
            st.write(f"**利多利空：** {item.get('impact', '无')}")
            st.write(f"**逻辑链：** {item.get('logic_chain', '无')}")
