import base64
import os

os.chdir("./b64/files")
files = os.listdir(".")
for file in files:
    newFile = base64.b64encode(file.encode()).decode()
    os.rename(file, newFile) 