# Student Task Manager – User Guide

## 1. Introduction

Student Task Manager is a Python console application that helps students manage their academic tasks. Users can add, view, complete, and delete tasks through a simple menu.

## 2. Requirements

- Python 3 installed on your computer.
- Git installed to clone the repository.

## 3. Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Hamna0598/studenttaskmanager.git
   ```

2. Open the project folder:

   ```bash
   cd studenttaskmanager
   ```

3. Start the application:

   ```bash
   python app.py
   ```

## 4. Main Menu

When the application starts, the following menu appears:

1. Add Task
2. Display Tasks
3. Complete Task
4. Delete Task
5. Exit

Enter the number of your preferred option.

## 5. Managing Tasks

### Add Task

- Select option 1.
- Enter a task title.
- The application checks that the title is not empty.
- A success message appears when the task is added.

### Display Tasks

- Select option 2.
- All available tasks are displayed with their IDs, titles, and statuses.
- Tasks are shown as Pending or Completed.

### Complete Task

- Select option 3.
- Enter the ID of the task you want to complete.
- The application validates the task ID.
- A success message appears when the task is completed.

### Delete Task

- Select option 4.
- Enter the ID of the task you want to delete.
- Confirm deletion by entering `y`.
- Enter `n` to cancel deletion.

### Exit

- Select option 5 to close the application.

## 6. Running Unit Tests

The project includes automated tests for the main task operations.

Run the following command from the project directory:

```bash
python -m unittest discover -s tests -v
```

The tests check task creation, task completion, and task deletion.

## 7. Troubleshooting

- **Python is not recognized:** Make sure Python is installed and added to PATH.
- **Task not found:** Check that you entered an existing task ID.
- **Invalid task ID:** Enter a numeric ID.
- **No tasks available:** Add a task before trying to complete or delete one.

## 8. Conclusion

Student Task Manager provides a simple way to organize academic tasks. Its validation features and automated unit tests help make task management more reliable.