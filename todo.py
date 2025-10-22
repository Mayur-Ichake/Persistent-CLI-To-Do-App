# Task : Create a To-Do List Application (Console-based )
# This application allows users to add, view, and delete tasks from their to-do list.
""" Hints/Mini Guide:
 1.Use lists to store tasks
 2.Implement add/remove/view functionality
 3.Store tasks in a text file using open()"""

# Load tasks from todo_list.txt file
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]

    except FileNotFoundError:
        tasks = []
    return tasks

# save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# add a new task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f'Task "{task}" added.')

# view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for todo, task in enumerate(tasks, start=1):
            print(f"{todo}. {task}")

# delete a task
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

# main function to run the to-do list application
def main():
    filename = 'todo_list.txt'           # save tasks in this file
    tasks = load_tasks(filename)
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        # take user input
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_task(tasks)
            save_tasks(filename, tasks)
        elif choice == '2':
            view_tasks(tasks)
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

