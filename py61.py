tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == 2:
        print("Your Tasks:")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

    elif choice == 3:
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
            print("Task removed.")
        else:
            print("Invalid task number.")

    elif choice == 4:
        break