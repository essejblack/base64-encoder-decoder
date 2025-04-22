import base64
import os

os.chdir("./b64/files")
files = os.listdir(".")
for file in files:
    content = open(file, "r").read()
    newContent = base64.b64decode(content).decode()
    newFile = base64.b64decode(file)
    os.rename(file, newFile)
    with open(newFile, "w") as f:
        f.write(newContent)