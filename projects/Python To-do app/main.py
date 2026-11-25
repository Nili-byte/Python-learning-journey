print("------------Welcome to To-Do-App-------------")
tasks = []
def menu():
    print("1. Add Task")
    print("2. view Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
   taski = input("Enter a task to add : ")
   tasks.append({"task":taski,"done":False})
   print(f"Task : {taski} added!")

def view_task():
    if not tasks:
        print("Task List empty !")
        return
    for i , task in enumerate(tasks,start=1):
        
        status = "✅" if task["done"] else "❌"
        
     
        
        print(f"{i}. {task['task']} --- {status} ")

def mark_task():
    if not tasks:
        return
    else:
        view_task()
        inn = int(input("Enter the task number to mark as completed")) - 1
        if 0<inn>=len(tasks):
         tasks[inn]["done"]=True
         print("Task marked as completed sucessfully!")
        else:   
        
         print("Invalid integer")


def delete():
    if not tasks:
        return
    else:
        view_task()
        ind = int(input("Enter a task number to remove !"))-1
        if 0<ind<len(tasks):
            tasks.pop(ind)
            print("Task deleted !")

def exit():
    print("Thankyou for using our app")





while True:
    menu()
    choice = int(input("Enter the option (1-5) : "))
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        mark_task()
    elif choice == 4:
        delete()
    elif choice == 5:
        exit()







