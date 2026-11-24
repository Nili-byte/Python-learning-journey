print("------------Welcome to To-Do-App-------------")
tasks = []
def menu():
    print("1. Add Task")
    print("2. view Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
   task = input("Enter a task to add : ")
   tasks.append({"tasks": task , "Done":False})
   print(f"Task : {task} added!")

def view_task():
    if not tasks:
        print("Task List empty !")
        return
    for i , task in enumerate(tasks,start=1):
       status =  "✅" if task["Done"] else "❌"
       print(f"{i}. {task} {status}")

def mark_task():
    if not tasks:
        return
    else:
        inn = int(input("Enter the task number to mark as completed")) - 1
        if 0<=inn<=len(tasks):
            tasks[inn]["Done":True]
            
        else:
            print("Invalid integer")

// incomplete






