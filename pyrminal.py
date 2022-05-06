# (C) Rodrigo Dinis, 2022
import os, shutil
from sys import exit
user = os.getlogin()
curDir = os.getcwd()
os.system("cls")
print("pyrminal by Rocadinis - May 2022 build\n")
while True:
    command = input("$" + user + ": ")
    if command.lower().startswith("echo "):
        print(command[5:])
    elif command == "cd":
        print(curDir)
    elif command.lower().startswith("cd "):
        try:
            newDir = command[3:]
            os.chdir(newDir)
            curDir = os.getcwd()
        except:
            print("No such directory was found")
    elif command.lower().startswith("mkdir "):
        try:
            os.mkdir(command[6:])
        except:
            print("The directory could not be created")
    elif command.lower().startswith("rmdir "):
        try:
            os.rmdir(command[6:])
        except:
            print("No such directory was found")
    elif command.lower().startswith("type "):
        try:
            f = open(command[5:], "r")
            content = f.readlines()
            for line in content: print(line, end=" ")
            print("") 
        except:
            print("A file with that name was not found")
    elif command.lower() == "cls":
        os.system("cls") #shameful
    elif command.lower().startswith("title "):
        os.system("title " + command[6:]) #less shameful but still
    elif command.lower() == "dir":
        dirs = os.scandir(curDir)
        for thing in dirs:
            if thing.is_dir():
                print("Folder -", thing.name)
            if thing.is_file():
                print("File -", thing.name)
        print("\n")
    elif command.lower() == "tree":
        dirs = os.scandir(curDir)
        for folder in dirs:
            if folder.is_dir():
                print("Main Folder name -", folder.name)
                subDirs = os.scandir(folder)
                for subthing in subDirs: 
                    if subthing.is_dir(): print("Folder name -", subthing.name)
                    if subthing.is_file(): print("File name -", subthing.name)
                print("\n")
    elif command.lower() == "exit": exit(0)
    elif command.lower() == "ver": print("pyrminal by Rocadinis - May 2022 build")
    elif command.lower() == "rename":
        try:
            toRename = input("To rename? ")
            newName = input("New name? ")
            os.rename(toRename, newName)
        except:
            print("The file was either not found or it already exists")
    elif command.lower() == "move":
        try:
            toMove = input("Move which file? ")
            targetDir = input("To which directory? ")
            shutil.move(toMove, targetDir)
        except:
            print("Either the file or directory was not found")
    elif command.lower() == "copy":
        try:
            toCopy = input("Copy which file? ")
            targetDir = input("To which directory? ")
            shutil.copy(toCopy, targetDir)
        except:
            print("Either the file or directory was not found")
    elif command.lower() == "space":
        print("Total space on current directory: " + str(shutil.disk_usage(curDir)[0]) + " bytes")
        print("Used space on current directory: " + str(shutil.disk_usage(curDir)[1]) + " bytes")
        print("Free space on current directory: " + str(shutil.disk_usage(curDir)[2]) + " bytes")
    else:
        print("command " + command + " was not found")