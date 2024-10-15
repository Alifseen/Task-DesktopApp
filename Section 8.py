"""
Updating the edit and complete functionality to interact with the to do list text file as well
"""

userPrompt = "Enter a To Do Item: "
userPromptSelection = "Type add or complete or edit or show or exit: "

while True:
    userAction = input(userPromptSelection).lower().strip()

    match userAction:

        case "add":
            todo = input(userPrompt).capitalize() + "\n"

            with open("files/todos.txt", "r") as file:
                todoList = file.readlines()

            todoList.append(todo)

            with open("files/todos.txt", "w") as file:
                file.writelines(todoList)

        case "complete":
            """ My Logic """
            with open("files/todos.txt", "r") as file:  ## reads the tasks from the text file, saves them in python variable and prints them
                todoList = file.readlines()
            for index, task in enumerate(todoList):
                task = task.strip("\n")
                print(f"{index + 1}. {task}")

            while True:
                taskNumber = int(input("Enter the task number from the Task list you want to mark as complete: ")) - 1
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

            with open("files/todos.txt", "w") as file:  ## writes the new list in the text file
                file.writelines(todoList)

        case "edit":
            """ My logic """
            with open("files/todos.txt", "r") as file:  ## reads the tasks from the text file, saves them in python variable and prints them
                todoList = file.readlines()
            for index, task in enumerate(todoList):
                task = task.strip("\n")
                print(f"{index + 1}. {task}")

            taskNumber = int(input("Enter the task number from the Task list you want to edit: ")) - 1
            print("Task selected: ", todoList[taskNumber])
            newTodo = input("Enter the new Todo Task: ") + "\n"
            todoList[taskNumber] = newTodo.capitalize()
            print("list Updated!")

            with open("files/todos.txt", "w") as file:  ## writes the new list in the text file
                file.writelines(todoList)

        case "show":
            with open("files/todos.txt", "r") as file:
                todoList = file.readlines()

            for index, task in enumerate(todoList):
                task = task.strip("\n")
                print(f"{index + 1}. {task}")

        case "exit":
            break

print("Good Bye")
