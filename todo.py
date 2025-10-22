# Task : Create a To-Do List Application (Console-based )
# This application allows users to add, view, and delete tasks from their to-do list.
""" Hints/Mini Guide:
 1.Use lists to store tasks
 2.Implement add/remove/view functionality
 3.Store tasks in a text file using open()"""

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]

    except FileNotFoundError:
        tasks = []
    return tasks
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f'Task "{task}" added.')
def view_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task}" deleted.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def main():
    filename = 'todo_list.txt'
    tasks = load_tasks(filename)
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(filename, tasks)
        elif choice == '3':
            delete_task(tasks)
            save_tasks(filename, tasks)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

