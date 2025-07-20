# control-flow/daily_reminder.py

def send_reminder(task: str, time: str) -> None:
    """Prints a formatted daily reminder message."""
    print(f"Reminder: You need to {task} by {time} today.")

# Example usage
send_reminder("complete your daily Python task", "8:00 PM")

