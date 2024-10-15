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
password = ""

while password != "pass123":
    password = input("Enter Password: ")
print("Correct Password")


## Using while loop a definite number of times
x = 1
while x <= 6:
    print(x)
    x += 1