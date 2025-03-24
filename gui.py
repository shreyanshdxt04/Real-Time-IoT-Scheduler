import tkinter as tk

def create_dashboard():
    root = tk.Tk()
    root.title("IoT Task Scheduler Dashboard")
    
    label = tk.Label(root, text="Real-Time IoT Task Scheduling", font=("Arial", 14))
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    create_dashboard()
