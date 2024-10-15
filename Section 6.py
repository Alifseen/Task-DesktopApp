"""Storing items in Text Files
The problem with program in section 5 is that it stores the to do list in temporary memory, which wipes out when you exit the program.
To store data permanently, we will store it text file, although we can also store this in CSV, or SQL.
We will use a file function to create a file, read its content, add those contents to a python list, and then after operating on the list, overwrite the txt file with new python list
"""
userPrompt = "Enter a To Do Item: "
userPromptSelection = "Type add or complete or edit or show or exit: "

# todoList = []  ## todoList This list is moved to the add case to get the file stored and then overwrite the new file. Note that this code will only work for adding to the list, since this variable is in the add case only.

while True:
    userAction = input(userPromptSelection).lower().strip()

    match userAction:
        case "add":
            todo = input(userPrompt).capitalize() + "\n"  ## "\n" adds a new line at the end of the string

            file = open("files/todos.txt", "r")  ## opens a file, saves it into file variable, and the file is opened in read mode, denoted by "r"
            todoList = file.readlines()  ## this method reads the file and stores it in the todolist variable.
            file.close()  ## this method closes the files so that the cursor/carrot that processes over the file character by character and is moved back to the start so it can process from the start again. It also saves up memory when file is closed.

            todoList.append(todo)  ## adds the user's input text to the list

            file = open("files/todos.txt", "w")  ## Opens the same file but this time in write mode, denoted by "w"
            file.writelines(todoList)  ## Overwrites the todolist into the text file.
            file.close()  ## Close the files to move the cursor back to start.


        case "complete":
            for task in todoList:
                print(f"{todoList.index(task) + 1}. {task}")
            while True:
                taskNumber = int(input("Enter the task number from the Task list you want to mark as complete: ")) - 1
                confirm = input(f"Are you sure you want to mark '{todoList[taskNumber]}' as complete. Enter Y/N: ").lower().strip()  ##
                match confirm:
                    case "y":
                        todoList.pop(taskNumber)
                        break
                    case "n":
                        print("Select again")
                    case _:
                        print("Only enter y for yes or n for no, Select task again")
        case "edit":
            for task in todoList:
                print(f"{todoList.index(task) + 1}. {task}")
            taskNumber = int(input("Enter the task number from the Task list you want to edit: ")) - 1
            print("Task selected: ", todoList[taskNumber])
            newTodo = input("Enter the new Todo Task: ")
            todoList[taskNumber] = newTodo.capitalize()
            print("list Updated!")
        case "show":
            file = open("files/todos.txt", "r")  ## opens the file in read mode
            todoList = file.readlines()  ## saves content in python variable as a list
            file.close()  ## clsoes the file
            for index, task in enumerate(todoList):
                task = task.replace("\n", "")  ## removes the line breaker "\n" from the string since print function already creates break lines, the insctructor used strip method highlighted but commented out below:
                # task = task.strip("\n")
                print(f"{index + 1}. {task}")
        case "exit":
            break

print("Good Bye")
