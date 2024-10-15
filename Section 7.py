"""
Using + sign for multiple operations in a single list comprehension, in this case, removing and adding characters
"""

fileNames = ["1. doc", "1.report", "1.presentation"]
fileNames = [name.replace(".","-", 1) + ".txt" for name in fileNames]
print(fileNames)