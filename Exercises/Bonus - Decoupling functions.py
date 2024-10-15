"""
A function should do one thing and do it well, the function below is doing too much, decoupling function involves creating more functions to ensure that each function performs one action only.
The code below has been modified from the "bonus - decoupling output" to allow us to use the feet, inches and meters values freely, however we want.
"""

feet_inches = input("Enter feet and inches: ")


def parse(measurement):  # We seperate the action of splitting and storing the values from string in to this fucntion
    ft_inch_list = measurement.split(" ")
    feet = float(ft_inch_list[0])
    inches = float(ft_inch_list[1])
    return feet, inches  # we can return multiple values, these are stored in a tuple, but can be changed to dictionaries and list by adjusting the syntax.


def convert(feet, inches):
    inches_to_meter = ((feet * 12)+inches) / 39.37
    # return f"meters: {inches_to_meter}, inches: {inches}, feet: {feet}"
    return inches_to_meter


result = convert(parse(feet_inches)[0], parse(feet_inches)[1])  # we input the first value from the parse function's return tuple as feet, and second as inches.

if result < 1:
    print("Small")
else:
    print("Good")

print(f"meters: {result}, feet: {parse(feet_inches)[0]}, inches {parse(feet_inches)[1]}")  # Now we can access all the values and operate on them however we want. this is decoupling.