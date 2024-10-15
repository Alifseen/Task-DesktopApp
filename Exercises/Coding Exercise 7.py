fileNames = ["a.txt", "b.txt", "c.txt"]
for fileName in fileNames:
    file = open(rf"../files/{fileName}", "r")
    files = file.read()
    file.close()
    print(files)