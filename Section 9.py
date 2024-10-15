"""
Dictionary is very useful when we need a value pair or for index to not be just a number. It is initiated by curly brackets {}
"""
normalList = [14,20,30]
dictionary = {"height":14, "width":20, "depth":30}  # this is more explicit and tells us what the value represents more clearly compared to a list
# lists are useful when the data in them represent same or similar things. Dictionary has an added advantage of labelling things so it can have a variety of values.
# To get a value from dictionary, we specify its key instead of index number
print(dictionary["width"])

# While a list automatically prints values only and not the index numbers, dictionaries prints both keys and values, so you have to explicit use value method or key method depending on what you want.
print(normalList, dictionary.values())