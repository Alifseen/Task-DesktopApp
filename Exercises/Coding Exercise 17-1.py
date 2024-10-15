import FreeSimpleGUI as sg
from converter14 import convert

sg.theme("black")

feetLabel = sg.Text("Enter FEET:")
inchesLabel = sg.Text("Enter INCHES:")
feetBox = sg.InputText(key="feet")
inchesBox = sg.InputText(key="inch")
convertButton = sg.Button("Convert", key="action")
exitButton = sg.Button("Exit", key="exit")
answerLabel = sg.Text("", key='answer')

windows = sg.Window("Converter",
                    [[feetLabel,feetBox],
                     [inchesLabel,inchesBox],
                     [convertButton, exitButton, answerLabel]])

while True:
    event, values = windows.read()
    match event:
        case "action":
            try:
                feetValue = int(values["feet"])
                inchValue = int(values["inch"])
                meterValue = convert(feetValue, inchValue)
                windows["answer"].update(value=f"{meterValue} m")
            except ValueError:
                sg.popup("Please provide both values", font=("Helvetica", 10))
        case sg.WIN_CLOSED | "exit":
            exit()
