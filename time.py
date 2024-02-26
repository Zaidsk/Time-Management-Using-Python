import random

# Define activities and their average durations in minutes
activities = {
    "Sleep": 500,   # 8 hours and 20 minutes
    "Work/School": 360,  # 6 hours
    "Commute": 60,  # 1 hour
    "Family Time": 120,  # 2 hours
    "Meals": 90,  # 1.5 hours
    "Exercise": 60,  # 1 hour
    "Chores": 60,  # 1 hour
    "Relaxation": 60,  # 1 hour
}

# Calculate total available time excluding sleep
total_time = 1440 - activities["Sleep"]

# Calculate total duration of all activities
total_activity_time = sum(activities.values())

# Calculate remaining time after accounting for activities
remaining_time = total_time - total_activity_time

# Allocate remaining time evenly among remaining activities
remaining_activities = {activity: remaining_time // (len(activities) - 1) for activity in activities if activity != "Sleep"}

# Merge allocated time with predefined activity durations
daily_schedule = {**activities, **remaining_activities}

# Display daily schedule
print("Daily Schedule (in minutes):")
for activity, duration in daily_schedule.items():
    print(f"{activity}: {duration}")

# Calculate and display total time allocated
total_allocated_time = sum(daily_schedule.values())
print(f"\nTotal Time Allocated: {total_allocated_time} minutes")

# Calculate and display percentage of time allocated
percentage_allocated = (total_allocated_time / 1440) * 100
print(f"Percentage of Time Allocated: {percentage_allocated:.2f}%")
