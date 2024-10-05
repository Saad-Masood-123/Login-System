def calculate():
    flag = True
    while flag == True:  
        x = int(input ("Enter your first value"))
        op = input("select opertor + - * / ")
        y = int(input("Enter your second value "))      
        if(op == "+"):
            print(x + y)
        elif(op == "-"):
            print(x - y)
        elif(op == "*"):
            print(x * y) 
        elif(op == "/"):
            print(x / y) 
        else:
            print("Invalid Opertor")

        flag_input = input("Do you want to continue press N/Y ")
        if(flag_input.lower() == "n"):
            flag = False 