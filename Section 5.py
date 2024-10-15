"""enumerate() function
enumerate returns the index as well as the value in a list.
enumerate object are not displayable by themselves but they can be printed after converting into a list of tuples
"""

a = enumerate(["a", "b", "c"])
print(a)  # prints the object location in memory
print(list(a))  # prints index and items as a tuple inside a list

""""""

## Whenever a for loop ends the last iteration of the loop is still stored in the variables

alist = ["abc", "def", "ghi"]
for index, item in enumerate(alist):
    print(index, item)

print(f"final values of the loop: INDEX:{index}, VALUE:{item}")  # once the loop ends, we can still access the index and item variable with the values in the last iteration
