# Student Task Manager

## Project Description

Student Task Manager is a Python-based console application designed to help students organize and manage their daily academic tasks. It provides simple options to add, display, complete, and delete tasks.

## Features

- Add new tasks with title validation.
- Display all available tasks.
- Mark pending tasks as completed.
- Prevent tasks from being completed more than once.
- Delete tasks with confirmation.
- Validate task IDs before completing or deleting tasks.
- Display task status (Pending or Completed).

## Technologies Used

- Python 3
- Git
- GitHub
- GitHub Actions
- Python unittest framework

## Project Structure

```text
studenttaskmanager/
│
├── app.py
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── docs/
│   └── userguide.md
├── README.md
├── LICENSE
└── .gitignore
```

## Setup Instructions

1. Install Python 3.
2. Clone this repository:

   ```bash
   git clone https://github.com/Hamna0598/studenttaskmanager.git
   ```

3. Open the project directory:

   ```bash
   cd studenttaskmanager
   ```

4. Run the application:

   ```bash
   python app.py
   ```

## Usage

Run the application and select an option from the menu:

1. Add Task
2. Display Tasks
3. Complete Task
4. Delete Task
5. Exit

Follow the instructions displayed in the console to manage your tasks.

## Running Unit Tests

The project includes three unit tests for adding, completing, and deleting tasks.

Run all tests using:

```bash
python -m unittest discover -s tests -v
```

## Continuous Integration

GitHub Actions automatically runs the unit tests when code is pushed to the `main` branch or when a pull request targets `main`.

The workflow is configured in:

`.github/workflows/python-tests.yml`

## Documentation

For detailed instructions on using the application, see [User Guide](docs/userguide.md).

## License

This project is licensed under the MIT License.

## Project Status

Project status: In Development (Testing in progress).