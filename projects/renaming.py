import os 
folder="C:/Users/vaani/OneDrive/Desktop/renamer"
files=[]
for f in os.listdir(folder):
    if f.endswith(".txt"):
        files.append(f)
for index , file in enumerate(files,start=1):
    old_path=os.path.join(folder,file)
    new_name=f"note{index}.txt"
    new_path=os.path.join(folder,new_name)
    os.rename(old_path,new_path)


print("files renamed succesfully and i learned also yayyy")   
