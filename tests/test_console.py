import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class TestConsole(unittest.TestCase):
    def run_console(self, commands):
        result = subprocess.run(
            [sys.executable, "main.py"],
            cwd=PROJECT_ROOT,
            input=commands,
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        return result.stdout

    def test_task_lifecycle(self):
        output = self.run_console("1\nStudy DevOps\n2\n3\n1\n2\n4\n1\n2\n5\n")
        for message in (
            "Task 1 added successfully!",
            "1. Study DevOps - Pending",
            "Task marked as completed!",
            "1. Study DevOps - Completed",
            "Task deleted successfully!",
            "No tasks available.",
            "Goodbye!",
        ):
            with self.subTest(message=message):
                self.assertIn(message, output)

    def test_invalid_input_recovers_to_menu(self):
        output = self.run_console("1\n   \n3\nabc\n3\n999\n4\nabc\n4\n999\n9\n5\n")
        self.assertIn("Error: Task title cannot be empty.", output)
        self.assertEqual(output.count("Please enter a valid numeric task ID."), 2)
        self.assertEqual(output.count("Task not found."), 2)
        self.assertIn("Invalid choice. Please try again.", output)
        self.assertIn("Goodbye!", output)


if __name__ == "__main__":
    unittest.main()
