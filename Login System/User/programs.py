
def request():
    status = 200
    match status:
        case 200:
            print("request successfully")
        case 400:
            print("Bad request")
        case 404:
            print("Not found")
        case 418:
            print("I'm a teapot")
            # If an exact match is not confirmed, this last case will be used if provided
        case _:
            print("Something's wrong with the internet")

def evenOddNumber():
    flag  = True
    while flag == True:
        x  = int(input("Enter random your number "))
        if(x  % 2 == 0):
            print("Even Number")
        else:
            print("odd Number")  
    
        y = input("Do you want play again press y/n ")
        if(y.lower() == "y"):
            continue
        else:
            flag = False

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
