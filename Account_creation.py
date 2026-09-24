import os

os.system("cls")

print("Please input a username and password to create your account:")
 
def UserNameAsk():

    global UsNa
    UsNa = input("Create Username:\n")

    if UsNa.isspace():
        os.system("cls")
        print("Please input a username")
        UserNameAsk()
    elif UsNa == "":
        os.system("cls")
        print("Please input a username")
        UserNameAsk()    
    else:
        PasswordAsk()


def PasswordAsk():

    global UsPa
    UsPa = input("Create Password:\n")

    if UsPa.isupper():
        os.system("cls")
        print("Password must contain atleast one lowercase letter, please try again.")
        PasswordAsk()
    elif UsPa.islower():
        os.system("cls")
        print("Password must contain atleast one uppercase letter, please try again.")
        PasswordAsk()
    elif UsPa.isalpha():
        os.system("cls")
        print("Password must contain atleast one number/symbol, please try again.")
        PasswordAsk()
    elif UsPa.isspace():
        os.system("cls")
        print("Please input a password.")
        PasswordAsk()
    elif UsPa == "":
        os.system("cls")
        print("Please input a password.")
        PasswordAsk()
    else:
        Confirm()

def Confirm():
    
    global Confirmation

    File = open("C:\\Users\\jacko\\Python Projects\\Account_stuff\\AccountFile.txt","r")
    if UsNa in File.read():
        print("Username already in use, please try again.")
        UserNameAsk()
    else:

        Confirmation = input("Password Confirmation:\n")
    
        if Confirmation != UsPa:
            os.system("cls")
            print("Password Confirmation must be the same as Password")
            Confirm()
        else:
            File = open("C:\\Users\\jacko\\Python Projects\\Account_stuff\\AccountFile.txt","a")
            File.write(UsNa)
            File.write("  ")
            File.write(UsPa)
            File.write("\n")
            File.close()
            print("Account created!")

os.system("cls")
UserNameAsk()