import os

def show_menu():
    print("Menu: ")
    print('1. Create new task file')
    print('2. View all task')
    print('3. Add new task')
    print('4. delete a task')
    print('5. Mark task as done')
    print('6. EXIT')
    print()

    choice = input('Enter your choice: ')
    return choice

def new_task_file():
    filepath = os.getcwd
    fullpath = os.path.join(filepath, 'task.txt')
    if os.path.exists(fullpath):
        print("Task file 'task.txt' already exists.")
        option = input('Overwrite?? (y/n):')
        if option == "y":
            print("file overwritten")
        else:
            print('file not overwritten')
    else:
        print('no')

def view_all_tasks():
    with open('tasks.txt', 'r') as file:
        content = file.readlines()
        for line in content:
            print(line.strip())

 
