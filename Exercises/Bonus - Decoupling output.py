feet_inches = input("Enter feet and inches: ")


def convert(measurement):
    ft_inch_list = measurement.split(" ")
    feet = float(ft_inch_list[0])
    inches = float(ft_inch_list[1])
    inches_to_meter = ((feet * 12)+inches) / 39.37
    # return f"meters: {inches_to_meter}, inches: {inches}, feet: {feet}"
    return inches_to_meter


print((convert(feet_inches)))

"""
The Code above (commented out) is only good enough to print the conversions, it can not be used in another expression, for example to check height using if else statement because it is too many things
The concept of decoupling states that a function should only return 1 value and we should be able to use operations on that returned value
"""

result = convert(feet_inches)

if result < 1:
    print("Small")
else:
    print("Good")