#create an empty list of task
tasks = []

#main menu and welcome screen
def show_menu():
    print("""
    Welcome to "To Do List App"
    Here you can add, view, and delete tasks.

    Select 1 to add a task
    Select 2 to view tasks
    Select 3 to delete a task
    Select Q to quit
    """)
    


#function to add task
def add_task(tasks):
    task = input("Please enter what task you want to add to the To Do List apps?  ")
    if task == "":
        print("enter a task")
    else:
        tasks.append(task)
        print(f'Task "{task}" added successfully!')
        print(f'here is your tasks summary {tasks}')
    

#function to view tasks
def view_task(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    
    

#function to delete task
def delete_task(tasks):
    if not tasks:
        print('no tasks to delete')
        return
    #print and enumerate the index
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")
    try:
        delete = int(input("Select the number of the task you want to delete  "))
        #in python index start from 0 so we need to make the index number match
        index = delete - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f'Task "{removed}" deleted.')
            print(f'your remaining tasks is {tasks}')
        else:
            print('invalid input')
    except ValueError:
        print('please enter a valid number')


def main():
    while True:
        show_menu()
        option = input('Please enter your option  ').upper().strip(' ') #try to avoid any lowercase or empty space added
        if option == '1':
            add_task(tasks)
        elif option == '2':
            view_task(tasks)
        elif option == '3':
            delete_task(tasks)
        elif option == 'Q':
            print("thank you for using To Do Apps")
            break
        else:
            print('enter a valid option!')

if __name__ == "__main__":
    main()
