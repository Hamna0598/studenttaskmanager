
tasks = []

def display_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n===== YOUR TASKS =====")

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f'ID: {task["id"]} | {task["title"]} | {status}')


def add_task():
    title = input("Enter task title: ")

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def complete_task():
    display_tasks()

    if not tasks:
        return

    try:
        task_id = int(input("\nEnter task ID to complete: "))
    except ValueError:
        print("Error: Please enter a valid numeric task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("This task is already completed.")
                return

            task["completed"] = True
            print("Task completed successfully!")
            return

    print("Task not found.")


def delete_task():
    display_tasks()

    task_id = int(input("\nEnter task ID to delete: "))

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            return

    print("Task not found.")


def main():
    while True:
        print("\n===== STUDENT TASK MANAGER =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using Student Task Manager!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
