"""enumerate() function
Improving To do list by adding numbers before the task
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
                print(todoList.index(task)+1, task)  ## We can use the index method and add 1 to get the task number
            taskNumber = (int(input("Enter the task number from the Task list you want to edit: "))) - 1
            print("Task selected: ", todoList[taskNumber])
            newTodo = input("Enter the new Todo Task: ")
            todoList[taskNumber] = newTodo.capitalize()
            print("list Updated!")
        case "show":
            for index, task in enumerate(todoList):  ## An alternate to using index method is to use the "enumerate()" function which allows processing key-value pairs, so index and value in list
                print(index+1, task)
        case "exit":
            break

print("Good Bye")

