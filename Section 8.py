""""with context manager
with context manager closes the file automatically.
"""

userPrompt = "Enter a To Do Item: "
userPromptSelection = "Type add or complete or edit or show or exit: "

while True:
    userAction = input(userPromptSelection).lower().strip()

    match userAction:

        case "add":
            todo = input(userPrompt).capitalize() + "\n"

            with open("files/todos.txt", "r") as file:  ## using context manager to read file
                todoList = file.readlines()

            todoList.append(todo)

            with open("files/todos.txt", "w") as file:  ## using context manager to write file
                file.writelines(todoList)

        case "complete":
            for task in todoList:
                print(f"{todoList.index(task) + 1}. {task}")
            while True:
                taskNumber = int(input("Enter the task number from the Task list you want to mark as complete: ")) - 1
                confirm = input(f"Are you sure you want to mark '{todoList[taskNumber]}' as complete. Enter Y/N: ").lower().strip()  #
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
            with open("files/todos.txt", "r") as file:  ## Using context manager to read file
                todoList = file.readlines()

            for index, task in enumerate(todoList):
                task = task.strip("\n")
                print(f"{index + 1}. {task}")

        case "exit":
            break

print("Good Bye")

