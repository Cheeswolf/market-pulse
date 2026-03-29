# MarketPulse

> 基于 Python、Streamlit 与大模型的财经新闻结构化分析工具。

## 项目简介

MarketPulse 是一个面向财经信息理解与市场情绪分析场景的轻量级 AI 应用。
用户输入一段财经新闻后，系统会自动完成摘要提炼、新闻分类、影响资产识别、市场情绪判断、利多利空分析、逻辑链生成与风险等级评估，并将结果以结构化形式展示和保存，便于后续查看与复盘。

本项目适合作为以下用途：

* 金融科技方向课程练手项目
* 大模型应用开发入门项目
* Streamlit 小型产品化项目
* 个人作品集与简历展示项目

---

## 核心功能

### 已实现功能

* 单条财经新闻输入与分析
* 大模型结构化分析输出
* 新闻摘要提炼
* 新闻类别识别
* 影响资产识别
* 市场情绪判断
* 利多利空分析
* 市场逻辑链生成
* 风险等级评估
* Streamlit 页面展示
* 历史记录展示
* 本地 JSON 持久化存储
* 基础异常处理

### 规划中的后续功能

* 多条新闻批量分析
* 市场情绪汇总
* 图表可视化展示
* 新闻数据导出
* 实时新闻源接入
* 新闻与行情联动分析

---

## 项目结构

```text
market_pulse/
│
├── assets/
│   ├── demo.png
│   ├── history.png
│   └── test.png
│
├── core/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── llm.py
│   ├── parser.py
│   ├── prompt.py
│   └── utils.py
│
├── data/
│   └── history.json
│
├── tests/
│   └── ...
│
├── .gitignore
├── README.md
├── app.py
├── config.py
└── requirements.txt
```

---

## 模块说明

| 模块                  | 说明                                       |
| ------------------- | ---------------------------------------- |
| `app.py`            | Streamlit 页面入口，负责接收用户输入、触发分析流程、展示结果与历史记录 |
| `config.py`         | 项目基础配置文件，用于管理模型参数、路径配置等内容                |
| `core/prompt.py`    | 负责构建财经新闻分析 Prompt                        |
| `core/llm.py`       | 负责封装大模型调用逻辑                              |
| `core/parser.py`    | 负责解析模型返回结果，并转换为结构化数据                     |
| `core/analyzer.py`  | 串联 Prompt 构建、模型调用、结果解析等完整分析流程            |
| `core/utils.py`     | 工具函数模块，负责历史记录读写、时间处理等公共逻辑                |
| `data/history.json` | 本地历史记录文件，用于保存分析结果                        |
| `assets/`           | README 使用的项目截图资源                         |
| `tests/`            | 测试脚本目录                                   |
| `.gitignore`        | Git 忽略文件配置                               |

---

## 技术栈

| 类别    | 技术                 |
| ----- | ------------------ |
| 编程语言  | Python             |
| 页面框架  | Streamlit          |
| 大模型调用 | Ollama / API       |
| 数据存储  | JSON               |
| 运行环境  | WSL / Linux + venv |

---

## 安装与运行

### 1. 克隆项目

```bash
git clone https://github.com/Cheeswolf/market-pulse.git
cd market-pulse
```

### 2. 创建虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 启动项目

```bash
streamlit run app.py
```

启动后，在浏览器访问：

```text
http://localhost:8501
```

---

## 使用方式

1. 启动 Streamlit 应用
2. 在输入框中粘贴一段财经新闻
3. 点击分析按钮
4. 查看系统返回的结构化分析结果
5. 在历史记录区域查看过往分析内容

---

## 输出字段说明

系统返回的分析结果包含以下核心字段：

| 字段名           | 含义      |
| ------------- | ------- |
| `summary`     | 新闻摘要    |
| `category`    | 新闻类别    |
| `assets`      | 受影响资产   |
| `sentiment`   | 市场情绪    |
| `impact`      | 利多利空判断  |
| `logic_chain` | 市场影响逻辑链 |
| `risk_level`  | 风险等级    |

---

## 输出示例

```json
{
  "summary": "美联储官员暗示短期内不会降息",
  "category": "货币政策",
  "assets": ["股票", "债券"],
  "sentiment": "偏空",
  "impact": "利空",
  "logic_chain": "由于通胀较高，美联储可能推迟降息时间窗口，这将提高市场对未来利率水平的预期，增加资金成本，从而对股市和债市形成压力。",
  "risk_level": "中"
}
```

---

## 系统流程

```text
用户输入财经新闻
        ↓
构建 Prompt
        ↓
调用大模型
        ↓
解析模型返回结果
        ↓
页面展示分析结果
        ↓
保存历史记录到本地文件
```

---

## 项目预览

### 主页面

![demo](assets/demo.png)

### 历史记录页面

![history](assets/history.png)

### 运行效果示例

![test](assets/test.png)

---

## 测试

测试脚本位于 `tests/` 目录中。可以根据实际文件名执行，例如：

```bash
python3 tests/test_day3.py
python3 tests/test_day4.py
```

如果测试文件名称与上述示例不同，请以仓库中的实际文件名为准。

---

## 项目特点

* 聚焦金融新闻分析场景，主题明确
* 采用模块化结构，便于后续维护与扩展
* 从输入、分析、展示到存储形成完整闭环
* 具备基础产品形态，适合作为作品集项目展示
* 兼顾 AI 应用开发与金融分析思维训练

---

## 当前限制

* 当前版本主要支持单条新闻分析
* 分析质量受模型能力与输出稳定性影响
* 当模型返回格式不规范时，可能出现解析失败
* 当前版本更适合作为学习项目与辅助分析工具，不构成投资建议

---

## 后续优化方向

* 支持多条新闻批量输入与统一汇总
* 增加市场情绪统计与图表展示
* 支持导出 JSON / CSV 分析结果
* 接入实时财经新闻源
* 联动行情数据，增强分析维度
* 增加更严格的结果校验机制

---

## 简历描述示例

**项目名称：** MarketPulse：AI 市场情绪与新闻分析助手

**项目描述：**
基于 Python、Streamlit 与大模型能力开发财经新闻结构化分析工具，实现新闻摘要提炼、类别识别、影响资产提取、市场情绪判断、利多利空分析与逻辑链生成，并支持历史记录展示和本地 JSON 存储，形成从输入到分析再到展示与持久化的完整应用闭环。

---

## 适用场景

* 金融科技专业课程项目
* AI 应用开发练手项目
* 大模型 Prompt 工程实践项目
* 个人 GitHub 作品展示
* 简历项目经历补充

---

## 作者

* GitHub: [Cheeswolf](https://github.com/Cheeswolf)

---

## License

本项目仅用于学习交流、课程练手与个人作品展示。

