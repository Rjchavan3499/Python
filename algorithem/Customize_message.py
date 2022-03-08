import re
from datetime import date
# Prompts the user for input string
a = print("hello rohit")
b = print("we have your full name Rohit Ashok Chavan")
c = print("your mobile number is +91xxxxxxxx")
d = print("thank you bridgela 06-03-2020")

username = input("enter your username")
if re.match("[A-Za-z]{4,25}||\s[A-Za-z]{4,25}", username):
    print("entered valid name")
else:
    print("username shoulb be one character , one number and one special char")

full_name = input ("enter your full name")
#if re.match("^[a-zA-Z]{4,}(?: [a-zA-Z]+)?(?: [a-zA-Z]+)?$",full_name)
    #print("enter valid fullname")
#else:
    #print("please enter your full name")
num = input("enter your mobile number")
if re.match("[6-9]{1}[0-9]{9}", num):
    print("entered valid  number")
    print("\n")
    print("hello ",username)
    print("we have your full name is our system",full_name)
    print("your moible number is", num)
    today = date.today()
    print("Thank you Bridgelabz", today)
else:
    print("your mobile number should be 10 digit")






