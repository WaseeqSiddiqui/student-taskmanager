
import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Complete Assignment")

        self.assertEqual(task["title"], "Complete Assignment")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.manager.get_tasks()), 1)
        self.assertEqual(task["id"], 1)

    def test_reject_invalid_titles_without_changing_tasks(self):
        for title in ("", "   ", "\t\n", None, 42):
            with self.subTest(title=title):
                with self.assertRaises(ValueError):
                    self.manager.add_task(title)
                self.assertEqual(self.manager.get_tasks(), [])
        self.assertEqual(self.manager.add_task("Valid task")["id"], 1)

    def test_trim_title(self):
        task = self.manager.add_task("  Read notes  ")
        self.assertEqual(task["title"], "Read notes")

    def test_complete_task(self):
        task = self.manager.add_task("Study DevOps")

        result = self.manager.complete_task(task["id"])

        self.assertTrue(result)
        self.assertTrue(task["completed"])

    def test_complete_only_selected_task(self):
        first = self.manager.add_task("First")
        second = self.manager.add_task("Second")
        self.assertTrue(self.manager.complete_task(second["id"]))
        self.assertFalse(first["completed"])
        self.assertTrue(second["completed"])

    def test_complete_missing_task(self):
        self.assertFalse(self.manager.complete_task(1))
        task = self.manager.add_task("Existing")
        self.assertFalse(self.manager.complete_task(999))
        self.assertFalse(task["completed"])

    def test_complete_already_completed_task(self):
        task = self.manager.add_task("Existing")
        self.assertTrue(self.manager.complete_task(task["id"]))
        self.assertTrue(self.manager.complete_task(task["id"]))

    def test_delete_task(self):
        task = self.manager.add_task("Prepare Notes")

        result = self.manager.delete_task(task["id"])

        self.assertTrue(result)
        self.assertEqual(len(self.manager.get_tasks()), 0)

    def test_delete_preserves_other_tasks_and_unique_ids(self):
        first = self.manager.add_task("First")
        second = self.manager.add_task("Second")
        self.assertTrue(self.manager.delete_task(first["id"]))
        self.assertEqual(self.manager.get_tasks(), [second])
        self.assertFalse(self.manager.complete_task(first["id"]))
        self.assertEqual(self.manager.add_task("Third")["id"], 3)

    def test_delete_missing_task(self):
        self.assertFalse(self.manager.delete_task(1))
        task = self.manager.add_task("Existing")
        self.assertFalse(self.manager.delete_task(999))
        self.assertEqual(self.manager.get_tasks(), [task])


if __name__ == "__main__":
    unittest.main()
