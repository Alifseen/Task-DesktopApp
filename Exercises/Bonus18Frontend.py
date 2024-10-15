import FreeSimpleGUI as sg
from Bonus18Zipextractor import extract_zip

sg.theme("black")

label1 = sg.Text("Select archive: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select destination: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

label3 = sg.Text(key="output", text_color="white")
output_button = sg.Button("Extract", key="extract")

window = sg.Window("Archive Extractor",
                   layout=[[label1,input1, choose_button1],
                           [label2, input2, choose_button2],
                           [output_button,label3]])

while True:
    event, values = window.read(timeout=200)
    match event:
        case "extract":
            file = values["archive"]
            destination = values["folder"]
            extract_zip(file, destination)
            window["output"].update(value="Extraction Complete")
        case sg.WIN_CLOSED:
            break

window.close()
