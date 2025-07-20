def get_input(prompt):
    return input(prompt).strip()

def main():
    task = get_input("Enter your task: ")
    priority = get_input("Priority (high/medium/low): ").lower()
    time_bound = get_input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            message = f"Reminder: '{task}' is a medium priority task"
        case "low":
            message = f"Note: '{task}' is a low priority task"
        case _:
            message = f"'{task}' has an unknown priority level"

    if time_bound == "yes" and priority in ("high", "medium"):
        message += " that requires immediate attention today!"
    elif priority == "low":
        message += ". Consider completing it when you have free time."

    print(message)

if __name__ == "__main__":
    main()
