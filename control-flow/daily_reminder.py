def get_input(prompt):
    return input(prompt).strip()

def main():
    task = get_input("Enter your task: ")
    priority = get_input("Priority (high/medium/low): ").lower()
    time_bound = get_input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Try to complete it soon.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Plan to do it sometime soon.")
        case "low":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print(f"'{task}' has an unknown priority level. Please enter high, medium, or low.")

if __name__ == "__main__":
    main()
