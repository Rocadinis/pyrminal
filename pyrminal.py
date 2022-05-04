# (C) Rodrigo Dinis
import os
user = os.getlogin()
curDir = os.getcwd()
os.system("cls")
while True:
    command = input("$" + user + ": ")
    if command.startswith("echo "):
        print(command[5:])
    elif command == "cd":
        print(curDir)
    elif command.startswith("cd "):
        newDir = command[3:]
        os.chdir(newDir)
        curDir = os.getcwd()
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
    else:
        print("command " + command + " was not found")