import base64

def encrpt(passwd):
    encrypted = base64.b64encode(passwd.encode())
    print(encrypted)

userpass = input("Enter password: ")

encrpt(userpass)