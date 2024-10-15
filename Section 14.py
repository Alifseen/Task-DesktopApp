""" Creative and importing Local Modules
It is better to separate the declaration of functions in a different file and import that file to be able to call them in the current script. That separate file is called a module
Syntax for that can be either importing specific functions declared from the file using "from file import function", or importing the whole file "import file" and then using function as method of that file
Note the file must be in the same directory for "import file" to work, if it is in a separate directory, we will have to use "from directoryname import file"
Importing file can be better for readability since it allows you to know where the called function is coming from if you need to change anything.
"""
# from functions import get_todo_list, set_todo_list  ## Option 1
import functions  # Option 2

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

            todoList = functions.get_todo_list()  ## Calling get to do list function as a method knowing that it is stored in functions file

            todoList.append(todo)

            functions.set_todo_list(todoList)  ## Calling set to do list function as a method knowing that it is stored in functions file

            print("ToDo item Added!")
        except ValueError:
            print("Command Argument is invalid")
            continue

    elif userAction.startswith("complete"):
        try:
            todoList = functions.get_todo_list()

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

            functions.set_todo_list(todoList)

        except ValueError:
            print("Command Argument is invalid")
            continue

        except IndexError:
            print("The number entered is not in the list")
            continue

    elif userAction.startswith("edit"):
        try:
            todoList = functions.get_todo_list()

            print("ToDo List:")

            for index, task in enumerate(todoList):
                task = task.strip("\n")
                print(f"{index + 1}. {task}")

            taskNumber = int(userAction[5:]) - 1
            print("\nTask selected: ", todoList[taskNumber])
            newTodo = input("Enter the new Todo Task: ") + "\n"
            todoList[taskNumber] = newTodo.capitalize()
            print("list Updated!")

            functions.set_todo_list(todoList)

        except ValueError:
            print("Command Argument is invalid")
            continue

        except IndexError:
            print("The number entered is not in the list")
            continue

    elif userAction.startswith("show"):
        todoList = functions.get_todo_list()

        for index, task in enumerate(todoList):
            task = task.strip("\n")
            print(f"{index + 1}. {task}")

    elif userAction.startswith("exit"):
        break

    else:
        print("Incorrect Command")

print("Good Bye")

