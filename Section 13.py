"""Default Argument
We improve the code by making the filepath a default argument with the ability to change it if we want when calling the function.
Order is important, Default parameters are always at the end when defining a function, they can not be before any non-default parameter
"""


def get_todo_list(filepath="files/todos.txt"):  ## Setting the filepath as a default paramenter so we do not have to add it everytime we call this function, however, this default parameter can be changed if we decided to enter a file path when calling the function.
    with open(filepath) as file:
        todoTxtFile = file.readlines()
        return todoTxtFile


def set_todo_list(set_list, filepath="files/todos.txt"):  ## Default parameters must be at the end of the function, and not have any non-default parameters after them in order to work properly.
    with open(filepath, "w") as file:
        file.writelines(set_list)


userPrompt = "Enter a To Do Item: "
userPromptSelection = ("\nType Command: add | complete | edit | show | exit\n"
                       "Command: ")

while True:
    userAction = input(userPromptSelection).lower().strip()

    if userAction.startswith("add"):
        try:
            todo = userAction[4:].capitalize() + "\n"

            if len(todo) < 5:
                print("You did not enter any task. Try Again!")
                continue

            todoList = get_todo_list()

            todoList.append(todo)

            set_todo_list(todoList)

            print("ToDo item Added!")
        except ValueError:
            print("Command Argument is invalid")
            continue

    elif userAction.startswith("complete"):
        try:
            todoList = get_todo_list()

            while True:
                taskNumber = int(userAction[9:]) - 1
                confirm = input(
                    f"Are you sure you want to mark '{todoList[taskNumber].strip("\n")}' as complete. Enter Y/N: ").lower().strip()  #
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

            set_todo_list(todoList)

        except ValueError:
            print("Command Argument is invalid")
            continue

        except IndexError:
            print("The number entered is not in the list")
            continue

    elif userAction.startswith("edit"):
        try:
            todoList = get_todo_list()

            print("ToDo List:")

            for index, task in enumerate(todoList):
                task = task.strip("\n")
                print(f"{index + 1}. {task}")

            taskNumber = int(userAction[5:]) - 1
            print("\nTask selected: ", todoList[taskNumber])
            newTodo = input("Enter the new Todo Task: ") + "\n"
            todoList[taskNumber] = newTodo.capitalize()
            print("list Updated!")

            set_todo_list(todoList)

        except ValueError:
            print("Command Argument is invalid")
            continue

        except IndexError:
            print("The number entered is not in the list")
            continue

    elif userAction.startswith("show"):
        todoList = get_todo_list()

        for index, task in enumerate(todoList):
            task = task.strip("\n")
            print(f"{index + 1}. {task}")

    elif userAction.startswith("exit"):
        break

    else:
        print("Incorrect Command")

print("Good Bye")
