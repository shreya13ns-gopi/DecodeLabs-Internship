tasks = []

while True:
    print("\n--- TO-DO-LIST ---")
    print("1 ADD TASK")
    print("2 VIEW TASK")
    print("3 EXIT")

    choice = input("enter your choice: ")

    if choice == "1":
        task = input("enter your task: ")
        tasks.append(task)
        print("task added succesfully")

    elif choice == "2":
        if len(tasks) == 0:
             print("No tasks available.")
        else:
             print("\nyour tasks:")
             for i, task in enumerate(tasks,1):
                  print(i, ".", task)

    elif choice == "3":
         print("Goodbye")
         break
    
    else:
         print("Invalid choice.Please try again.")