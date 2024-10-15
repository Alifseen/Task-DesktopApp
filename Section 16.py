"""Building GUI (graphical User Interface) and Third Party Modules/library
To create a desktop graphical interface we will user free simple gui library which can be imported using the pip install command or through pycharm preference/settings
"""
import functions
import FreeSimpleGUI as gui  ## We import the library

label = gui.Text("Type in a To-Do")
inputBox = gui.InputText(tooltip="Enter a Task")
addButton = gui.Button("Add")

windows = gui.Window("My To-Do App", layout=[[label], [inputBox, addButton]])  ## We can get details on the pypi.org that this library can create a window using Windows function that takes in string as the title of program and layout as elements to be displayed. Each list is a row and if we want things on the same line, they should be in the same list, like the text box and add button in this case.

windows.read()  ## this opens the GUI program

windows.close()  ## this closes the GUI program if anything is pressed
