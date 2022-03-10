import os 
import shutil
from_dir = 'C:/Users/Lenovo/Downloads'
to_dir="C:/Users/Lenovo/Document_files"
listoffiles=os.listdir(from_dir)
print(listoffiles)
for file_name in listoffiles :
    name,extention=os.path.splitext(file_name)
    #print(name)
    #print(extention)
    if extention=='':
        continue
    if extention in ['.txt','.docx','.doc','.jpeg','.pdf']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+"Document_Files"
        path3=to_dir + '/' + "Document_Files" + '/' + file_name
        print("path1",path1)
        print("path3",path3)
        if os.path.exists(path2):
            print("moving"+file_name+".....")
            shutil.move(path1,path3)
        else:
            os.markedirs(path2)
            print("moving"+file_name+".....")
            shutil.move(path1,path3)