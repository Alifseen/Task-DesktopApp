"""Custom Functions
Object-Oriented programming allows for abstraction and reduces repetition through creation of custom functions
Functions are declared above the code (top of the script) and are initialized by "def" and end with "return"
"""
def get_todo_list():  ## we declare a custom function with code that was being repeated over and over again
    with open("files/todos.txt", "r") as file:
        todoTxtFile = file.readlines()
        return todoTxtFile

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

            todoList = get_todo_list()  ## we call that function and assign it to a local variable each place where that code was repeated

            todoList.append(todo)

            with open("files/todos.txt", "w") as file:
                file.writelines(todoList)

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

            with open("files/todos.txt", "w") as file:
                file.writelines(todoList)
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

            with open("files/todos.txt", "w") as file:
                file.writelines(todoList)
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

