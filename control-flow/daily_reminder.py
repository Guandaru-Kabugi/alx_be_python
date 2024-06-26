task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high": reminder = f"'{task}' is a {priority} priority task that requires immediate attention today!"
    case "low" : note = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."
if time_bound == "yes":
    print(f"Reminder:  {reminder}")
elif time_bound == "no":
    print(f"Note: {note}")