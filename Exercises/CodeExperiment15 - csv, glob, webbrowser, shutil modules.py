# """Glob Module
# It is about pathname patterns.
# One of its functions is to filter through multiple files and get the ones you want to iterate on
# """
# import glob
#
# myFiles = glob.glob("../files/*.txt")
# """ this looks for all txt files using regex '*' in the file directory and returns a list with their path names"""
#
# """Now we can operate on these files, in the example belwo, we will simply open,read and close them"""
# for filePath in myFiles:
#     with open(filePath) as file:
#         content = file.read()
#     print(
#         f"""
# {filePath}:
# {content}""")



# """CSV Module
# allows processing csv file (comma separated file with columns and rows)
# """
# import csv
#
# with open("../files/weather.csv") as file:
#     data = list(csv.reader(file))
#     """ reader is an iterator datatype is able to iterate over the datastructure of a csv file, but it is not readable by itself so it needs to be converted to a list"""
#
# print(data)
# """this prints each row as a list"""
#
# """ We can use csv for a lot of things, for example, if our weather csv had thousands of temperature values they can be used to check that cities temperature"""
# userPrompt = input("Enter City Name: ")
#
# for row in data:
#     if row[0] == userPrompt:
#         print(row[1])
#     else:
#         continue



# """Shutil Module
# Shutil stands for shell utilities
# with this module you can perform shell actions, such as copy, paste, zip etc
# Lets create a zip file using shutil
# """
# import shutil
#
# shutil.make_archive("shutil-output", "zip", "../files/ShutilFiles")



# """webbrowser module
# this module allows us to operate broswer through code.
# in the example below we will perform a simple search on duckduckgo
# """
# import webbrowser
#
# searchTerm = input("Enter Search Term Here: ").replace(" ","+")
# """since urls do not accept white space, the replace method can be used to replace whitespace with + sign """
#
# webbrowser.open(f"https://duckduckgo.com/?t=h_&q={searchTerm}")
