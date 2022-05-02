from base64 import decode
from cryptography.fernet import Fernet #encription 

''' 
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: #opens key file in wb mode. writes a key with Fernet
        key_file.write(key)'''# 3 quotation marks turns funtion into a comment after we ran the funtion once to get write key


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()    
    return key

key = load_key()
fer = Fernet(key)

def view(): #function 
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip() #rstrip doesn't reed the "n/"
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Acount Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f: #with closes the file after it is modified # open(file you want to open, mode type a,w,r)
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view/add), press q to quit? ").lower()
    if mode == "q":
        break
    
    elif mode == "view":
        view()
    elif mode == "add":
        add() 
    else:
        print("Invalid mode.")
        continue
