""" Using Match Case Statements
To perform different tasks based on what the user types in we can use "Match Case" Statements to break the loop, add a task or see the task list
"""

userPrompt = "Enter a To Do Item: "
userPromptSelection = "Type add or show or exit: "

todoList = []

while True:  ## This loop will continue to run infinitely unless we add something to the code inside it to terminate it.
    userAction = input(userPromptSelection).lower().strip  ## Takes in the user action input then converts into lowercase as well as removes any whitespace to check against the match case conditions later

    match userAction:  ## Checks the variable for one of the values defined in case statements
        case "add":  ## if the match value is same as the case value, the code is executed, otherwise it is skipped.
            todo = input(userPrompt)
            todo = todo.capitalize()
            todoList.append(todo)
        case "show":
            print(todoList)
        case "exit":
            break  ## Breaks the loop.

print("Good Bye")
