import os,re

drives = re.findall(r"[A-Z]+:[\\]+", os.popen("mountvol /").read(), re.MULTILINE)

file_name=""
folder_name="deepak"
i=0
j=0
cwd = os.getcwd()
for drive in drives:
    try:
        os.chdir(f"{drive}\\")
        for root, dirs, files in os.walk(f"{drive}\\"):
            if(file_name!=""):
                for f in files:
                    if(f==file_name):
                        print(f"Yes this file({file_name}) is in the system and the location is  : ",end="")
                        print(f" {root}\\{f}")
                        i=i+1

            if(folder_name!=""):
                for d in dirs:
                    if (d == folder_name):
                        print(f"Yes this folder({folder_name}) is in the system and the location is  : ", end="")
                        print(f"{root}\\{d}")
                        j=j+1

    except:
        pass


if(file_name!=""):
    print(f"you have {i} files with {file_name} name")

if(folder_name!=""):
    print(f"you have {j} folder's with {folder_name} name")


