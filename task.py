class Task:
    def __init__(self, name, arrival_time, execution_time, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.priority = priority
        self.remaining_time = execution_time

    def __str__(self):
        return f"Task({self.name}, Arrival: {self.arrival_time}, Exec: {self.execution_time}, Priority: {self.priority})"
