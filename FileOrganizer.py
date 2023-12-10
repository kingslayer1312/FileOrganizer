import os

class FileOrganizer:
    def printWelcomeMessage():
        print("Welcome to FileOrganizer!\n")
        print("FileOrganizer lets you organize all files of the same type into folders\n")
    def changeDirectory(path):
        try:
            os.chdir(path)
        except OSError:
            print("Sorry, the directory does not exist\n")
    