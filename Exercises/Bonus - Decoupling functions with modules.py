"""
We can move the functions to a different file and import it as a module automatically using the pycharms refactor feature and selecting move.
"""
from Exercises.converter14 import convert  # These are added automatically by pycharm
from Exercises.parser14 import parse  # Notice that they include the directory path name with dot notation when calling the file, this is not required if the file is in same directory as the file that is calling.

feet_inches = input("Enter feet and inches: ")

result = convert(parse(feet_inches)[0], parse(feet_inches)[1])

if result < 1:
    print("Small")
else:
    print("Good")

print(f"meters: {result}, feet: {parse(feet_inches)[0]}, inches {parse(feet_inches)[1]}")
