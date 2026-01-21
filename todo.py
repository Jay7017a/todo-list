tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully.")

def update_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to update: "))
        new_task = input("Enter new task name: ")
        tasks[task_no - 1] = new_task
        print("Task updated successfully.")
    except:
        print("Invalid input.")

def delete_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        tasks.pop(task_no - 1)
        print("Task deleted successfully.")
    except:
        print("Invalid input.")

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting application.")
        break
    else:
        print("Invalid choice. Try again.")
