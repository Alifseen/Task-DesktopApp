""" Using Match Case Statements
To perform different tasks based on what the user types in we can use "Match Case" Statements to break the loop, add a task or see the task list
"""
#
# userPrompt = "Enter a To Do Item: "
# userPromptSelection = "Type add or show or exit: "
#
# todoList = []
#
# while True:  ## This loop will continue to run infinitely unless we add something to the code inside it to terminate it.
#     userAction = input(userPromptSelection).lower().strip  ## Takes in the user action input then converts into lowercase as well as removes any whitespace to check against the match case conditions later
#
#     match userAction:  ## Checks the variable for one of the values defined in case statements
#         case "add":  ## if the match value is same as the case value, the code is executed, otherwise it is skipped.
#             todo = input(userPrompt)
#             todo = todo.capitalize()
#             todoList.append(todo)
#         case "show":
#             print(todoList)
#         case "exit":
#             break  ## Breaks the loop.
#
# print("Good Bye")

""""""

## The output of the code that prints a list is not very user friendly, specially if the list is long and has many elements.
## For loop can be used to iterate over a list and print one item at a time

userPrompt = "Enter a To Do Item: "
userPromptSelection = "Type add or show or exit: "

todoList = []

while True:
    userAction = input(userPromptSelection).lower().strip()

    match userAction:
        case "add":
            todo = input(userPrompt)
            todo = todo.capitalize()
            todoList.append(todo)
        case "show" | "display":  ## an example of how to use or operator to look for and match multiple values in a single case statement
            for task in todoList:  ## starts from the 0 index position inside the list and iterates over it to execute the code inside the loop until the list is exhausted
                print(task)
        case "exit":
            break  ## Breaks the loop.
        case _:  ## You can declare any anonymous variable in a case statement to serve as a fallback if any other case statement is not matched. It is convertion to declare this anonymous variable with an underscore.
            print("Invalid Command")

print("Good Bye")
