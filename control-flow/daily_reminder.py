task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high": reminder = f"Reminder: {task} is a high priority task that requires immediate attention today!"
print(reminder)
    #     if time_bound == "yes":
    #         print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    #     elif time_bound == "no":
    #         print(f"Reminder: {task} is a medium priority task that requires immediate attention today!")
    # case "low":
    #     if time_bound == "yes":
    #         print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    #     elif time_bound == "no":
    #         print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    # case "medium":
    #     if time_bound == "yes":
    #         print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    #     elif time_bound == "no":
    #         print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")