# Skill: Caring Secretary TTS (贴心小秘书)

This skill provides a voice-based personal assistant using Alibaba Cloud's `qwen3-tts-instruct-flash` model. It supports real-time text-to-speech with a caring persona and scheduled daily reminders.

## Features
- **Voice-First Interaction**: Every response is spoken by the "Secretary" in a gentle, caring tone.
- **Real-time Streaming**: Uses `pyaudio` for immediate playback without waiting for the full audio to generate.
- **Scheduled Reminders**: Set daily tasks (like medicine reminders) that the Secretary will announce at fixed times.
- **Customizable Persona**: Easily adjust the personality via the `instructions` parameter in `TTSEngine`.

## Setup
1.  **Dependencies**:
    -   Install `portaudio` (required for `pyaudio` on Mac):
        ```bash
        brew install portaudio
        ```
    -   Install Python packages (ensure you use the correct pip for your environment):
        ```bash
        python -m pip install -r requirements.txt
        ```
2.  **API Key (Secure Access)**:
    -   **Preferred**: Create a file named `.config_secret` in the project root and paste your API key inside.
    -   **Alternative**: Set your Aliyun DashScope API Key as an environment variable:
        ```bash
        export DASHSCOPE_API_KEY="your-api-key"
        ```
    -   *Note: The key is automatically masked in logs for your safety.*

3.  **Mock Mode**:
    -   If no API Key is found, the system will automatically enter **Mock Mode**. It will print the "Secretary's" dialogue to the console but will not perform real TTS calls or play audio. This is useful for testing logic.

## Usage

### 1. Running the Secretary Service
To start the background listener and scheduler:
```bash
python secretary.py
```

### 2. Adding Reminders
In `secretary.py`, you can add recurring tasks:
```python
secretary.add_reminder("08:00", "服用早上的药物", "Morning Medicine")
secretary.add_reminder("22:30", "准备休息", "Sleep Reminder")
```

### 3. Persona Customization
Edit `tts_engine.py` to change the `instructions` or `voice`:
- **Available Voices**: `Cherry`, `Serena`, `Ethan`, `Aiden`, etc.
- **Instructions**: Describe the tone (e.g., "温柔治愈风格：语速偏慢，音调温柔甜美，语气治愈温暖").

## File Structure
- `secretary.py`: Main coordinator and CLI entry.
- `tts_engine.py`: Core TTS logic using Qwen-TTS.
- `scheduler.py`: Handles background task scheduling.
- `requirements.txt`: Project dependencies.
