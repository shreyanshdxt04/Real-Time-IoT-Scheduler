Real-Time IoT Task Scheduler 🕒🔧
A Python-based real-time task scheduler with a modern GUI to manage and execute periodic and aperiodic tasks based on priority — designed for IoT systems and automation workflows.

🚀 Features
🧠 Priority-based task execution (High > Medium > Low)

⏱️ Periodic and Aperiodic task support

🛑 Preemptive-like behavior (low-priority tasks yield to high-priority ones)

📋 Intuitive GUI to add, monitor, and manage tasks

📜 Real-time execution logs with timestamps and color indicators

💡 Built using Python's threading, tkinter, and object-oriented design

📸 GUI Preview
![GUI Screenshot Placeholder - insert image here if needed]

📂 Project Structure
bash
Copy
Edit
.
├── main.py          # Entry point for the GUI application
├── gui.py           # Tkinter-based graphical interface
├── scheduler.py     # Core logic for task scheduling and priority handling
🧰 Requirements
Python 3.7+

No external dependencies (only uses built-in libraries)

🔧 How It Works
Task Creation: You can add tasks with attributes like name, time interval/delay, working time, type (Periodic/Aperiodic), and priority.

Scheduler Execution: The TaskManager class manages all tasks and initiates execution based on priority.

Interruptible Loop: Lower-priority tasks wait when high-priority tasks are running (mimicking real-time preemption).

Logging: The GUI displays colored logs of task start and finish events with timestamps.

▶️ Getting Started
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/iot-task-scheduler.git
cd iot-task-scheduler
Run the application

bash
Copy
Edit
python main.py
Add and manage tasks via GUI

📝 Example Use Case
Automate IoT device actions like sensor polling (periodic) and emergency alerts (aperiodic) with intelligent prioritization.

🛠️ Future Enhancements
Task persistence using a database or JSON

Real-time visualization of running tasks

IoT device integration via MQTT or HTTP

📃 License
MIT License – use it freely and responsibly.
