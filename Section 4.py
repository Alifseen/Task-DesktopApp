"""List Mutability
Lists are mutable, which means they can be changed, where as strings are immutable, meaning they can not be changed. Even though string index can be accessed to get the character at that index position, they can not be assigned a new value.
"""

## List Index
## Lists can be indexed using the square bracket notation with index number
## User needs to be able to edit the task item they have in the to do list. To edit the to do item, they need to be select it using list indexing.
## Remember the index starts from 0, not 1.

userPrompt = "Enter a To Do Item: "
userPromptSelection = "Type add or edit or show or exit: "  # Added another prompt of "edit" for the user to type

todoList = []

while True:
    userAction = input(userPromptSelection).lower().strip()

    match userAction:
        case "add":
            todo = input(userPrompt)
            todo = todo.capitalize()
            todoList.append(todo)
        case "edit":  ## Added another case statements that checks for the new prompt option
            for task in todoList:
                print(task)
            taskNumber = int(input("Enter the task number from the Task list you want to edit: ")) - 1  ## We need to ask the user which task from the list they want to edit. We can do that by getting them to type the exact task string OR we can get them to simply type the number of where that task is located which is more convenient. Since the list indexing needs a number and the input function returns a string, we convert the string into a number using the "int()" function. Since the user thinks the list starts from 1, whereas it actually starts from 0, we -1 from whatever the user enters to get the correct index number, that value is stored here.
            print("Task selected: ", todoList[taskNumber])
            newTodo = input("Enter the new Todo Task: ")
            todoList[taskNumber] = newTodo.capitalize()
            print("list Updated!")

        case "show":
            for task in todoList:
                print(task)
        case "exit":
            break

print("Good Bye")
