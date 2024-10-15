""" JSON
Text file is one dimensional, that is it only contains test, CSV is two dimensional, that is, it contains rows and columns as lists of lists, but a JSON Is a dynamic data type, that means it contains a list/dictionaries of dictionaries and each dictionary can have different datatypes represented by keys. A JSON is nested dictioanries
While lists can have data of similar nature, dictionaries can have data of different nature due to it having keys. So in JSON we have a list/dictionary of dictionaries to represent different data types, and we can add another dictionary on the fly.
A JSON file has a .json extension and requires json module to read properly
json load reads JSON as list of dictionaries instead of a str as a normal open function would

In the example below, we are making a quiz that asks two questions, each question has multiple options, the correct answer is defined already and if user answers correctly they score 1 point. The quiz requires a dynamic datatype because we need a list that can store multiple questions, each with a question string, a list of options, the correct answer as int and the user's response as a string. So we will make a list containing questions as disctionaries, and these question disctionaries containing more dictionaries for each datatype described previously.
"""
import json

with open("Bonus15-Questions.json") as file:
    """ The file above is a list of nested dictionaries we described in docstring above"""
    content = file.read()

data = json.loads(content)
"""json.loads method converts the string captured in content variable into a list"""

score = 0
answerValidation = []


for mainQuestion in data:
    print(mainQuestion["questionText"])
    for index, options in enumerate(mainQuestion["answerOptions"]):
        print(index + 1, ". ", options)
    userAnswer = int(input("Select the Correct Option Number: "))
    mainQuestion["userResponse"] = userAnswer
    if mainQuestion["correctAnswer"] == mainQuestion["userResponse"]:
        score += 1
        answerValidation.append("Correct Answer")
    else:
        answerValidation.append("Incorrect Answer")
        continue

for index, answer in enumerate(answerValidation):
    print(index+1,". ",answer)

print(f"Score: {score}/{len(data)}")