#I haven't yet added a check for if the entered username and password are blank (this displays 'Account Found!')

import os
os.system("cls")

print("Please input your username and password to log into your account, or continue as a guest:\n")

def Ask():
    UsNaLogin = input("Username:\n")

    if UsNaLogin != "guest":
        UsPaLogin = input("\nPassword:\n")
        AccountLogin = UsNaLogin + "  " + UsPaLogin
        AccountConfirm = open("c:\\Users\\jacko\\Python Projects\\Account_stuff\\AccountFile.txt","r")

        if  AccountLogin in AccountConfirm.read():
            print("\nAccount Found!")
            file = open("c:\\Users\\jacko\\Python Projects\\Account_stuff\\Top_secret_"+UsNaLogin+".txt","w")
            text = ("This is top secret file that belongs to ")
            textToWrite = text + UsNaLogin
            file.write(str(textToWrite))
            file.close
        else:
           os.system("cls")
           print("\nAccount not found, please try again.\n")
           Ask()
    else:
        print("Continuing as guest.")
        file = open("c:\\Users\\jacko\\Python Projects\\Account_stuff\\Not_so_secret.txt","w")
        file.write("This is a guest file.\n\n")
        file.close
Ask()
