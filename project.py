import os
import shutil

source= r"C:\Users\Vishwajeet Kumbhar\OneDrive\Desktop\PYTHON\class102"
destination= r"C:\Users\Vishwajeet Kumbhar\OneDrive\Desktop\PYTHON\class102\documents"

list_of_files=os.listdir(source)
print(list_of_files)

for x in list_of_files:
    name, extension = os.path.splitext(x)
    if extension == "":
        continue
    if extension in [".pdf", ".ppt", ".txt"]:
        path1= source + "/" + x
        path2= destination 
        path3= destination + "/" + x

        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)