import threading
import time

PRIORITY_MAP = {
    'High': 1,
    'Medium': 2,
    'Low': 3
}

class Task:
    def __init__(self, name, interval, working_time, task_type, priority):
        self.name = name
        self.interval = interval
        self.working_time = working_time
        self.task_type = task_type
        self.priority = priority
        self.running = False
        self.thread = None
        self._stop_event = threading.Event()
        self.pause_event = threading.Event()
        self.pause_event.set()
        self.executed = False  # Only for aperiodic

    def run(self, log_callback, task_manager):
        self.running = True

        if self.task_type == "Periodic":
            while not self._stop_event.is_set():
                self._check_and_wait_high_priority(task_manager)
                log_callback(f"[{self.name}] ▶ Started (Periodic, Priority {self.priority})")
                self._wait_with_interrupt(self.working_time)
                log_callback(f"[{self.name}] ◼ Finished after {self.working_time}s")
                start_time = time.time()
                self._wait_with_interrupt(self.interval - (time.time() - start_time))
        else:
            if self.executed:
                return  # prevent multiple runs
            self._wait_with_interrupt(self.interval)
            if self._stop_event.is_set():
                return
            self._check_and_wait_high_priority(task_manager)
            log_callback(f"[{self.name}] ▶ Started (Aperiodic, Priority {self.priority})")
            self._wait_with_interrupt(self.working_time)
            log_callback(f"[{self.name}] ◼ Finished after {self.working_time}s")
            self.executed = True

        self.running = False

    def _wait_with_interrupt(self, duration):
        end_time = time.time() + duration
        while time.time() < end_time:
            if self._stop_event.is_set():
                break
            self.pause_event.wait(timeout=0.1)

    def _check_and_wait_high_priority(self, task_manager):
        # Only pause if this task is Low priority (3)
        if self.priority == 3:
            while any(task.priority == 1 and task.running for task in task_manager.tasks):
                self.pause_event.clear()
                time.sleep(0.1)
            self.pause_event.set()

    def start(self, log_callback, task_manager):
        if self.task_type == 'Aperiodic' and self.executed:
            return
        self._stop_event.clear()
        self.pause_event.set()
        self.thread = threading.Thread(target=self.run, args=(log_callback, task_manager), daemon=True)
        self.thread.start()

    def stop(self):
        self._stop_event.set()
        self.pause_event.set()
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
        self.running = False


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.lock = threading.Lock()
        self.scheduler_thread = None
        self.running = False

    def add_task(self, task):
        with self.lock:
            self.tasks.append(task)

    def start_all(self, log_callback):
        if self.running:
            return
        self.running = True
        self.scheduler_thread = threading.Thread(target=self.scheduler_loop, args=(log_callback,), daemon=True)
        self.scheduler_thread.start()

    def scheduler_loop(self, log_callback):
        while self.running:
            with self.lock:
                ready_tasks = [t for t in self.tasks if not t.running]
                ready_tasks.sort(key=lambda t: t.priority)
                for task in ready_tasks:
                    task.start(log_callback, self)
            time.sleep(0.5)

    def stop_all(self):
        self.running = False
        if self.scheduler_thread and self.scheduler_thread.is_alive():
            self.scheduler_thread.join(timeout=2)
        with self.lock:
            for task in self.tasks:
                task.stop()
