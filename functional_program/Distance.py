#Write a program Distance.java that takes two integer command-line arguments x
#and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
#formulae to calculate distance = sqrt(x*x + y*y).
def distance(a1 ,a2,b1,b2):

    result= ((((a2 - a1 )**2) + ((b2-b1)**2) )**0.5)
    print("distance between",(a1,a2),"and",(b1,b2),"is : ",result)

x1=int(input("enter x1 : "))
x2=int(input("enter x2 : "))
y1=int(input("enter y1 : "))
y2=int(input("enter y2 : "))
result1 = distance(x1,x2,y1,y2)

