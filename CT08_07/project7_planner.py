import os
import time

def show_menu():
    while True:
        time.sleep(3)
        print("Menu: ")
        print('1. Create new task file')
        print('2. View all task')
        print('3. Add new task')
        print('4. delete a task')
        print('5. Mark task as done')
        print('6. EXIT')
        print()

        option = input('Enter your choice: ')
        if option == "1":
            new_task_file()
        elif option == '2':
            view_all_tasks()
        elif option == '3':
            add_task()
        elif option == '4':
            delete_task()
        elif option == '5':
            completed_task()
        elif option == '6':
            print("program exited")
            break
        else:
            print("INVALID")

def new_task_file():
    filepath = os.getcwd()
    fullpath = os.path.join(filepath, 'task.txt')
    if os.path.exists(fullpath):
        print("Task file 'task.txt' already exists.")
        option = input('Overwrite?? (y/n):')
        if option == "y":
            print("File overwritten")
            with open("task.txt","w")as file:
                file.write("My task list")
        else:
            print('File not overwritten')
    else:
        with open('tasks.txt', 'w') as file:
            file.write("My task list")
        print("task.txt has been created.")

def view_all_tasks():
    with open('tasks.txt', 'r') as file:
        content = file.readlines()
        for line in range(len(content)):
            if line == 0:
                # No numbering for the title
                print(content[line].strip())
            else:
                print(f"{line}.{content[line].strip()}")

def add_task():
    with open('tasks.txt', 'a') as file:
        new_task = input("Enter new task: ")
        file.write(f"\n{new_task}")
    print(f"{new_task} was added to the task list.")

def completed_task():
    with open("tasks.txt" , "r") as file:
        task = file.readlines()

    with open("tasks.txt" , "w") as file:
        task_num = int(input("Enter the completed task number :"))
        task[task_num]
        task = task.strip() + " (DONE\n)"
        task[task_num] = task
        file.writelines(task)

def delete_task():
    with open("tasks.txt" , "r") as file:
        task = file.readlines()

    with open("tasks.txt" , "w") as file:
        task_num = int(input("Enter what task u want to delete:"))
        task.pop(task_num)
        file.writelines(task)
    print('Task deleted sucsesfully!')


show_menu()
