
import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Complete Assignment")

        self.assertEqual(task["title"], "Complete Assignment")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.manager.get_tasks()), 5)

    def test_complete_task(self):
        task = self.manager.add_task("Study DevOps")

        result = self.manager.complete_task(task["id"])

        self.assertTrue(result)
        self.assertTrue(task["completed"])

    def test_delete_task(self):
        task = self.manager.add_task("Prepare Notes")

        result = self.manager.delete_task(task["id"])

        self.assertTrue(result)
        self.assertEqual(len(self.manager.get_tasks()), 0)


if __name__ == "__main__":
    unittest.main()
