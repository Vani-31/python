import os
folder= r"C:\Users\vaani\OneDrive\Desktop\images"
files=[]
for f in os.listdir(folder):
    f.endswith(".jpg")or f.endswith(".png")
    files.append(f)
for index, file in enumerate(files , start=1):
    old_path=os.path.join(folder,file)
    new_name=f"image{index}.png"
    print(f"{file} is changed to {new_name}")
    new_path=os.path.join(folder,new_name)
    os.rename(old_path, new_path)
print("sucessfully learned automation")

