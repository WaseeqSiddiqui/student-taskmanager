
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        task = {
            "id": self.next_id,
            "title": title,
            "completed": False
        }
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_tasks(self):
        return self.tasks
