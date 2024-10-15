## Index() method
alist = ["a", "b", "c", "d", "e"]
print(alist.index("a"))  # this will print the index position of "a" which is 0

""""""

## setitem method
alist = ["a", "b", "c", "d", "e"]
alist.__setitem__(0, "new a")  # this takes the key (which is index in case of list) as first argument and the new value as the second argument, to replace the existing value. In this case, it replaces "a" with "new a"
print(alist)

""""""

## String Mutability
## The string datatype has a method called "replace()" which takes two arguments, 1st is the character to be replaced, second is the replacement character.
filename = "1. This is a file.txt"
filename = filename.replace(".", "-", 1)  # create a new string with the dash instead of a dot and save it in the same variable to overwrite the old value. The 1 at the end makes sure that only the first occurrence of the dot is changed, not the subsequent ones.
print(filename)

## Alternatively if the string is in a list, use replace in a for loop
filenames = ["1. This is a file.txt", "2. This is another file.txt", "3. This is last file.txt"]
for name in filenames:
    name = name.replace(".", "-", 1)
    print(name)