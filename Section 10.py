"""
More subtle logical errors need to be fixed manually and we can use the "exit" function to account for them, for example in a program that calculates area of a rectangle, we need to manually account for a square
"""
try:
    width = float(input("Enter rectangle width: "))
    height = float(input("Enter rectangle height: "))
    if width == height:  # Since only a square has the same width and height
        exit("this is not a rectangle, its a square")  # we exit with our own statement
    area = width *height
    print(area)
except ValueError:
    print("please enter a number.")
