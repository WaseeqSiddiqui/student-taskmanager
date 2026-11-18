
from task_manager import TaskManager

manager = TaskManager()


def show_menu():
    print("\n===== STUDENT TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")

            try:
                task = manager.add_task(title)
                print(f"Task {task['id']} added successfully!")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            tasks = manager.get_tasks()

            if not tasks:
                print("No tasks available.")
            else:
                for task in tasks:
                    status = "Completed" if task["completed"] else "Pending"
                    print(f"{task['id']}. {task['title']} - {status}")

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))

                if manager.complete_task(task_id):
                    print("Task marked as completed!")
                else:
                    print("Task not found.")

            except ValueError:
                print("Please enter a valid numeric task ID.")

        elif choice == "4":
            print("Delete task feature coming soon.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
