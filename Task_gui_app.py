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

