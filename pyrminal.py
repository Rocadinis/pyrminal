# (C) Rodrigo Dinis, 2022
import os
user = os.getlogin()
curDir = os.getcwd()
os.system("cls")
print("pyrminal by Rocadinis - May 2022 build\n")
while True:
    command = input("$" + user + ": ")
    if command.startswith("echo "):
        print(command[5:])
    elif command == "cd":
        print(curDir)
    elif command.startswith("cd "):
        try:
            newDir = command[3:]
            os.chdir(newDir)
            curDir = os.getcwd()
        except:
            print("No such directory was found")
    elif command.startswith("mkdir "):
        try:
            os.mkdir(command[6:])
        except:
            print("The directory could not be created")
    elif command.startswith("rmdir "):
        try:
            os.rmdir(command[6:])
        except:
            print("No such directory was found")
    elif command.startswith("type "):
        try:
            f = open(command[5:], "r")
            content = f.readlines()
            for line in content: print(line, end=" ")
            print("") 
        except:
            print("A file with that name was not found")
    elif command == "cls":
        os.system("cls") #shameful
    elif command.startswith("title "):
        os.system("title " + command[6:]) #less shameful but still
    elif command == "dir":
        dirs = os.scandir(curDir)
        for thing in dirs:
            if thing.is_dir():
                print("Folder -", thing.name)
            if thing.is_file():
                print("File -", thing.name)
        print("\n")
    elif command == "tree":
        dirs = os.scandir(curDir)
        for folder in dirs:
            if folder.is_dir():
                print("Main Folder name -", folder.name)
                subDirs = os.scandir(folder)
                for subthing in subDirs: 
                    if subthing.is_dir(): print("Folder name -", subthing.name)
                    if subthing.is_file(): print("File name -", subthing.name)
                print("\n")
    else:
        print("command " + command + " was not found")