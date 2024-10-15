def get_todo_list(filepath="files/todos.txt"):
    """ Read the text file and return the content in a variable as a list"""
    with open(filepath) as file:
        todoTxtFile = file.readlines()
        return todoTxtFile


def set_todo_list(set_list, filepath="files/todos.txt"):
    """ Writes content as a list to a text file"""
    with open(filepath, "w") as file:
        file.writelines(set_list)

if __name__ == "__main__":
    """__name__ is a hidden variable defined by python that stores __main__ is the program is calling itself, otherwise it changes to the name of the python file."""
    print(get_todo_list())