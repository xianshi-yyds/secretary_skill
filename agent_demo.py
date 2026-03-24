"""
Agent Integration Example: How an AI Assistant orchestrates the Secretary Skill.
"""

import time
from secretary import CaringSecretary

class Agent:
    def __init__(self):
        # 1. Agent 启动，初始化“贴心小秘书”技能
        print("[Agent] 正在启动并连接‘贴心小秘书’系统...")
        self.secretary = CaringSecretary()

    def process_user_goal(self, goal: str):
        """
        Agent 接收到用户的高层目标（例如：提醒我每天下午3点喝水）。
        Agent 会解析目标，并调用 Skill 的具体功能。
        """
        print(f"\n[Agent] 处理用户目标: {goal}")
        
        # 2. Agent 内部逻辑解析（模拟）
        # 假设 Agent 解析出：时间是 15:00，任务是“喝水”， persona 是“温柔提醒”
        reminder_time = "15:00"
        task_content = "补充水分，休息一下"
        task_label = "Hydration"

        # 3. Agent 调用 Skill
        print(f"[Agent] 调用 Secretary.add_reminder(time='{reminder_time}', message='{task_content}')")
        self.secretary.add_reminder(reminder_time, task_content, task_label)

        # 4. Agent 给予反馈（通过语音）
        print("[Agent] 任务下发成功，由秘书形象反馈给用户...")
        self.secretary.chat_and_speak(f"好的，我已经为您安排好了。以后每天下午{reminder_time}，我都会准时提醒您喝水的。")

    def run_simulation(self):
        # 模拟工作流
        self.process_user_goal("帮我设置一个每天下午三点的喝水提醒")
        
        print("\n[Agent] 您现在可以去忙您的事情了，小秘书将在后台为您守护。")
        # 模拟运行一段时间
        # self.secretary.run_forever()

if __name__ == "__main__":
    ai_agent = Agent()
    ai_agent.run_simulation()
