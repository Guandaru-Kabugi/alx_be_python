task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high": 
        if time_bound == "yes":
            reminder = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"'{task}' is a high priority task but does not need immediate attention."
    case "medium": 
        if time_bound == "yes":
            reminder = f"'{task}' is a medium priority task that requires immediate attention today!"
        else:
            reminder = f"'{task}' is a medium priority task but does not need immediate attention."
    case "low" : 
        if time_bound == "yes":
            reminder = f"'{task}' is a low priority task. Consider completing it sooner."
        else:
            reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
print("Reminder: ",reminder)