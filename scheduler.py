from task import Task

def rate_monotonic_scheduling(tasks):
    tasks.sort(key=lambda x: x.priority)  # Higher priority = lower priority number
    print("\nExecuting Rate Monotonic Scheduling (RMS):")
    
    for task in tasks:
        print(f"Executing {task.name} (Priority {task.priority})")
        task.remaining_time -= 1

def earliest_deadline_first(tasks):
    tasks.sort(key=lambda x: x.arrival_time + x.execution_time)  # EDF sorts by deadline
    print("\nExecuting Earliest Deadline First (EDF):")

    for task in tasks:
        print(f"Executing {task.name} (Deadline {task.arrival_time + task.execution_time})")
        task.remaining_time -= 1
