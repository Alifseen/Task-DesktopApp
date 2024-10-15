""" Added in section 15
Defining this constant makes it easier to change the file path if needed in the future
"""
FILEPATH = "files/todos.txt"



def get_todo_list(filepath=FILEPATH):
    """ Read the text file and return the content in a variable as a list"""
    with open(filepath) as file:
        todoTxtFile = file.readlines()
        return todoTxtFile


def set_todo_list(set_list, filepath=FILEPATH):
    """ Writes content as a list to a text file"""
    with open(filepath, "w") as file:
        file.writelines(set_list)

if __name__ == "__main__":
    print(get_todo_list())