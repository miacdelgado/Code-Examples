taskApp =[ ]

def add_task(task):
    taskApp.append(task)
    print(f"Task '{task}' Added!")

def view_task(task):
    if not task:
        print("No task avaliable!.")
    else:
        for index, task in enumerate(taskApp, 1):
            print(f"{index}. {task}")

def remove_task(taskToBeRemoved):
    global taskApp
    inital_length = len(taskApp)
    taskApp =[task for task in taskApp if task != taskToBeRemoved]
    if len(taskApp) < inital_length:
        print(f"Task '{taskToBeRemoved}' removed")
    else:
        print(f"Task '{taskToBeRemoved}' not found")

def menu():
    active = True
    while active:
        print("\nTo-do list menu")
        print("1. Add Tasks")
        print("2. Remove Tasks")
        print("3. View Task")
        print("4. Exit")         
        choice = input("Enter your choice :")
        if choice == '1':        
            while True:
                task = input("Enter the task (or type 'done' to finish) ")
                if task.lower()=='done':
                    break
                add_task(task)
        elif choice == '2':
            taskToBeRemoved = input("Enter the task you want to remove: ")
            remove_task(taskToBeRemoved)
        elif choice == '3':
                view_task(task)
        elif choice == '4':
            print("Good bye!")
            active = False
        else:
            print("invaild choice. please choice again!")
menu()
