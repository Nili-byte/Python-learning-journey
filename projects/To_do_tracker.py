print("---------- To-Do Tracker ----------")
lists = []


def add_task():
    print("---------- Add a Task ----------")
    task = input("Enter the task: ")
    lists.append(task)
    print(f"Task '{task}' added successfully.")


def view_tasks():
    print("---------- View All Tasks ----------")
    if not lists:
     print("The lists is empty.")

    else:
        for i,j in enumerate(lists,start=1):
            print(f"{i}.{j}")


def mark_task_completed():
    print("---------- Mark a Task as Completed ----------")
    if not lists:
        print("The lists is empty.")

    else:
        view_tasks()
        task_number = int(input("Enter the task number to mark completed:"))
        if 1 <= task_number <= len(lists):
            task = lists[task_number - 1]
            print(f"Task '{task}' marked as completed ✅")
        else:
            print("Invalid task number.")
    

def remove_task():
    print("---------- Delete a task ----------")
    if not lists:
        print("The lists is empty.")
    else:
        view_tasks()
        task_number = int(input("Enter the task number to remove: "))
        if 1<= task_number <= len(lists):
            task = lists.pop(task_number -1 )
            print(f"Task '{task}' removed successfully.")
        else:
            print("Invalid task number.")

def exit():
  
  print("Thank you for using the To-Do Tracker. Goodbye!")
 
menu()    
def menu():
 
 print("-"*20)
 
 print("1. Add a task")
 
 print("2. view all tasks")
 
 print("3. Mark a task as completed")
 
 print("4. Remove a task")
 
 print("5. Exit")
 
 print("-"*20)
 
 
 
 choice = input("Enter your choice (1-5): ")
 
 if choice == "1":
 
      add_task()
 
 elif choice == "2":
 
      view_tasks()
 
 elif choice == "3":
 
     mark_task_completed()
 
 elif choice == "4":
 
     remove_task()
 
 elif choice == "5":
 
     print("Exiting the program...")
        
            





    