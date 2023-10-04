works = []

def add_work(description,due_date):
    task_id = len(works) + 1
    task = {'id': task_id, 'description': description, 'due_date': due_date, 'completed': False}
    works.append(task)

def complete_work(task_id):
    for task in works:
        if task['id'] == task_id:
            task['completed'] = True
            return

def delete_work(task_id):
    global works
    for task in works:
        if task['id'] == task_id:
            works = [task for task in works if task['id'] != task_id]
            print("Task Deleted")
            break
        else:
            print("No Such Task Available")
            break

def list_works(filter_completed=False):
    result = [task for task in works if not filter_completed or task['completed']]
    for task in result:
        print(f"Task {task['id']}: {task['description']} {'(Completed)' if task['completed'] else ''} Due Date: {task['due_date']}")

def completed_works(filter_completed=True):
    result = [task for task in works if filter_completed and task['completed']]
    for task in result:
        print(f"Task {task['id']}: {task['description']} {'(Completed)'} Due Date: {task['due_date']}")

def pending_works(filter_completed=True):
    result = [task for task in works if filter_completed or task['completed']]
    for task in result:
        if(task['completed'] == False):
            print(f"Task {task['id']}: {task['description']} {'(Pending)'} Due Date: {task['due_date']}")


while True:
    print("\nTODO LISTS")
    print("1. Add Task")
    print("2. List All Tasks")
    print("3. Complete Task")
    print("4. List Completed Tasks")
    print("5. List Pending Tasks")
    print("6. Delete Task")
    print("7. Exit")
   
    choice = input("Enter your Choice: ")

    if choice == '1':
        description = input("Enter Work Description: ")
        due_date = input("Enter Task Due_Date: ")
        add_work(description,due_date)
    elif choice == '2':
        list_works()
    elif choice == '3':
        task_id = int(input("Enter Task ID To Complete The Task: "))
        complete_work(task_id)
    elif choice == '4':
        completed_works()
    elif choice == '5':
        pending_works()
    elif choice == '6':
        task_id = int(input("Enter Task ID To Delete The Task: "))
        delete_work(task_id)
    elif choice == '7':
        break
    else:
        print("Invalid Choice... Please Try Again...")
