from pathlib import Path
import shutil


def createfolder():
    try:
        name = input("please tell your folder name ")
        if name == "":
            name == "New Folder"
        path = Path(name)
        path.mkdir()
        print(f" Folder name {name} created successfully ")
    except Exception as err:
        print(f"Error : folder {name} already exist ")


def readfileandfolder():
    path = Path("")  # if we want to an special folder name access then ./foldername
    items = list(path.rglob("*"))
    for i, v in enumerate(items):  # index or values k basis per divide kerna
        print(f"{i + 1} : {v}")


def updatefolder():
    try:
        readfileandfolder()
        name = input("Which folder you want to update : ")
        path = Path(name)
        if path.exists() and path.is_dir():  # exists function batata h ki kuch chej exist kerti h ya nahi
            newname = input("Please tell your new name : ")
            new_path = Path(newname)
            path.rename(new_path)
            print("Done successfully ")
        else:
            print("No such Folder Exists ")
    except Exception as err:
        print(f"Sorry error occured : {err}")


def deletefolder():
    try:
        name = input("Please tell your folder name ")
        path = Path(name)
        if path.exists() and path.is_dir():
            shutil.rmtree(path)
        else:
            print("Sorry no path exists")
    except Exception as err:
        print(f"sorry error occured : {err}")


def createfile():
    try:
        name = input("Please tell your file name ")
        path = Path(name)
        if not path.exists():
            with open(name, 'w') as fs:
                data = input("What do you want to write in your file ")
                fs.write(data)
            print(f"File {name} creted successfully")
        else:
            print("sorry this file name already exists")
    except Exception as err:
        print(f"sorry error occured as: {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("tell which file you want to read")
        path = Path(name)
        if path.exists():
            with open(name, 'r') as fs:
                data = fs.read()
                print(data)
        else:
            print("Sorry the file was not exists")
    except Exception as err:
        print(f"sorry error occured {err}")


def updatefile():
    try:
        name = input("please tell your file name ")
        path = Path(name)
        if path.exists():
            print("press 1 for changing the name ")
            print("press 2 for appending new content")
            print("press 3 for deleting all the content")
            choice = input("what you wanna do")
            if choice == "1":
                new_name = input("Enter your new file name: ")
                new_path = Path(new_name)
                if not new_path.exists():
                    path.rename(new_path)
                    print("name chnage succesfully")
                else:
                    print("sorry this name already exists ")
            elif choice == "2":
                with open(name, "a") as fs:
                    data = input("What do you want to append ")
                    fs.write(" " + data)
                print("content appended successfully ")
            elif choice == "3":
                with open(name, "w") as fs:
                    data = input("press enter to skip or write new data ")
                    fs.write(data)
                print("done successfull")
    except Exception as err:
        print(f" Error Occured i.e : {err}")


def deletefile():
    try:
        name = input("Please tell me which file you want to delet ")
        path = Path(name)
        if path.exists() and path.is_file():
            path.unlink()  # or # os.remove(path)
        else:
            print("sorry this file does not exist ")
    except Exception as err:
        print(err)


while True:
    print("press 1 for creating a folder ")
    print("press 2 for reading files and folder ")
    print("press 3 for updating the folder ")
    print("press 4 for deleting a folder ")
    print("press 5 for create file ")
    print("press 6 for reading a file")
    print("press 7 for updating the file ")
    print("press 8 for deleting the file ")
    check = int(input("What do you want : "))
    if check == 1:
        createfolder()
        a = input("Do you want to continue then press yes otherwise no")
        if a in ["yes", "Yes"]:
            print("press 1 for creating a folder ")
            print("press 2 for reading files and folder ")
            print("press 3 for updating the folder ")
            print("press 4 for deleting a folder ")
            print("press 5 for create file ")
            print("press 6 for reading a file")
            print("press 7 for updating the file ")
            print("press 8 for deleting the file ")
            check = int(input("What do you want : "))
            if check==1:
                createfolder()
            elif check == 2:
                readfileandfolder()
            elif check == 3:
                updatefolder()
            elif check == 4:
                deletefolder()
            elif check == 5:
                createfile()
            elif check == 6:
                readfile()
            elif check == 7:
                updatefile()
            elif check == 8:
                deletefile()
        else:
            break
    elif check == 2:
        readfileandfolder()
        a = input("Do you want to continue then press yes otherwise no")
        if a in ["yes", "Yes"]:
            print("press 1 for creating a folder ")
            print("press 2 for reading files and folder ")
            print("press 3 for updating the folder ")
            print("press 4 for deleting a folder ")
            print("press 5 for create file ")
            print("press 6 for reading a file")
            print("press 7 for updating the file ")
            print("press 8 for deleting the file ")
            check = int(input("What do you want : "))
            if check == 1:
                createfolder()
            elif check == 2:
                readfileandfolder()
            elif check == 3:
                updatefolder()
            elif check == 4:
                deletefolder()
            elif check == 5:
                createfile()
            elif check == 6:
                readfile()
            elif check == 7:
                updatefile()
            elif check == 8:
                deletefile()
        else:
            break
    elif check == 3:
        updatefolder()
        a = input("Do you want to continue then press yes otherwise no")
        if a in ["yes", "Yes"]:
            print("press 1 for creating a folder ")
            print("press 2 for reading files and folder ")
            print("press 3 for updating the folder ")
            print("press 4 for deleting a folder ")
            print("press 5 for create file ")
            print("press 6 for reading a file")
            print("press 7 for updating the file ")
            print("press 8 for deleting the file ")
            check = int(input("What do you want : "))
            if check == 1:
                createfolder()
            elif check == 2:
                readfileandfolder()
            elif check == 3:
                updatefolder()
            elif check == 4:
                deletefolder()
            elif check == 5:
                createfile()
            elif check == 6:
                readfile()
            elif check == 7:
                updatefile()
            elif check == 8:
                deletefile()
        else:
            break
    elif check == 4:
        deletefolder()
        a = input("Do you want to continue then press yes otherwise no")
        if a in ["yes", "Yes"]:
            print("press 1 for creating a folder ")
            print("press 2 for reading files and folder ")
            print("press 3 for updating the folder ")
            print("press 4 for deleting a folder ")
            print("press 5 for create file ")
            print("press 6 for reading a file")
            print("press 7 for updating the file ")
            print("press 8 for deleting the file ")
            check = int(input("What do you want : "))
            if check == 1:
                createfolder()
            elif check == 2:
                readfileandfolder()
            elif check == 3:
                updatefolder()
            elif check == 4:
                deletefolder()
            elif check == 5:
                createfile()
            elif check == 6:
                readfile()
            elif check == 7:
                updatefile()
            elif check == 8:
                deletefile()
        else:
            break
    elif check == 5:
        createfile()
        a = input("Do you want to continue then press yes otherwise no")
        if a in ["yes", "Yes"]:
            print("press 1 for creating a folder ")
            print("press 2 for reading files and folder ")
            print("press 3 for updating the folder ")
            print("press 4 for deleting a folder ")
            print("press 5 for create file ")
            print("press 6 for reading a file")
            print("press 7 for updating the file ")
            print("press 8 for deleting the file ")
            check = int(input("What do you want : "))
            if check == 1:
                createfolder()
            elif check == 2:
                readfileandfolder()
            elif check == 3:
                updatefolder()
            elif check == 4:
                deletefolder()
            elif check == 5:
                createfile()
            elif check == 6:
                readfile()
            elif check == 7:
                updatefile()
            elif check == 8:
                deletefile()
        else:
            break
    elif check == 6:
        readfile()
        a = input("Do you want to continue then press yes otherwise no")
        if a in ["yes", "Yes"]:
            print("press 1 for creating a folder ")
            print("press 2 for reading files and folder ")
            print("press 3 for updating the folder ")
            print("press 4 for deleting a folder ")
            print("press 5 for create file ")
            print("press 6 for reading a file")
            print("press 7 for updating the file ")
            print("press 8 for deleting the file ")
            check = int(input("What do you want : "))
            if check == 1:
                createfolder()
            elif check == 2:
                readfileandfolder()
            elif check == 3:
                updatefolder()
            elif check == 4:
                deletefolder()
            elif check == 5:
                createfile()
            elif check == 6:
                readfile()
            elif check == 7:
                updatefile()
            elif check == 8:
                deletefile()
        else:
            break
    elif check == 7:
        updatefile()
        a = input("Do you want to continue then press yes otherwise no")
        if a in ["yes", "Yes"]:
            print("press 1 for creating a folder ")
            print("press 2 for reading files and folder ")
            print("press 3 for updating the folder ")
            print("press 4 for deleting a folder ")
            print("press 5 for create file ")
            print("press 6 for reading a file")
            print("press 7 for updating the file ")
            print("press 8 for deleting the file ")
            check = int(input("What do you want : "))
            if check == 1:
                createfolder()
            elif check == 2:
                readfileandfolder()
            elif check == 3:
                updatefolder()
            elif check == 4:
                deletefolder()
            elif check == 5:
                createfile()
            elif check == 6:
                readfile()
            elif check == 7:
                updatefile()
            elif check == 8:
                deletefile()
        else:
            break
    elif check == 8:
        deletefile()
        a = input("Do you want to continue then press yes otherwise no")
        if a in ["yes", "Yes"]:
            print("press 1 for creating a folder ")
            print("press 2 for reading files and folder ")
            print("press 3 for updating the folder ")
            print("press 4 for deleting a folder ")
            print("press 5 for create file ")
            print("press 6 for reading a file")
            print("press 7 for updating the file ")
            print("press 8 for deleting the file ")
            check = int(input("What do you want : "))
            if check == 1:
                createfolder()
            elif check == 2:
                readfileandfolder()
            elif check == 3:
                updatefolder()
            elif check == 4:
                deletefolder()
            elif check == 5:
                createfile()
            elif check == 6:
                readfile()
            elif check == 7:
                updatefile()
            elif check == 8:
                deletefile()
        else:
            break


