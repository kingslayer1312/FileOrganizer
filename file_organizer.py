import os
import pathlib

class FileOrganizer:
    def printWelcomeMessage(self):
        print("Welcome to FileOrganizer!\n")
        print("FileOrganizer lets you organize all files of the same type into separate directories\n")
    def changeDirectory(self, path):
        try:
            os.chdir(path)
        except OSError:
            print("Sorry, the directory does not exist\n")
    def findFiles(self):
        files = [file for file in os.listdir(".") if os.path.isfile(file)]
        return files
    def findExtensions(self, files):
        extensions = []
        for i in files:
            if pathlib.Path(i).suffix not in extensions:
                extensions.append(pathlib.Path(i).suffix[1:])
        return set(extensions)
    def createFolders(self, extensions):
        for i in extensions:
            os.mkdir(i)
    def moveFiles(self, files, extensions):
        for i in files:
            if pathlib.Path(i).suffix[1:] in extensions:
                os.rename(i, "{}/{}".format(pathlib.Path(i).suffix[1:], i))
            else:
                os.mkdir(pathlib.Path(i).suffix[1:])

tool = FileOrganizer()

tool.printWelcomeMessage()
print("Enter file path: ")
path = input()
tool.changeDirectory(path)
files = tool.findFiles()
extensions = tool.findExtensions(files)
print(extensions)
tool.createFolders(extensions)
tool.moveFiles(files, extensions)

print("Operation completed.\n{} files have been organized into {} folders\n".format(len(files), len(os.listdir())))