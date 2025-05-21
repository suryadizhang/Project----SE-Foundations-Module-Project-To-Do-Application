#create an empty list of task
tasks = []

#main menu and welcome screen
def show_menu():
    print ('welcome to "To Do List App" \nHere you can add, view and delete the task \nPlease select an option')
    print ('Please select an option')
    print ('Select 1 to add task \nSelect 2 to view task \nSelect 3 to delete task \nSelect 0 to go back to main menu \nSelect Q to quit')
    option= input('Please enter your option').upper
    if option == 1:
        add_task(tasks)
    elif option == 2:
        view_task(tasks)
    elif option == 3:
        delete_task(tasks)
    elif option == 0:
        print('you are not going anywhere!')
    elif option == Q:
        break
    else:
        print('enter a valid option!')
    
    pass



def add_task(tasks):
    pass


def view_task(tasks):
    pass


def delete_task(tasks):
    pass


def main():
    pass

if __name__ == "__main__":
    main()