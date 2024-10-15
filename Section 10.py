"""Anticipating errors and error handling
error 1: what if instead of the task number, user enters the task itself
error 2: what if user types command anywhere else instead of start
error 3: what if the user does not anything except for the command for add
error 4: Incase of any error the program should not stop
error 5: Selecting an item that is not in the list with edit or complete command
"""
userPrompt = "Enter a To Do Item: "
userPromptSelection = ("\nType Command: add | complete | edit | show | exit\n"
                       "Command: ")

while True:
    userAction = input(userPromptSelection).lower().strip()

    # if "add " in userAction[:4]:  ## My solution was to slice the string and then check it for error 2.
    if userAction.startswith("add"):  ## instructors solution to use the startswith method for error 2.
        try:  # for error 1 and error 4, this try-except expression can be used. It tries to run a code block inside it, if it fails it moves to the except code block
            todo = userAction[4:].capitalize() + "\n"

            if len(todo) < 5:  # handles error 3
                print("You did not enter any task. Try Again!")
                continue

            with open("files/todos.txt", "r") as file:
                todoList = file.readlines()

            todoList.append(todo)

            with open("files/todos.txt", "w") as file:
                file.writelines(todoList)

            print("ToDo item Added!")
        except ValueError:  ## We can define the kind of errors we want to catch here and the corresponding code block we want to run.
            print("Command Argument is invalid")
            continue  # restarts the while loop to run again, ignoring everything that comes after "continue"

    # elif "complete " in userAction[:9]:  ## My solution was to slice the string and then check it for error 2.
    elif userAction.startswith("complete"):
        try:  ## for error 4, this try-except expression can be used. It tries to run a code block inside it, if it fails it moves to the except code block
            with open("files/todos.txt", "r") as file:
                todoList = file.readlines()

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
        except ValueError:  # For error 1
            print("Command Argument is invalid")
            continue  ## restarts the while loop to run again, ignoring everything that comes after "continue"

        except IndexError:  # for error 5
            print("The number entered is not in the list")
            continue  ## restarts the while loop to run again, ignoring everything that comes after "continue"

    # elif "edit " in userAction[:5]:  ## My solution was to slice the string and then check it for error 2.
    elif userAction.startswith("edit"):
        try:  ## for error 4, this try-except expression can be used. It tries to run a code block inside it, if it fails it moves to the except code block
            with open("files/todos.txt", "r") as file:
                todoList = file.readlines()

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
        except ValueError:  ## for error 1
            print("Command Argument is invalid")
            continue  ## restarts the while loop to run again, ignoring everything that comes after "continue"

        except IndexError:  # for error 5
            print("The number entered is not in the list")
            continue  ## restarts the while loop to run again, ignoring everything that comes after "continue"

    # elif "show" in userAction[:4]:  ## My solution was to slice the string and then check it for error 2.
    elif userAction.startswith("show"):
        with open("files/todos.txt", "r") as file:
            todoList = file.readlines()

        for index, task in enumerate(todoList):
            task = task.strip("\n")
            print(f"{index + 1}. {task}")

    # elif "exit" in userAction[:4]:  ## My solution was to slice the string and then check it for error 2.
    elif userAction.startswith("exit"):
        break

    else:
        print("Incorrect Command")

print("Good Bye")

