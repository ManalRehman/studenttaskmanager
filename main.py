
# Student Task Manager

tasks = []
next_id = 1


def add_task():
    global next_id

    title = input("Enter task title: ")

    task = {
        "id": next_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    next_id += 1

    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n===== YOUR TASKS =====")

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"

        print(f'ID: {task["id"]}')
        print(f'Title: {task["title"]}')
        print(f'Status: {status}')
        print("----------------------")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_id = int(input("Enter task ID to complete: "))

        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print("Task marked as completed!")
                return

        print("Invalid task ID!")

    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_id = int(input("Enter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                print("Task deleted successfully!")
                return

        print("Invalid task ID!")

    except ValueError:
        print("Please enter a valid number!")


def main():
    while True:
        print("\n" + "=" * 40)
        print("       STUDENT TASK MANAGER")
        print("=" * 40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()
        
        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Thank you for using Student Task Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
