import base64
import os

os.chdir("./b64/files")
files = os.listdir(".")
for file in files:
    newFile = base64.b64decode(file)
    os.rename(file, newFile)