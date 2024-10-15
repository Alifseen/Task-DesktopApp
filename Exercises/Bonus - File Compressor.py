import FreeSimpleGUI as gui
import BonusFileCompressorFunction as su

compressLabel = gui.Text("Select Files to compress")
destinationLabel = gui.Text("Select Destination folder")
confirmationLabel = gui.Text("", key="confirmation", text_color="green")
inputBoxFile = gui.InputText(tooltip="Enter File Path")
inputBoxDestination = gui.InputText(tooltip="Enter Destination Path")
chooseButtonFile = gui.FilesBrowse("Choose", key="fileSelect")
""" File Browse is a special kind of built in button that allows selecting a file from explorer when pressed"""
chooseButtonDestination = gui.FolderBrowse("Choose", key="folderSelect")
""" Allows selecting a folder"""

compressButton = gui.Button("Compress", key="Process")

windows = gui.Window("File Zipper",
                     layout=[[compressLabel, inputBoxFile, chooseButtonFile],
                             [destinationLabel, inputBoxDestination, chooseButtonDestination],
                             [compressButton, confirmationLabel]])

while True:
    event, values = windows.read()

    match event:
        case "Process":
            destination = values["folderSelect"]
            file = values["fileSelect"].split(";")
            zipName = "ShUtilzippedfiles"
            su.create_zip(file, destination, zipName)
            windows["confirmation"].update(value="Compression successful".upper())
        case gui.WIN_CLOSED:
            break

windows.close()
