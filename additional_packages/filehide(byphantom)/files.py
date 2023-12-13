#imports
from logging.config import dictConfig
from operator import le
import os
import random
from datetime import datetime
from time import sleep
from traitlets import directional_link

#vars and const

dirname = "WindowsVarHandler"
logname = "fileslogger.txt"
names = ["Windows", "Task", 
         "exe", "System", "windows", "Microsoft", "Server", "valid", "upgrade", "update", "data", "Database"
         , "systemcall", "manager", "binary", "executable", os.getlogin(), "variables", "handler"
         , "object", "code", "coding", "language", "DE", "EN", "assistant", "Desktop"]
file_endings = ["txt", "bin", "server", "exe", "run", "mp4", "mxf", "cpp", "py", "js", "mscdb"]

directorys = {}
dirlist = []
files = {}
deepness = random.randint(10, 20)
processes = 0


#logfile check

try:
    open(file=logname, mode="a")
except FileExistsError:
    pass
except:
    quit()

#functions
def name_gen():
    times = random.randint(1, 5)
    file_name = []
    for i in range(times):
        word = names[random.randint(0, len(names) - 1)]
        file_name.append(word)
    final_file_name = ""
    for i in file_name:
        final_file_name = final_file_name + i
    return final_file_name

def log(msg):
    logtime = datetime.now()
    logtime_final = logtime.strftime("%Y-%M-%D/%h-%m-%S")
    logmessage = logtime_final + "/" + str(msg)
    file = open(file=logname, mode="a").write(logmessage + "|")

#run
def dirspawn():
    deepness = random.randint(100, 300)
    for i in range(deepness):
        dir_name = name_gen()
        os.system("mkdir " + dir_name)
        print(os.getcwd())
        while True:
            try:
                os.chdir(dir_name)
                directorys[dir_name] = os.getcwd()
                dirlist.append(dir_name)
                break
            except:
                pass

def filespawn():
    filecount = random.randint(0, 2)
    for i in range(filecount):
        operation = "touch " + name_gen() + "." + file_endings[random.randint(0, len(file_endings) - 1)]
        os.system(operation)
        print("File in:", os.getcwd(), "created")
        files[operation] = os.getcwd()

while True:
    file = input("Type in the filepath: ")
    try:
        file_hide = open(file=file).read()
        print(file_hide)
        sleep(5)
        break
    except:
        pass

#############
#File
############
try:
    os.rmdir(dirname)
except:
    pass
file_spawned = False
spawn_path = ""
namefile = file.split(sep="/")
name_of_file = namefile[0]
#################.
cur_pwd = os.getcwd().split("/")
goto_pwd = ""
goto_pwd = cur_pwd[0]
for i in range(1, len(cur_pwd)):
    goto_pwd = goto_pwd + "/" + cur_pwd[i]
print("gotopwd: ", goto_pwd)
os.chdir(goto_pwd)
os.mkdir(dirname)
os.chdir(dirname)
dirspawn()
dirchoose = random.choice(dirlist)
dirchoose_name = directorys[dirchoose]
spawn_path = dirchoose_name
hide_file = open(file=name_of_file, mode="w")
hide_file.write(file_hide)
hide_file.close()
file_spawned = True
os.system("clear")
msg = "The File: " + name_of_file + "spawned at:" + spawn_path
open("fileslogger", "w").write(msg)
sleep(10)
opr = "cat" + " " + spawn_path + "/" + name_of_file
os.system(opr)
deepness = 100
try:
    for dir in dirlist:
        path = directorys[dir]
        os.chdir(path)
        dirspawn()
        filespawn()
except:
    pass
print(f"The File: {name_of_file} spawned at: {spawn_path}")