import time
import sys
from tts_engine import TTSEngine
from scheduler import SecretaryScheduler

class CaringSecretary:
    def __init__(self):
        print("Initializing Caring Secretary Skill...")
        self.engine = TTSEngine()
        self.scheduler = SecretaryScheduler(self.engine)
        
        # Initial greeting
        self.engine.speak("您好，我是您的私人秘书。我会时刻挂念着您，为您管理日常琐事。如果您有任何需要，请随时告诉我。")

    def add_reminder(self, time_str: str, message: str, name: str = "Work"):
        self.scheduler.add_daily_reminder(time_str, message, name)

    def chat_and_speak(self, text: str):
        """
        Normal chat interaction. Always returns voice.
        """
        # In a real scenario, this might call a LLM first.
        # For now, we assume this acts as a direct speak interface for the "Secretary".
        self.engine.speak(text)

    def run_forever(self):
        print("Secretary is online. Press Ctrl+C to stop.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nShutting down secretary service...")
            self.scheduler.stop()
            self.engine.close()

if __name__ == "__main__":
    secretary = CaringSecretary()
    
    # Example setup: Medicine reminders
    # secretary.add_reminder("08:00", "服用早上的药物", "Morning Medicine")
    # secretary.add_reminder("20:00", "服用晚上的药物", "Evening Medicine")
    
    # Optional CLI for adding reminders
    if len(sys.argv) > 1:
        # Simple CLI logic could go here
        pass
        
    secretary.run_forever()
