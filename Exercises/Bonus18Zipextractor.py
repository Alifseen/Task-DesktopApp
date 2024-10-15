import zipfile

def extract_zip(filePath, destinationDir):
    with zipfile.ZipFile(filePath, "r") as zipFile:
        zipFile.extractall(destinationDir)


if __name__ == "__main__":
    print("main")