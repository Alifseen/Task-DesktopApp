file = open(r"D:\Downloads\members.txt", "r")
memberFile = file.readlines()
file.close()

newMemberPrompt = input("Add a new member: ")
memberFile.append(newMemberPrompt)

file = open(r"../files/members.txt", "w")
file.writelines(memberFile)
file.close()