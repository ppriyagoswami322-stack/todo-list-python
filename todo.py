task = []

def show_tasks():
    if len(task) == 0:
        print("No tasks available")
    else:
        print("Your tasks are:")
        i = 1
        for t in task:
            print(i,"-",t)
            i += 1
def add_task():
    t = input("Enter new task: ")
    task.append(t)
    print("Task added")

def delete_task():
    show_tasks()
    num = int(input("Enter task number to delete: "))

    if num > 0 and num<= len(task):
        task.pop(num - 1)
        print("Task deleted")
    else:
        print("Invalid number")

while True:
    print("\n1. Show tasks")
    print("2. Add tasks")
    print("3. Delete tasks")
    print("4. Exite")

    choice = input("Enter choice: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Wrong choice")  

    tasks = []

# load tasks from file
try:
    file = open("tasks.txt", "r")
    for line in file:
        tasks.append(line.strip())
    file.close()
except:
    pass


    

        
