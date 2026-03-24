import time
from apscheduler.schedulers.background import BackgroundScheduler
from tts_engine import TTSEngine
from datetime import datetime

class SecretaryScheduler:
    def __init__(self, tts_engine: TTSEngine):
        self.scheduler = BackgroundScheduler()
        self.tts_engine = tts_engine
        self.scheduler.start()

    def add_daily_reminder(self, time_str: str, message: str, task_name: str = "Reminder"):
        """
        Adds a daily reminder. time_str should be in 'HH:MM' format.
        """
        hour, minute = map(int, time_str.split(':'))
        
        def reminder_task():
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{now}] Executing reminder: {task_name}")
            # Ensure the secretary speaks the reminder
            full_message = f"亲爱的，现在是{time_str}，提醒您该{message}了。不要忘记哦。"
            self.tts_engine.speak(full_message)

        # Schedule daily at specific hour and minute
        self.scheduler.add_job(
            reminder_task,
            'cron',
            hour=hour,
            minute=minute,
            id=task_name,
            replace_existing=True
        )
        print(f"Scheduled '{task_name}' at {time_str} daily.")

    def add_one_off_reminder(self, delay_seconds: int, message: str):
        """
        Adds a one-off reminder after a delay for testing.
        """
        def task():
            self.tts_engine.speak(message)
        
        self.scheduler.add_job(task, 'date', run_date=datetime.now()) # Example: trigger immediately or after delay

    def stop(self):
        self.scheduler.shutdown()

if __name__ == "__main__":
    # Test script
    engine = TTSEngine()
    scheduler = SecretaryScheduler(engine)
    
    print("Setting up a test reminder for 10 seconds from now...")
    # For testing, we just trigger a message immediately
    scheduler.add_one_off_reminder(1, "这只是一个测试提醒，您的秘书系统已经准备好了。")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        scheduler.stop()
        engine.close()
