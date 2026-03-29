# 📈 MarketPulse：AI 市场情绪与新闻分析助手

## 一、项目简介

MarketPulse 是一个基于 Python、Streamlit 和大模型能力开发的金融新闻分析工具。

用户输入一段财经新闻后，系统将自动完成结构化分析，并输出以下结果：

- 新闻摘要
- 新闻类别
- 影响资产
- 市场情绪
- 利多利空判断
- 市场逻辑链
- 风险等级

本项目适合作为金融科技方向的 AI 应用练手项目，也可以作为个人作品集项目展示。

---

## 二、项目功能

当前版本已实现：

| 功能模块 | 功能说明 |
|----------|----------|
| 新闻输入 | 支持手动输入财经新闻 |
| 智能分析 | 调用大模型完成结构化分析 |
| 结果展示 | 页面展示分析结果 |
| 历史记录 | 展示历史分析记录 |
| 本地存储 | 保存到 data/history.json |
| 异常处理 | 模型异常时友好提示 |

---

## 三、技术栈

- Python
- Streamlit
- 大模型（Ollama / API）
- JSON（本地存储）
- Linux / WSL

---

## 四、项目结构


market_pulse/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── data/
│ └── history.json
└── core/
├── init.py
├── prompt.py
├── llm.py
├── parser.py
├── analyzer.py
└── utils.py


---

## 五、核心流程


用户输入新闻
→ 构建 Prompt
→ 调用大模型
→ 解析结果
→ 页面展示
→ 保存历史记录


---

## 六、输出字段说明

| 字段名 | 含义 |
|--------|------|
| input_text | 原始新闻 |
| summary | 新闻摘要 |
| category | 新闻类别 |
| assets | 影响资产 |
| sentiment | 市场情绪 |
| impact | 利多利空 |
| logic_chain | 逻辑链 |
| risk_level | 风险等级 |
| timestamp | 时间 |

---

## 七、运行方式

### 1. 进入项目目录


cd market_pulse


### 2. 创建虚拟环境


python3 -m venv venv


### 3. 激活环境


source venv/bin/activate


### 4. 安装依赖


pip install -r requirements.txt


### 5. 启动项目


streamlit run app.py


浏览器访问：


http://localhost:8501


---

## 八、测试示例

示例1：


美联储官员表示通胀仍然较高，年内降息可能推迟


示例2：


美元持续走强，黄金价格跌至近三个月低点


示例3：


AI板块集体回调，纳斯达克指数下跌超过2%


---

## 九、当前版本说明

当前版本为 MVP，实现：

- 单条新闻分析
- 结构化输出
- 页面展示
- 历史记录
- 本地 JSON 存储

未实现：

- 批量分析
- 市场复盘
- 图表分析
- 实时新闻接入

---

## 十、后续优化方向

- 批量新闻分析
- 市场复盘总结
- 数据可视化
- CSV 导出
- 实时新闻源接入
- 行情联动分析

---

## 十一、项目能力体现

本项目可以体现：

- Python 模块化开发能力
- Streamlit 页面开发能力
- 大模型 Prompt 设计能力
- JSON 数据处理能力
- 金融新闻分析能力

---

## 十二、总结

MarketPulse 首版实现了完整闭环：

输入 → 分析 → 展示 → 存储

是一个可持续迭代的金融 AI 应用项目。
