""" List comprehension
Instead of using a for loop separately, the pythonic way of doing is it is by using the list comprehension with for loop inside it. all in a single line
"""

userPrompt = "Enter a To Do Item: "
userPromptSelection = "Type add or complete or edit or show or exit: "

while True:
    userAction = input(userPromptSelection).lower().strip()

    match userAction:

        case "add":
            todo = input(userPrompt).capitalize() + "\n"

            file = open("files/todos.txt", "r")
            todoList = file.readlines()
            file.close()

            todoList.append(todo)

            file = open("files/todos.txt", "w")
            file.writelines(todoList)
            file.close()

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
            file = open("files/todos.txt", "r")
            todoList = file.readlines()
            file.close()

            newTodoList = [item.strip("\n") for item in todoList]  ## Using list comprehension to removing break line by creating a new list variable, using strip method, and iterating with for loop, all in a single line.
            for index, task in enumerate(newTodoList):
                print(f"{index + 1}. {task}")

        case "exit":
            break

print("Good Bye")
