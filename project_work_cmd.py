import os
import sys


path = "/" #macOS does not have C drive
while True:
    command = input(f"{path}" + '>')
    list_ls = os.listdir(path)
    if command == "ls":
        for i in list_ls:
            print(i)
    elif command == "cd ..":
        list_path = path.split("/")
        path = ""
        if path != "/":
            list_path.remove(list_path[-2])
            list_path.remove(list_path[-1])
            for i in list_path:
                path += f"{i}/"
    elif command.startswith("cd"):
        xxx = command.split()
        if not xxx[1] in list_ls:
            print('No such directory')
        else:
            path += f"{xxx[1]}/"

    # Creating a 'folder' by mkdir and 'file' by mkfile

    elif command.startswith("mkdir"):
        xxx = command.split()
        os.mkdir(path + xxx[1])

    elif command.startswith("mkfile"):
        xxx = command.split()
        f = open(path + xxx[1], "x")


    # Renaming a directory or file

    elif command.startswith("rename"):
        xxx = command.split()
        os.rename(path + xxx[1], path + xxx[2])


    # Removing a directory or file

    elif command.startswith("remove"):
        xxx = command.split()
        try:
            os.rmdir(path+xxx[1])
        except:
            os.remove(path+xxx[1])

    elif command.startswith("open"):
        xxx = command.split()
        f = open(path+xxx[1])
        for line in f:
            print(line)
        f.close()

    elif command == "quit":
        sys.exit(0)
