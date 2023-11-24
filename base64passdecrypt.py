import base64

def decrpt(passwd):
    decrypted = base64.b64decode(passwd)
    print(decrypted)

userpass = input("Enter base64 password: ")

decrpt(userpass)