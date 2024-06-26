task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high": reminder = f"Reminder: "
    case "low" : note = f"Note: "
if time_bound == "yes":
    print(f"{task}")
elif time_bound == "no":
    print(note)