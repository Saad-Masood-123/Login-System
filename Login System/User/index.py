from heading import topheading
from User.calculator import calculate
from User.game import guessGame
# import User.programs as up

import User.programs as up
def useroptions(username):
    a ="welcome to " + username
    topheading(title=a)
    print("""
         Press 1 for calculator
         press 2 for guess game 
         press 3 for internet request
         press 4 for even and odd number
         press 5 for factorial number
        """)
    x = int(input("Please enter the option 1/2 "))
    if(x == 1):
        calculate()
    elif(x == 2):
        guessGame()
    elif(x == 3):
        up.request()
    elif(x == 4):
        up.evenOddNumber()
    elif(x == 5):
        x = int(input("Enter your number "))
        result  = up.factorial(x)
        print(result)
    else:
        print("Invaild Options")

