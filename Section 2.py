"""Manual Way of repeating a task
To do list code:
In this section the user input code is repeated 3 times to take in the users To Do list item.
This is bad practice because it:
    hard codes the number of to do list items a user can enter
    repeats the same line of code
"""
userPrompt = "Enter a To Do Item: "  ## The message that user sees when prompted for input

todo1 = input(userPrompt)  ## To Do list item 1
todo2 = input(userPrompt)  ## To Do list item 2
todo3 = input(userPrompt)  ## To Do list item 3

todoList = [todo1, todo2, todo3]  ## Manually add To Do items to a list variable

print(todoList)  ## Show the list ones done
