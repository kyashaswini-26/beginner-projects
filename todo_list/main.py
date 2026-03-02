import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_FILE = os.path.join(BASE_DIR, "tasks.txt")
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(task+"\n")

def show_tasks(tasks):
    if not tasks:
        print("\n No tasks found.\n")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_no = int(input("Enter no of tasks to delete: "))
        removed = tasks.pop(task_no -1)
        save_tasks(tasks)
        print(f"Removed task: {removed}\n")
    except (ValueError, IndexError):
        print("Invalid task number.\n")

def main():
    tasks = load_tasks()

    while True:
        print("----TO-DO LIST----")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("choose an option: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()

