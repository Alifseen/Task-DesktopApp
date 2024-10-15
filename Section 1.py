"""
Variables and Functions
"""
## Variable are boxes where you can store data types
thisContainsString = "Hello World"
thisContainsList = ["thing 1", "thing 2", "thing 3", "and so on...", thisContainsString]


## Functions are operations you can perform through code
print("Hello World")  ## this prints out whatever argument is inside it.
print("Hello World", thisContainsList)  ## there can be multiple arguments inside a function, Number of arguments depends on the function.

userInput = input("Type Here: ")  ## Input function allows taking in user input, but it must be stored in a variable to be used

print(type(thisContainsList))  ## Type function describes the datatype of a variable. This needs to be used with print to show 'list'
print(type(thisContainsString))  ## This shows "str" for string

print(len(thisContainsString))  ## strings are a list of characters and to find the out the length of any list, we use the len function. This shows number of characters
print(len(thisContainsList))  ## This shows number of things
