"""If Else statements
currently, user needs to press enter then add the to do item, and press enter again, we want to be able to do this in a simple prompt, without the need to press enter multiple times.
match case statement looks for patterns such as string and does not allow operating expressions, this is where if else comes in, which allows expressions as well.
To accomplish this, we will use the "in" expression as well as slice strings to remove the command from user input.
"""
userPrompt = "Enter a To Do Item: "
userPromptSelection = ("\nType Command: add | complete | edit | show | exit\n"
                       "Command: ")

while True:
    userAction = input(userPromptSelection).lower().strip()

    ## We replace match case with if else statements

    if "add " in userAction[:4]:  ## this expression checks for the command in the sliced version of the string, defining the slice end index based on the length of the command.
        todo = userAction[4:].capitalize() + "\n"  ## this expression adds only the intended task from the sliced version of the string, defining the slice start index based on the length of the command and space.

        with open("files/todos.txt", "r") as file:
            todoList = file.readlines()

        todoList.append(todo)

        with open("files/todos.txt", "w") as file:
            file.writelines(todoList)

        print("ToDo item Added!")

    elif "complete " in userAction[:9]:  ## this expression checks for the command in the sliced version of the string, defining the slice end index based on the length of the command.
        """ My Logic """
        with open("files/todos.txt", "r") as file:
            todoList = file.readlines()

        while True:
            taskNumber = int(userAction[9:]) - 1  ## this expression adds only the intended task from the sliced version of the string, defining the slice start index based on the length of the command and space.
            confirm = input(
                f"Are you sure you want to mark '{todoList[taskNumber].strip("\n")}' as complete. Enter Y/N: ").lower().strip()  ##
            match confirm:
                case "y":
                    todoList.pop(taskNumber)
                    print("Done!")
                    break
                case "n":
                    print("Try again")
                    break
                case _:
                    print("Only enter y for yes or n for no, Select task again")

        with open("files/todos.txt", "w") as file:
            file.writelines(todoList)

    elif "edit " in userAction[:5]:  ## this expression checks for the command in the sliced version of the string, defining the slice end index based on the length of the command.
        """ My logic """

        with open("files/todos.txt", "r") as file:
            todoList = file.readlines()

        print("ToDo List:")

        for index, task in enumerate(todoList):
            task = task.strip("\n")
            print(f"{index + 1}. {task}")

        taskNumber = int(userAction[5:]) - 1 ## this expression adds only the intended task from the sliced version of the string, defining the slice start index based on the length of the command and space.
        print("\nTask selected: ", todoList[taskNumber])
        newTodo = input("Enter the new Todo Task: ") + "\n"
        todoList[taskNumber] = newTodo.capitalize()
        print("list Updated!")

        with open("files/todos.txt", "w") as file:
            file.writelines(todoList)

    elif "show" in userAction[:4]:  ## this expression checks for the command in the sliced version of the string, defining the slice end index based on the length of the command.
        with open("files/todos.txt", "r") as file:
            todoList = file.readlines()

        for index, task in enumerate(todoList):
            task = task.strip("\n")
            print(f"{index + 1}. {task}")

    elif "exit" in userAction[:4]:  ## this expression checks for the command in the sliced version of the string, defining the slice end index based on the length of the command.
        break

    else:
        print("Incorrect Command")

print("Good Bye")
