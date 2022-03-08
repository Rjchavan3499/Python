#Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
#Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
#can be found using a formula
import math

def quad(a,b,c):

    name = input("Enter your name :\n ")
    print("Hi, '", name, "'.")
    print(name, ", you are here for finding the real and imaginary roots")
    print("\n Equation is 'A*x*x + B*x + C' ")
    print("\n Please give the following details:")

    try:


        if a != 0:
            d = (b * b) - (4 * a * c)
            if d > 0:
                root1 = float((-b + math.sqrt(d)) / (2 * a))

                root2 = float((-b - math.sqrt(d)) / (2 * a))
                print(" root1 = %.2f", root1, " and root2 = %.2f", root2)
            elif d == 0:
                root1 = root2 = -b / (2 * a)
                print(" root1 = root2 = ", root1)
            else:
                realPart = float(-b / (2 * a))
                imaginaryPart = float(math.sqrt(-d) / (2 * a))
                print(" root1 = ", realPart, " + ", imaginaryPart, " i")
                print()
                print(" root2 = ", realPart, " - ", imaginaryPart, " i")
    except ValueError:
        print(" Enter the Numeric value ")
    except ZeroDivisionError:
        print(" Division by Zero Error ")

x = int(input(" Enter the value of 'A' : \n "))
y = int(input(" Enter the value of 'B' : \n "))
z = int(input(" Enter the value of 'C' : \n "))
result = quad(x,y,z)