import os
f = open("programdb.txt", "w")
for root, dirs, files in os.walk("C:\ProgramData\Microsoft\Windows\Start Menu\Programs"):
    for file in files:
        fileending = ".lnk"
        if file.endswith(fileending):
            path_file = os.path.join(root,file)
            f.write(path_file + "\n")
f.close()

def readdb(program):
    with open("programdb.txt") as f:
        

readdb("c")
