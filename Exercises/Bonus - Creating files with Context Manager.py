fileName = input("Enter Today's Date: ") + " (Bonus exercise)"
mood = input("how would you rate your mood today from 1 to 10: ")
content = input("Let your thoughts flow: ")


with open(f"../files/{fileName}.txt", "w") as file:
    file.writelines(content + 2*"\n")
    file.writelines(mood)
