"""Manual Way of repeating a task
To do list code:
In this section the user input code is repeated 3 times to take in the users To Do list item.
This is bad practice because it:
    hard codes the number of to do list items a user can enter
    repeats the same line of code
"""
# userPrompt = "Enter a To Do Item: "  ## The message that user sees when prompted for input
#
# todo1 = input(userPrompt)  ## To Do list item 1
# todo2 = input(userPrompt)  ## To Do list item 2
# todo3 = input(userPrompt)  ## To Do list item 3
#
# todoList = [todo1, todo2, todo3]  ## Manually add To Do items to a list variable
#
# print(todoList)  ## Show the list ones done

""""""

## Instead, we can use a while loop for repeating Tasks
## initiated by the "while" keyword, this loops takes a condition and continues running the code inside it as long as the condition is true.
## The condition can be defined through a statement such as "while 2 > 1:" or it can simply use a boolean datatype, such as "while True:"


## An example is using the while loop to check password, if it is the same, stop the loop, if not continue
# password = ""
#
# while password != "pass123":
#     password = input("Enter Password: ")
# print("Correct Password")
#
#
# ## Using while loop a definite number of times
# x = 1
# while x <= 6:
#     print(x)
#     x += 1

""""""

## To do list code

## Using 'python Methods' we can do all kinds of things. Methods are functions associated with objects / datatype. Methods can be accessed through the "Dot Notation"
userPrompt = "Enter a To Do Item: "  # The message that user sees when prompted for input

todoList = []  # Declared an empty list that be used later

while True:  # This loop will continue to run infinitely unless we add something to the code inside it to terminate it.
    # anything after the colon is indented so that it runs inside the loop
    todo = input(userPrompt)  # User input stored in a variable
    todo = todo.capitalize()  # Using the capitalize method for the string datatype inside the variable, the value is capitalized and stored back in the variable, replacing the old non capitalized value.
    todoList.append(todo)  # Using the append method for the list datatype inside the variable, value of the variable given as an argument is added to the bottom of the list
    print(todoList)
