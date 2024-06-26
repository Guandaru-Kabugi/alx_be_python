task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
# match priority:
#     case "high": reminder = f"'{task}'"
#     case "low" : note = f"'{task}'"
# if time_bound == "yes":
#     print(f"Reminder:",reminder, "is a high priority task that requires immediate attention today!")
# elif time_bound == "no":
#     print(f"Note:",note, "is a low priority task. Consider completing it when you have free time.")

match priority:
    case "high": reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
    case "low" : note = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
if time_bound == "yes":
    print(reminder)
elif time_bound == "no":
    print(note)