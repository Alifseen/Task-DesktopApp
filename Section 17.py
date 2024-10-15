"""Adding custom functionality to GUI Layout created previously
We will add "Add" functionality and Edit functionality and make the program show list in realtine as it changes
"""
import functions
import FreeSimpleGUI as gui

label = gui.Text("Type in a To-Do")

inputBox = gui.InputText(tooltip="Enter a Task", key="inputTask")  ## 4.2 We add a key to this box to be able to use its value using values variable from step 2

addButton = gui.Button("Add", key="addTask")  ## 4.1 We add a key to this button to be able to use its value using event variable from step 2

listBox = gui.Listbox(values=functions.get_todo_list(), key="taskList", enable_events=True, size=(43,15))  ## 8.1  We create a list view of all the items we have added in a text file at any given time

editButton = gui.Button("Edit", key="editTask")  ## 8.2 We add a key to this button to be able to use its value using event variable from step 2


windows = gui.Window("My To-Do App",
                     layout=[[label],
                             [inputBox, addButton],
                             [listBox, editButton]],
                     font=("Helvetica", 10))  ## 1. We add font type and size using a third argument

while True:  ## 3. We dont want the program to close when we press a button so we add a while loop to keep it from reading the windoes.close() line
    event, values = windows.read()
    todoList = functions.get_todo_list()
    print(event)
    print(values)

    ## 2. We assign contents of window to variable. Since windwos.read() returns a tuple of thing thats clicked and a dictionary values, we assign two variables
    match event:
        case "addTask":
            todo = values["inputTask"] + "\n"
            todoList.append(todo)
            functions.set_todo_list(todoList)
            todoList = functions.get_todo_list()
            windows["inputTask"].update(value="")
            windows["taskList"].update(values=todoList)
        case gui.WIN_CLOSED:
            break
        case "taskList":
            windows["inputTask"].update(value=values["taskList"][0])
        case "editTask":
            newTask = values["taskList"][0]
            taskNumber = todoList.index(newTask)
            todoList[taskNumber] = values["inputTask"]
            if "\n" in todoList[taskNumber]:
                functions.set_todo_list(todoList)
            else:
                todoList[taskNumber] = todoList[taskNumber] + "\n"
                functions.set_todo_list(todoList)
            todoList = functions.get_todo_list()
            windows["inputTask"].update(value="")
            windows["taskList"].update(values=todoList)



## 5. We create a match case statement
## 6. We add case such that if the event is add, that is, click happened on add button, we get the string inside the inputbox to the todolist.txt
## 7. we add case such that if window close (built in function) button is clicked, the loop breaks
## 9. we add a todolist case that updates its value into the inputbox  in realtime for easy updating


windows.close()


"""
For more structured layouts, you can use Column method to create column instances. 

# Prepare the widgets for the left column
left_column_content = [[sg.Text('Left 1')],
                       [sg.Text('Left 2')]]
 
# Prepare the widgets for the right column
right_column_content = [[sg.Text('Right 1')],
                        [sg.Text('Right 2')]]
 
 
# Construct the Column widgets
left_column = sg.Column(left_column_content)
right_column = sg.Column(right_column_content)
 
# Construct the layout
layout = [[left_column, right_column]]
 
# Construct and display the window
window = sg.Window('Columns', layout)
window.read()
window.close()

"""