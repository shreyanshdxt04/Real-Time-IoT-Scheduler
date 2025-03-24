from task import Task
from scheduler import rate_monotonic_scheduling, earliest_deadline_first
import time

def simulate_iot_tasks():
    tasks = [
        Task("Sensor Read", 0, 2, 1),
        Task("Camera Feed", 1, 3, 2),
        Task("Light Control", 2, 1, 3)
    ]
    
    print("Executing Rate Monotonic Scheduling:")
    rate_monotonic_scheduling(tasks)
    time.sleep(1)

    print("\nExecuting Earliest Deadline First Scheduling:")
    earliest_deadline_first(tasks)

if __name__ == "__main__":
    simulate_iot_tasks()
