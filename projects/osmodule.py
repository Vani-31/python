import os 

folder= "C:/Users/vaani/OneDrive/Desktop/renamer"
files=os.listdir(folder)

print("files in the folder :")
for file in files:
    print(file)