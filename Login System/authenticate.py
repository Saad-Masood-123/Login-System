import os
from heading import topheading
from User.index import useroptions;






def login():
    os.system('cls')
    topheading(title="Welcom to Login System",length=100)

    count = 0
    username = input("Enter your username ")
    password = input("Enter your password ")

    with open('database.txt', 'r') as file:
        for line in file:
            file_username, file_password,file_status = line.strip().split(',')
            if(username == file_username and password == file_password):
                count = 1
                if(file_status == "admin"):
                    print("admin")
                else:
                    # useroptions(username=username)
                    print("user")
                break
            # else:
            #     login()
    print(count)
    if(count == 0):
        confirmation  =input("you want to try again N/Y ")
        if(confirmation.lower() == "y"):
            login()
login()
    






    # topheading(title="Enter your username",length=30,char="?")
    # # username = input()
    # topheading(title="Enter your password",length=30,char="*")
    # password = input()
    # topheading("Welcome",80,"!")
    # topheading("login system",50,"=")
    # topheading("Login System")
    # topheading("Login System",100,"?")
    # topheading(title="Login Systemt",length=80,char="!")
    # topheading(title = "Login System",char="=")



