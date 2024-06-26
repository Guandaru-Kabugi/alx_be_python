task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
reminder = None
note = None
match priority:
    case "high": reminder = f"Reminder: "
    case "low" : note = f"Note: "
if time_bound == "yes":
    print(f"{reminder} {task} is a high priority task that requires immediate attention today!")
elif time_bound == "no":
    print(f"{note} {task} is a low priority task. Consider completing it when you have free time.")