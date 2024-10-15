""" Importing and using standard/builtin modules.
Most of the actions and processes, not counting highly customized functions you create for your own program, have been developed as functions by python's team as well as third parties. For example you can use timestamp functionality using builtin time module.
You can find and learn about any type of function by having an understanding of how python works.
"""
import functions
import time  ## Located in directory where the python interpreter is installed

timeNow = time.strftime("%H:%M:%S")  ## We add a time stamp
dateNow = time.strftime("%d, %b,:%Y")  ## We add a date stamp
print(f"Time: {timeNow} | Date: {dateNow}")

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

            todoList = functions.get_todo_list()

            todoList.append(todo)

            functions.set_todo_list(todoList)

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
