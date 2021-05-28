import os
from hashlib import *
from tkinter import Tk     
from tkinter.filedialog import askopenfilename
import time

print(" _____ _ _                                         _               _______ ")
print("|  ___(_) | ___    ___ _ __   ___ _ __ _   _ _ __ | |_ ___ _ __   / /___ / ")
print("| |_  | | |/ _ \  / _ \ '_ \ / __| '__| | | | '_ \| __/ _ \ '__| / /  |_ \ ")
print("|  _| | | |  __/ |  __/ | | | (__| |  | |_| | |_) | ||  __/ |    \ \ ___) |")
print("|_|   |_|_|\___|  \___|_| |_|\___|_|   \__, | .__/ \__\___|_|     \_\____/ ")
print("                                       |___/|_|                           ")

print("Please select the file you want to encrypt / decrypt")

time.sleep(1)

Tk().withdraw() 
filename = askopenfilename() 
print(filename)


File_Input = filename
File_Output = str(input("Please, input the name of the output file : "))

Encryption_Key = str(input("Please, input the encryption key for the file : "))

ShaKey = sha256(Encryption_Key.encode('utf-8')).digest()
print(filename)



with open(File_Input, 'rb') as F_Input:
    with open (File_Output, 'wb') as F_Output:
        i = 0
        while F_Input.peek():
            c = ord(F_Input.read(1))
            j = i % len(ShaKey)
            b = bytes([c^ShaKey[j]])
            F_Output.write(b)
            i = i + 1
print("File encrypted !")
print('You can now close this window or it will close in 50000 seconds')

time.sleep(50000)
