import tkinter as tk
from tkinter import ttk
from scheduler import Task, TaskManager

class SchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IoT Real-Time Task Scheduler with Priorities")
        self.root.configure(bg="#f0f2f5")
        self.task_objects = []
        self.task_manager = TaskManager()
        self.create_widgets()

    def clear_logs(self):
        self.log_text.configure(state='normal')
        self.log_text.delete(1.0, tk.END)
        self.log_text.configure(state='disabled')

    def clear_task_list(self):
        self.task_listbox.delete(0, tk.END)
        self.task_objects.clear()
        self.task_manager.clear_tasks()
        self.log("All scheduled tasks cleared.")

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg="#f0f2f5")
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        left_frame = tk.Frame(main_frame, bg="#f0f2f5")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, anchor='n')

        right_frame = tk.Frame(main_frame, bg="#f0f2f5")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, anchor='n')

        # Form Layout Grid
        form_frame = tk.Frame(left_frame, bg="#f0f2f5")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Add Task", font=("Arial", 18), bg="#f0f2f5").grid(row=0, column=0, columnspan=2, pady=(0, 10))

        tk.Label(form_frame, text="Task Name:", font=("Arial", 12), bg="#f0f2f5").grid(row=1, column=0, sticky='w', pady=2)
        self.task_name_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.task_name_entry.grid(row=1, column=1, pady=2)

        tk.Label(form_frame, text="Time Interval (s) or Delay:", font=("Arial", 12), bg="#f0f2f5").grid(row=2, column=0, sticky='w', pady=2)
        self.task_interval_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.task_interval_entry.grid(row=2, column=1, pady=2)

        tk.Label(form_frame, text="Working Time (s):", font=("Arial", 12), bg="#f0f2f5").grid(row=3, column=0, sticky='w', pady=2)
        self.task_working_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.task_working_entry.grid(row=3, column=1, pady=2)

        tk.Label(form_frame, text="Task Type:", font=("Arial", 12), bg="#f0f2f5").grid(row=4, column=0, sticky='w', pady=2)
        self.task_type = ttk.Combobox(form_frame, values=["Periodic", "Aperiodic"], font=("Arial", 12), width=28)
        self.task_type.current(0)
        self.task_type.grid(row=4, column=1, pady=2)

        tk.Label(form_frame, text="Priority:", font=("Arial", 12), bg="#f0f2f5").grid(row=5, column=0, sticky='w', pady=2)
        self.task_priority = ttk.Combobox(form_frame, values=["High", "Medium", "Low"], font=("Arial", 12), width=28)
        self.task_priority.current(1)
        self.task_priority.grid(row=5, column=1, pady=2)

        tk.Button(form_frame, text="Add Task", font=("Arial", 12), bg="#2196F3", fg="white", command=self.add_task).grid(row=6, column=0, columnspan=2, pady=10)

        tk.Label(left_frame, text="Scheduled Tasks", font=("Arial", 14), bg="#f0f2f5").pack(pady=(10, 5))
        self.task_listbox = tk.Listbox(left_frame, font=("Arial", 11), width=60, height=6)
        self.task_listbox.pack()

        button_frame = tk.Frame(left_frame, bg="#f0f2f5")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Start Scheduler", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.start_scheduler).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Stop Scheduler", font=("Arial", 12), bg="#f44336", fg="white", command=self.stop_scheduler).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear Logs", font=("Arial", 12), bg="#607D8B", fg="white", command=self.clear_logs).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear Scheduled Tasks", font=("Arial", 12), bg="#9C27B0", fg="white", command=self.clear_task_list).pack(side=tk.LEFT, padx=5)

        # RIGHT SIDE - Log
        tk.Label(right_frame, text="Task Execution Log", font=("Arial", 16), bg="#f0f2f5").pack(pady=10)
        self.log_text = tk.Text(right_frame, height=28, width=70, bg="black", fg="white", font=("Consolas", 10))
        self.log_text.pack(fill=tk.BOTH, expand=True)
        self.log_text.configure(state='disabled')

    def log(self, message):
        import datetime
        timestamp = datetime.datetime.now().strftime("[%H:%M:%S]")

        # Auto-color based on message type
        icon = ""
        color = "white"
        if "Started" in message:
            icon = "🟢"
            color = "lightgreen"
        elif "Finished" in message:
            icon = "🔴"
            color = "tomato"

        self.log_text.configure(state='normal')
        self.log_text.insert(tk.END, f"{timestamp} {icon} {message}\n", color)
        self.log_text.tag_config(color, foreground=color)
        self.log_text.see(tk.END)
        self.log_text.configure(state='disabled')

    def add_task(self):
        name = self.task_name_entry.get()
        try:
            interval = float(self.task_interval_entry.get())
            working_time = float(self.task_working_entry.get())
        except ValueError:
            self.log("Invalid time or working time.")
            return

        task_type = self.task_type.get()
        priority_str = self.task_priority.get()
        priority_map = {"High": 1, "Medium": 2, "Low": 3}
        priority = priority_map.get(priority_str, 2)

        if name and interval and working_time:
            task_str = f"{task_type}: {name} ({interval}s, working {working_time}s, priority {priority_str})"
            self.task_listbox.insert(tk.END, task_str)
            task = Task(name, interval, working_time, task_type, priority)
            self.task_objects.append(task)
            self.task_manager.add_task(task)
            self.log(f"Task added: {task_str}")
        else:
            self.log("Please enter task details correctly.")

    def start_scheduler(self):
        self.task_manager.start_all(self.log)

    def stop_scheduler(self):
        self.task_manager.stop_all()
        self.log("Scheduler stopped.")
