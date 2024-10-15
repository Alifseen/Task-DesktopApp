"""Finishing up
1. Add exit and complete command
2. Add error handling
3. Add time
4. Change theme
5. Check if the text file exists using os module, if it does not, then create it.
Note: I changed the filepath of txt file so that it is not in a folder
"""
import functions
import FreeSimpleGUI as gui
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

gui.theme("dark")

clock = gui.Text("", key="clock")

label = gui.Text("Type in a To-Do")

confirmationlabel = gui.Text("", key="message", text_color="white")

inputBox = gui.InputText(tooltip="Enter a Task", key="inputTask")

# addButton = gui.Button("Add", key="addTask")
# completeButton = gui.Button("Mark Complete", key="markDone")

""" We made the add and complete button into an icon buttons using the code below """
addButton = gui.Button(size=2, image_source="add.png",mouseover_colors="LightBlue2", tooltip="Add a Task", key="addTask")
completeButton = gui.Button(size=2, image_source="complete.png",mouseover_colors="LightBlue2", tooltip="Mark as Done!", key="markDone")

listBox = gui.Listbox(values=functions.get_todo_list("todos.txt"), key="taskList", enable_events=True, size=(43, 15))

editButton = gui.Button("Edit", key="editTask")


exitButton = gui.Button("Exit", key="exit")

windows = gui.Window("My To-Do App",
                     layout=[[clock],
                             [label],
                             [inputBox, addButton],
                             [listBox, editButton, completeButton],
                             [exitButton, confirmationlabel]],
                     font=("Helvetica", 10))

while True:
    event, values = windows.read(timeout=200)
    if event == gui.WIN_CLOSED or windows.was_closed():
        break
    else:
        todoList = functions.get_todo_list("todos.txt")
        windows["clock"].update(value=time.strftime("%H:%M:%S - %b,%d,%Y"))
        print(event)
        print(values)

        match event:
            case "addTask":
                todo = values["inputTask"] + "\n"
                todoList.append(todo)
                functions.set_todo_list(todoList, filepath="todos.txt")
                todoList = functions.get_todo_list("todos.txt")
                windows["inputTask"].update(value="")
                windows["taskList"].update(values=todoList)
                windows["message"].update(value="Task Added Successfully!")
            case gui.WIN_CLOSED | "exit":
                break
            case "taskList":
                try:
                    windows["inputTask"].update(value=values["taskList"][0])
                except:
                    gui.popup("Task List is Empty", font=("Helvetica", 10))
            case "editTask":
                try:
                    newTask = values["taskList"][0]
                    taskNumber = todoList.index(newTask)
                    todoList[taskNumber] = values["inputTask"]
                    if "\n" in todoList[taskNumber]:
                        functions.set_todo_list(todoList, filepath="todos.txt")
                    else:
                        todoList[taskNumber] = todoList[taskNumber] + "\n"
                        functions.set_todo_list(todoList, filepath="todos.txt")
                    todoList = functions.get_todo_list("todos.txt")
                    windows["inputTask"].update(value="")
                    windows["taskList"].update(values=todoList)
                    windows["message"].update(value="Task Edited Successfully!")
                except IndexError:
                    gui.popup("No Task Selected!", font=("Helvetica", 10))
            case "markDone":
                try:
                    selectTask = values["taskList"][0]
                    taskNumber = todoList.index(selectTask)
                    todoList.pop(taskNumber)
                    functions.set_todo_list(todoList, filepath="todos.txt")
                    todoList = functions.get_todo_list("todos.txt")
                    windows["inputTask"].update(value="")
                    windows["taskList"].update(values=todoList)
                    windows["message"].update(value="Task Marked Done!")
                except IndexError:
                    gui.popup("No Task Selected!", font=("Helvetica", 10))

windows.close()


"""
Another example of using Column to align the window
import FreeSimpleGUI as sg
# from zip_extractor import extract_archive
 
sg.theme("Black")
 
label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")
 
label2 = sg.Text("Select destination directory:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")
 
extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")
 
col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[choose_button1], [choose_button2]])
 
window = sg.Window("Archive Extractor",
                   layout=[[col1, col2, col3], [extract_button]])
while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction Completed!")
 
window.close()
"""