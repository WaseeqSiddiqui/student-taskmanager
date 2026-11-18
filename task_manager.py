
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")

        task = {
            "id": self.next_id,
            "title": title.strip(),
            "completed": False
        }

        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_tasks(self):
        return self.tasks
