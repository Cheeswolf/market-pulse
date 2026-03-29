# 📈 MarketPulse：AI 市场情绪与新闻分析助手

> 一个基于大模型的财经新闻结构化分析工具，用于快速提炼新闻关键信息、识别市场情绪，并生成可复盘的分析结果。

---

## 项目简介

MarketPulse 是一个面向金融信息分析场景的小型 AI 应用。

用户输入一段财经新闻后，系统会自动输出结构化分析结果，包括：

* 新闻摘要
* 新闻类别
* 影响资产
* 市场情绪
* 利多利空判断
* 逻辑链分析
* 风险等级

项目使用 Streamlit 搭建交互页面，使用 Python 完成分析流程串联，并将分析结果保存到本地 JSON 文件中，便于后续查看与复盘。

---

## 项目目标

本项目用于练习并整合以下能力：

| 能力方向      | 具体内容                     |
| --------- | ------------------------ |
| Python 开发 | 模块化拆分、函数封装、JSON 处理、异常处理  |
| AI 应用开发   | Prompt 设计、模型调用、结构化输出解析   |
| 工程实践      | 页面展示、历史记录保存、目录组织         |
| 金融分析思维    | 新闻分类、市场情绪识别、资产影响映射、逻辑链梳理 |

---

## 功能特性

### 当前已实现

* [x] 支持输入单条财经新闻
* [x] 调用大模型进行结构化分析
* [x] 输出摘要、类别、影响资产、情绪、利多利空、逻辑链、风险等级
* [x] 使用 Streamlit 展示分析结果
* [x] 保存历史记录到本地 JSON 文件
* [x] 在页面中查看历史分析记录
* [x] 基础异常处理

### 后续计划

* [ ] 多条新闻批量分析
* [ ] 市场情绪汇总
* [ ] 图表可视化
* [ ] 接入实时新闻源
* [ ] 市场复盘总结

---

## 项目预览

![demo](assets/demo.png)

![history](assets/history.png)

![test](assets/test.png)

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

## 各模块说明

| 文件 / 目录             | 作用                                |
| ------------------- | --------------------------------- |
| `app.py`            | Streamlit 页面入口，负责用户输入、结果展示、历史记录展示 |
| `config.py`         | 项目配置文件，管理模型参数、路径或基础配置             |
| `core/prompt.py`    | 构建金融新闻分析 Prompt                   |
| `core/llm.py`       | 封装模型调用逻辑                          |
| `core/parser.py`    | 解析模型返回结果，转换为结构化数据                 |
| `core/analyzer.py`  | 串联 Prompt、模型调用、结果解析，形成完整分析流程      |
| `core/utils.py`     | 工具函数，如历史记录保存、读取、时间处理等             |
| `data/history.json` | 本地历史记录文件                          |
| `assets/`           | README 展示截图资源                     |
| `tests/`            | 测试脚本与测试文件                         |
| `.gitignore`        | Git 忽略规则配置                        |

---

## 技术栈

| 模块   | 技术           |
| ---- | ------------ |
| 页面框架 | Streamlit    |
| 后端逻辑 | Python       |
| 模型调用 | Ollama / API |
| 数据存储 | JSON         |
| 运行环境 | WSL + venv   |

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

启动后在浏览器访问：

```text
http://localhost:8501
```

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
解析返回结果
        ↓
页面展示分析结果
        ↓
保存到本地历史记录
```

---

## 测试

如果你已经将测试脚本整理到 `tests/` 目录，可以在项目根目录下运行对应测试文件，例如：

```bash
python3 tests/test_day3.py
python3 tests/test_day4.py
```

如果你的测试文件名和这里不一致，就把命令替换成你实际文件名。

---

## 当前项目特点与限制

* 当前版本以单条新闻分析为主
* 结果质量依赖模型输出稳定性
* 若模型返回格式不规范，仍可能出现解析失败
* 当前更适合作为学习项目、作品集项目和基础投研辅助工具

---

## 项目亮点

* 结合金融场景设计 AI 应用，而不是通用聊天 Demo
* 从输入、分析、展示到存储形成完整闭环
* 已完成基础模块化拆分，便于后续扩展
* 支持继续升级为批量新闻分析、市场复盘助手、新闻与行情联动工具

---

## 后续优化方向

* 支持多条新闻批量分析
* 增加市场情绪汇总功能
* 增加图表可视化
* 支持导出分析结果
* 接入实时新闻源
* 联动行情数据做增强分析

---

## 简历描述示例

**项目名称：** MarketPulse：AI 市场情绪与新闻分析助手

**项目描述：** 基于 Python、Streamlit 与大模型能力开发财经新闻结构化分析工具，实现新闻摘要、类别识别、影响资产提取、市场情绪判断、利多利空分析与逻辑链生成，并支持历史记录展示和本地 JSON 存储。

---

## 作者

* GitHub: [Cheeswolf](https://github.com/Cheeswolf)

---

## License

本项目仅用于学习、练手与个人作品展示。

