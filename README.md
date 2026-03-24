# 🎙️ Caring Secretary TTS (贴心小秘书)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Model: Qwen3-TTS](https://img.shields.io/badge/Model-Qwen3--TTS--Flash-orange.svg)](https://help.aliyun.com/zh/model-studio/user-guide/qwen-tts)

> **让 AI 拥有温度，让秘书走进生活。**  
> 基于通义千问 `qwen3-tts-instruct-flash` 模型开发的语音助理 Skill，具备治愈系人设与智能定时提醒功能。

---

## ✨ 核心特性

- **🎭 拟人化人设**：内置“治愈系私人秘书”指令，语速、音调、语气深度调优，提供温暖的语音陪伴。
- **⚡ 流式音频输出**：支持边合成边播放（Streaming），实现低延迟、丝滑的语音交互体验。
- **⏰ 智能定时提醒**：集成 `APScheduler` 后台任务，支持每日固定时间推送语音提醒（如喝水、服药、休息）。
- **🛠️ 高度可配置**：支持通过 `.env` 灵活切换音色（Cherry, Ryan 等）、调整语速及自定义人设指令。
- **🛡️ 安全合规**：采用标准环境变量管理 API Key，并在日志中自动进行脱敏处理。

---

## 🚀 快速开始

### 1. 环境准备 (macOS)

```bash
# 安装 PortAudio (PyAudio 的底层依赖)
brew install portaudio

# 进入项目目录
cd secretary_skill

# 安装 Python 依赖
python -m pip install -r requirements.txt
```

### 2. 配置密钥

在项目根目录创建 `.env` 文件：

```text
DASHSCOPE_API_KEY=您的阿里云API_KEY

# 可选音频配置
TTS_VOICE=Cherry
TTS_SPEECH_RATE=1.0
TTS_INSTRUCTIONS=语速偏慢，音调温柔甜美，语气治愈温暖...
```

### 3. 运行演示

```bash
# 启动完整秘书服务 (含定时任务)
python secretary.py

# 或者运行 Agent 视角演示流程
python agent_demo.py
```

---

## ⚙️ 配置说明

| 变量名 | 描述 | 默认值 |
| :--- | :--- | :--- |
| `TTS_VOICE` | 预设音色 (Cherry, Ryan, Momo 等) | `Cherry` |
| `TTS_SPEECH_RATE` | 语速调整 (0.5 - 2.0) | `1.0` |
| `TTS_INSTRUCTIONS` | 自然语言指令 (控制语气、情感) | 治愈系人设指令 |
| `TTS_MODEL` | 模型版本 | `qwen3-tts-instruct-flash` |

---

## 📂 目录结构

```text
.
├── secretary.py      # 系统协调器 (Coordinator)
├── tts_engine.py      # 语音合成核心引擎
├── scheduler.py       # 定时任务调度器
├── config.py          # 集中配置管理
├── agent_demo.py      # Agent 交互工作流演示
├── .env               # 环境变量 (Git已忽略)
└── SKILL.md           # 技能详细定义文档
```

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源。

---

**特别感谢**：感谢通义千问团队提供的强大 TTS 模型支持。
