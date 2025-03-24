import tkinter as tk
from iot_simulator import simulate_iot_tasks

def create_dashboard():
    root = tk.Tk()
    root.title("IoT Task Scheduler Dashboard")
    root.geometry("1000x600")  # Set default window size
    
    label = tk.Label(root, text="Real-Time IoT Task Scheduling", font=("Arial", 14))
    label.pack(pady=10)
    
    output_text = tk.Text(root, height=20, width=100)
    output_text.pack(pady=10)
    
    def run_scheduler():
        output_text.delete(1.0, tk.END)  # Clear previous output
        import sys
        from io import StringIO
        
        old_stdout = sys.stdout
        sys.stdout = buffer = StringIO()  # Redirect console output
        
        simulate_iot_tasks()  # Run scheduler
        
        sys.stdout = old_stdout  # Restore console output
        output_text.insert(tk.END, buffer.getvalue())  # Display output in GUI
    
    run_button = tk.Button(root, text="Run Scheduler", command=run_scheduler)
    run_button.pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    create_dashboard()
