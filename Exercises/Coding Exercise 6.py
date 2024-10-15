filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f"../files/{filename}", "w")
    file.writelines("Hello")
    file.close()