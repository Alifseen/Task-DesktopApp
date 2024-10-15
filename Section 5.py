"""f-strings
Using 'f-strings' to improve the code output to have complete control over what the program prints.
initiated by 'f' before the quotations "" and has variables inside curly brackets {}
"""

userPrompt = "Enter a To Do Item: "
userPromptSelection = "Type add or edit or show or exit: "

todoList = []

while True:
    userAction = input(userPromptSelection).lower().strip()

    match userAction:
        case "add":
            todo = input(userPrompt)
            todo = todo.capitalize()
            todoList.append(todo)
        case "edit":
            for task in todoList:
                print(f"{todoList.index(task) + 1}. {task}")  ## We use f-string here
            taskNumber = int(input("Enter the task number from the Task list you want to edit: ")) - 1
            print("Task selected: ", todoList[taskNumber])
            newTodo = input("Enter the new Todo Task: ")
            todoList[taskNumber] = newTodo.capitalize()
            print("list Updated!")
        case "show":
            for index, task in enumerate(todoList):
                print(f"{index + 1}. {task}")  ## We use f-string here
        case "exit":
            break

print("Good Bye")
