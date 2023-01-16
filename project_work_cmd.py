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
        if path != "C:/":
            list_path.remove(list_path[-2])
            list_path.remove(list_path[-1])
            for i in list_path:
                path += f"{i}/"
    elif command.startswith("cd"):
        a = command.split()
        if not a[1] in list_ls:
            print('No such directory')
        else:
            path += f"{a[1]}/"
    
