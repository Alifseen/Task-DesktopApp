"""
zip function to add list items in different files, this compbines the both lists items in to a tuple with first list item being from the first list, and second from the second list\
"""

contents = ["this goes in list A",
            "this goes in list B",
            "this goes in list C"]

fileNames = ["lista.txt",
             "listb.txt",
             "listc.txt"]

for content, fileName in zip(contents, fileNames):
    file = open(f"files/{fileName}", "w")
    file.writelines(content)
    file.close()
