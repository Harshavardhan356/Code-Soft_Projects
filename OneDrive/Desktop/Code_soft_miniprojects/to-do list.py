
# Week1
tasks = []

def show_tasks():
    print("\nYour Tasks:")
    if not tasks:
        print("No tasks yet.\n")
        return
    for i in range(len(tasks)):
        status = "✔️" if tasks[i]["done"] else "❌"
        print(f"{i+1}. {tasks[i]['task']} [{status}]")
    print()

def add_task():
    new_task = input("Enter a new task: ")
    if new_task.strip():
        tasks.append({"task": new_task, "done": False})
        print("Task added.\n")
    else:
        print("Empty task not added.\n")

def complete_task():
    show_tasks()
    try:
        idx = int(input("Which task is done? (number): "))
        if 0 < idx <= len(tasks):
            tasks[idx - 1]["done"] = True
            print("Marked as complete.\n")
        else:
            print("Invalid number.\n")
    except:
        print("Please enter a number.\n")

def delete_task():
    show_tasks()
    try:
        idx = int(input("Delete which task? (number): "))
        if 0 < idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            print(f"Deleted task: {removed['task']}\n")
        else:
            print("Invalid task number.\n")
    except:
        print("Please enter a valid number.\n")

def menu():
    while True:
        print("----- To Do List Menu -----")
        print("1 - Add Task")
        print("2 - View Tasks")
        print("3 - Mark as Done")
        print("4 - Delete Task")
        print("5 - Exit")
        choice = input("What do you want to do? (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!\n")
            break
        else:
            print("Invalid option, try again.\n")

menu()