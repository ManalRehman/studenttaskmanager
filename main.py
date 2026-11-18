
# Student Task Manager

from matplotlib.pyplot import title


tasks = []
next_id = 1


def add_task():
    global next_id

    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty!")
        return

    if len(title) < 3:
        print("Task title must contain at least 3 characters!")
        return
    
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


def main():
    while True:
        print("\n" + "=" * 40)
        print("       STUDENT TASK MANAGER")
        print("=" * 40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            print("Thank you for using Student Task Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
