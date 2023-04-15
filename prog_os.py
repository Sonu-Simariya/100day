import os
# os.mkdir("sonu")

# to get path
print(os.getcwdb())

# to remove file
file='file.txt'
loc="C:\\Users\\lalit\\Desktop\\100day\\sonu"
path=os.path.join(loc,file)
os.remove(path)

# to remove directory
os.rmdir(loc)

# to creating multiple directory
for i in range(1,100):
    os.mkdir(f"sonu\Day {i}")



# to remove multiple directory
for i in range(1,100):
    os.rmdir(f"sonu\Day {i}")
