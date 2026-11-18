# Student Task Manager

A simple Python console-based application developed for the **CSC418 – DevOps for Cloud Computing** assignment.

The application allows students to manage their daily tasks by adding, viewing, completing, and deleting tasks.

The main purpose of this project is to practice Git and GitHub concepts such as version control, branching, pull requests, merge conflicts, automated testing, and releases.

## Features

- **Add Task:** Add a new task with a valid title.
- **View Tasks:** Display all tasks along with their IDs and completion status.
- **Complete Task:** Mark an existing task as completed using its ID.
- **Delete Task:** Delete an existing task using its ID.
- **Input Validation:** Prevent empty task titles and handle invalid task IDs.
- **Console Interface:** Simple menu-based interface for managing tasks.

## Technologies Used

- Python 3
- Git
- GitHub
- Python unittest (automated testing)
- GitHub Actions (CI workflow)

## Project Structure

```text
student-taskmanager/
│
├── main.py
├── task_manager.py
├── README.md
├── LICENSE
├── .gitignore
├── LABREPORT.md
│
├── tests/
│   └── test_task_manager.py
│
├── docs/
│   └── userguide.md
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
└── lab-evidence/
    └── screenshots/
```

*Some files and folders are added during the later assignment parts.*

## Installation and Setup

**Step 1: Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/student-taskmanager.git
```

**Step 2: Open the project directory**

```bash
cd student-taskmanager
```

**Step 3: Run the application**

```bash
python main.py
```

Python 3 must be installed on your computer. No additional Python packages are required.

## How to Use

After running the application, the following menu appears:

```text
===== STUDENT TASK MANAGER =====

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit

Enter your choice:
```

### 1. Add Task

Select option `1` and enter a task title.

```text
Enter task title: Complete DevOps Assignment
Task 1 added successfully!
```

An empty title is rejected.

### 2. View Tasks

Select option `2` to display all tasks.

```text
1. Complete DevOps Assignment - Pending
2. Prepare for Exam - Pending
```

### 3. Complete Task

Select option `3` and enter the task ID.

```text
Enter task ID to complete: 1
Task marked as completed!
```

The task status changes from Pending to Completed.

### 4. Delete Task

Select option `4` and enter the task ID.

```text
Enter task ID to delete: 2
Task deleted successfully!
```

### 5. Exit

Select option `5` to close the application.

## Git and GitHub Workflow

This project follows a feature-based development workflow.

The main branches used are:

- `main` – Main project branch
- `feature/addtask` – Task title validation
- `feature/completetask` – Task completion functionality
- `feature/deletetask` – Task deletion functionality
- `docs/update-readme` – Documentation improvements

Each feature is developed on a separate branch and integrated into the main branch through a GitHub Pull Request.

GitHub Issues are used to track project tasks, and Pull Requests are used to review changes before merging.

## Automated Testing

The project uses Python's built-in `unittest` framework.

The automated tests cover:

1. Adding a task
2. Completing a task
3. Deleting a task

To run the tests, execute:

```bash
python -m unittest discover -s tests -v
```

A GitHub Actions workflow is configured in `.github/workflows/tests.yml` to run the tests automatically whenever code is pushed to `main` or a Pull Request targets `main`.

## Documentation

More detailed instructions are available in:

`docs/userguide.md`

## Release

The first stable version of the project will be published as **v1.0.0** using GitHub Releases.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

Project status: Development