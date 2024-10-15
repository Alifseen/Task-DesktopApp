fileNames = ["1. doc", "1.report", "1.presentation"]
fileNames = [name.replace(".","-", 1) + ".txt" for name in fileNames]
print(fileNames)
