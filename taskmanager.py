tasks = []

def display_menu():
    print("Choose number: ")
    print("   1. Add Task")
    print("   2. Edit Task")
    print("   3. Delete")
    print("   4. View Task")
    print("   5. Exit")

def add_task():
    task_name = input("Enter task name: ")
    due = input("Enter task due: ")
    status = input("Enter tas status: ")
    tasks.append(
        {
            "task_name": task_name,
            "due": due,
            "status": status
        })
    print("")
    print("Task added successfully !!!\n")
    
def view_task():
    if not tasks:
        print("\nNo task available\n")
        return
    for index, task in enumerate(tasks, start = 1):
        print("\nTask index:", index)
        print(f"   Task name: {task['task_name']} ")
        print(f"   Task Due: {task['due']}")
        print(f"   Task Status: {task['status']}\n")

def update_task():
    if not tasks:
        print("\nNo task available\n")
        return
    view_task()
    task_index = int(input("Enter the index you want to update: ")) - 1
    if 0<= task_index < len(tasks):
        task = tasks[task_index]
        task['taskname'] = input(f"Enter new task name: (curent: {task['task_name']}) : ") or task['task_name']
        task['due'] = input(f"Enter new task due: (curent: {task['due']}) : ") or task['due']
        task['status'] = input(f"Enter new task status: (curent: {task['status']}) : ") or task['status']
        print("\nTask Updated Successfully !!\n")
    else:
        print("Invalid task Number!!!")
    

def delete_task():
    if not tasks:
        print("\nNo task available\n")
        return
    view_task()
    task_index = int(input("Enter the index you want to delete: ")) - 1
    print("")
    if 0<= task_index < len(tasks):
        tasks.pop(task_index)
        print("Task deleted successfully!!!")
    else:
        print("Invalid task index!!!")
    
# end def

while True:
    display_menu()
    choice = int(input("Enter a number: "))
    
    if (choice == 1):
        add_task()
    elif (choice == 2):
        update_task()
    elif (choice == 3):
        delete_task()
    elif (choice == 4):
        view_task()
    else:
        break
