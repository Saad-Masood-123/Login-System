import os 
def admin_options(username):
    login_heading : str = "Welcome to " + username
    print(f'{login_heading:=^50} \n')
    flag = 0;
    while flag != 3:
        #os.system("cls")
        print("""
        Press 1 add new user
        Press 2 update existing user  
        Press 3 Terminate Program  
        """)    
        option = int(input('Enter your choice (1/2/3) : '))

        if(option == 1):
            register()
        elif(option == 2):
            update()
        elif(option == 3):
            flag = 3
        else:
            print("option is not correct")            



def register():
    heading : str = "Add new user" 
    print(f'{heading.upper():=^50} \n')
    username = input("Enter  username ")
    password = input("Enter  password ")
    status  = input("Enter admin/user ")
    if(username):
        global flag
        with open('database.txt', 'r') as file:
            for line in file:
                file_username, file_password,file_status = line.strip().split(',')
                if(username==file_username):
                    flag = 1
                    

        if(flag != 1):
            with open("database.txt", 'a') as file:
                file.write(f"{username},{password},{status.lower()}\n")
        else:
            print("User already exists.")
def update():
    updated_data = []
    username = input("Enter  username ")
    with open("database.txt", 'r') as file:
        for line in file:
            file_username, file_password,file_status = line.strip().split(",")
            if file_username == username:
                password = input("Enter  password ")
                status  = input("Enter admin/user ")
                updated_data.append([file_username,password,status])
            else:
                updated_data.append([file_username,file_password,file_status])
    with open("database.txt", 'w') as file:
        for person in updated_data:
            file.write(f"{person[0]},{person[1]},{person[2]}\n")            
    