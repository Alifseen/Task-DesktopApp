""" adding a complete feature
Allowing user to delete an item from the list by marking it as complete
"""


userPrompt = "Enter a To Do Item: "
userPromptSelection = "Type add or complete or edit or show or exit: "  ## added a "complete" prompt for the user

todoList = []

while True:
    userAction = input(userPromptSelection).lower().strip()

    match userAction:
        case "add":
            todo = input(userPrompt)
            todo = todo.capitalize()
            todoList.append(todo)
        case "complete":  ## executes the code below if the case statement matches the user prompt "complete"
            for task in todoList:  ## displays the to do list
                print(f"{todoList.index(task) + 1}. {task}")
            while True:  ## runs a loop to ask for, confirm and remove the task
                taskNumber = int(input("Enter the task number from the Task list you want to mark as complete: ")) - 1
                confirm = input(f"Are you sure you want to mark '{todoList[taskNumber]}' as complete. Enter Y/N: ").lower().strip()  ## confirms if the task is the correct one to be removed, accepts only y and n for yes or no
                match confirm:
                    case "y":
                        # todoList.remove(todoList[taskNumber])  ## remove method takes in the task by indexing the task number in the to do list using square bracket notation
                        todoList.pop(taskNumber)  ## pop method takes in the index number in the to do list and removes the item, it also stores the removed item if assigned a variable.
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
            for index, task in enumerate(todoList):
                print(f"{index + 1}. {task}")
        case "exit":
            break

print("Good Bye")
