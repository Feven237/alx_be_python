# Step 1: Get user input for the task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()  # Normalize input to lowercase
time_bound = input("Is it time-bound? (yes/no): ").lower()  # Normalize input to lowercase

# Step 2: Prepare the reminder message
reminder = f"'{task}' is a {priority} priority task."

# Step 3: Use Match Case (Python 3.10+)
match priority:
    case "high":
        reminder += " It requires immediate attention today!"
    case "medium":
        reminder += " Make sure to complete it soon."
    case "low":
        reminder += " Consider completing it when you have free time."

# Step 4: Adjust the message if it's time-bound
if time_bound == "yes":
    reminder += " This task is time-sensitive."

# Step 5: Print the reminder with "Reminder:" label
print(f"Reminder: {reminder}")



