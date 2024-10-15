import zipfile
import pathlib


def create_zip(filePaths, destinationDir, fileName):
    destinationPath = pathlib.Path(destinationDir, fileName+".zip")
    with zipfile.ZipFile(destinationPath, "w") as zipFile:
        for path in filePaths:
            path = pathlib.Path(path)
            zipFile.write(path, arcname=path.name)


if __name__ == "__main__":
    create_zip(["Bugfix15-main.py", "Bugfix15parsers.py"], "../files/ShutilFiles", "newZips")