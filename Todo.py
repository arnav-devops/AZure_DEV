def add_task(todo_list):
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Task added successfully!")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def delete_task(todo_list):
    view_tasks(todo_list)
    if not todo_list:
        return 
    task_number = int(input("Enter the task number to delete:"))
    if task_number <= len(todo_list):
                del todo_list[task_number - 1]
                print("Task deleted successfully!")
    else:
                print("Invalid task number.")

def main():
    todo_list = []
    while True:
        print("\nTodo List MEnue")
        print("1. Add Task")
        print("2. View Tasks")

        choice = input("Enter choice: ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
        main()
    
