import os
import dashscope
import pyaudio
import base64
import numpy as np
import time
from typing import Optional

class TTSEngine:
    def __init__(self, api_key: Optional[str] = None):
        # 1. 优先尝试从本地配置文件加载 (推荐，可防止系统 env 扫描)
        self._raw_api_key = api_key or self._load_from_local_config() or os.getenv("DASHSCOPE_API_KEY")
        
        if not self._raw_api_key:
            raise ValueError("[Error] API Key (DPI-K) 未找到。请在本地文件或受保护的环境变量中进行配置。")
        
        # 2. 对外暴露的 key 属性进行掩码处理，防止被外部侦测或错误打印
        self.masked_api_key = f"{self._raw_api_key[:6]}***{self._raw_api_key[-4:]}" if len(self._raw_api_key) > 10 else "***"
        
        # Default configuration for "Caring Secretary"
        self.model = "qwen3-tts-instruct-flash"
        self.voice = "Cherry" # Cherry (芊悦) - 阳光积极、亲切自然小姐姐
        self.language = "Chinese"
        self.instructions = "语速偏慢，音调温柔甜美，语气治愈温暖，像贴心朋友般关怀，充满耐心和爱心。"
        
        # PyAudio setup for streaming
        self.p = pyaudio.PyAudio()
        self.stream = None

    def _get_stream(self):
        if self.stream is None:
            self.stream = self.p.open(format=pyaudio.paInt16,
                                     channels=1,
                                     rate=24000,
                                     output=True)
        return self.stream

    def speak(self, text: str, stream: bool = True):
        """
        Converts text to speech and plays it.
        """
        print(f"Secretary speaking: {text}")
        
        # Use Beijing endpoint by default
        dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'

        response = dashscope.MultiModalConversation.call(
            model=self.model,
            api_key=self._raw_api_key, # 使用私有存储的原始 key
            text=text,
            voice=self.voice,
            language_type=self.language,
            instructions=self.instructions,
            optimize_instructions=True,
            stream=stream
        )

        if stream:
            audio_stream = self._get_stream()
            for chunk in response:
                if chunk.output is not None:
                    audio = chunk.output.audio
                    if audio.data is not None:
                        wav_bytes = base64.b64decode(audio.data)
                        audio_np = np.frombuffer(wav_bytes, dtype=np.int16)
                        audio_stream.write(audio_np.tobytes())
            time.sleep(0.5) # Allow buffer to clear
        else:
            # Non-streaming (returns URL)
            if response.status_code == 200:
                audio_url = response.output.audio.url
                print(f"Audio URL: {audio_url}")
                # Optional: Download and play or just provide URL
                return audio_url
            else:
                print(f"Error in TTS call: {response.code} (Status code: {response.status_code})")
        
        return None

    def _load_from_local_config(self) -> Optional[str]:
        """
        从本地加密或受保护的配置文件加载 key，防止暴露在进程的环境变量列表 (env) 中。
        """
        config_path = os.path.join(os.path.dirname(__file__), ".config_secret")
        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                return f.read().strip()
        return None

    def close(self):
        if hasattr(self, 'stream') and self.stream:
            self.stream.stop_stream()
            self.stream.close()
        if hasattr(self, 'p') and self.p:
            self.p.terminate()

if __name__ == "__main__":
    # Simple test
    try:
        engine = TTSEngine()
        engine.speak("您好，我是您的贴心小秘书。我会一直陪伴着您，为您提供语音提醒哦。")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        if 'engine' in locals():
            engine.close()
