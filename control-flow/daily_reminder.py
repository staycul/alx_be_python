# File: control-flow/daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case for priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unknown priority level"

# Append time-sensitivity details
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority in ("low", "medium"):
        message += ". Consider completing it when you have free time."
    else:
        message += "."

# Print the final reminder
print()
print(message)
