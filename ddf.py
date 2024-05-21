# Function to display menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

# Function to add a task
def add_task():
    task_name = input("Enter task name: ")
    with open("tasks.txt", "a") as file:
        file.write(task_name + "\n")
    print("Task added successfully!")

# Function to view tasks
def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\nTasks:")
                for task in tasks:
                    print(task.strip())
            else:
                print("No tasks available.")
    except FileNotFoundError:
        print("No tasks available.")

# Function to mark a task as complete
def mark_task_complete():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if tasks:
            view_tasks()
            task_index = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index] = tasks[task_index].strip() + " - Complete\n"
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print("Task marked as complete.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks available.")
    except FileNotFoundError:
        print("No tasks available.")

# Function to delete a task
def delete_task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if tasks:
            view_tasks()
            task_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                del tasks[task_index]
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print("Task deleted.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks available.")
    except FileNotFoundError:
        print("No tasks available.")

# Main program
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 5.")
