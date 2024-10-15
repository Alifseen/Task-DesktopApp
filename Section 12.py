"""Custom Functions with Multiple arguments.
Arguments are inputs that function need to be performed operations. argument value is based on the parameters defined in the function

"""


def get_todo_list(filepath):  ## we can change the file path to a variable as well as the mode into a variable.
    with open(filepath) as file:
        todoTxtFile = file.readlines()
        return todoTxtFile


def set_todo_list(filepath, set_list):  ## This is a procedural function and does not need to be assigned to a variable or return anything because it just performs a series of actions to a file
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

            todoList = get_todo_list("files/todos.txt")  ## Calling custom function with an argument

            todoList.append(todo)

            set_todo_list("files/todos.txt", todoList)

            print("ToDo item Added!")
        except ValueError:
            print("Command Argument is invalid")
            continue

    elif userAction.startswith("complete"):
        try:
            todoList = get_todo_list("files/todos.txt")

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

            set_todo_list("files/todos.txt", todoList)

        except ValueError:
            print("Command Argument is invalid")
            continue

        except IndexError:
            print("The number entered is not in the list")
            continue

    elif userAction.startswith("edit"):
        try:
            todoList = get_todo_list("files/todos.txt")

            print("ToDo List:")

            for index, task in enumerate(todoList):
                task = task.strip("\n")
                print(f"{index + 1}. {task}")

            taskNumber = int(userAction[5:]) - 1
            print("\nTask selected: ", todoList[taskNumber])
            newTodo = input("Enter the new Todo Task: ") + "\n"
            todoList[taskNumber] = newTodo.capitalize()
            print("list Updated!")

            set_todo_list("files/todos.txt", todoList)  ## Calling Custom funciton with 2 arguments

        except ValueError:
            print("Command Argument is invalid")
            continue

        except IndexError:
            print("The number entered is not in the list")
            continue

    elif userAction.startswith("show"):
        todoList = get_todo_list("files/todos.txt")

        for index, task in enumerate(todoList):
            task = task.strip("\n")
            print(f"{index + 1}. {task}")

    elif userAction.startswith("exit"):
        break

    else:
        print("Incorrect Command")

print("Good Bye")
