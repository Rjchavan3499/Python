#Write a program WindChill.java that takes two double command-line arguments tand
# v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
#temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
#National Weather Service defines the effective temperature (the wind chill) to be:

def wind(t,v):
    if ((t >= 0) and (t <= 50)):
        print()
        if ((v >= 3) and (v <= 120)):
            windChill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * pow(v, 0.16)
            print()
            print("Temperature = ", t)
            print("Wind speed  = ", v)
            print("Wind chill  = ", windChill)
            print()
        else:
            print("Enter the Valid Wind Speed")
    else:
        print("Enter the Valid Temperature")

s = int(input("Enter the Temperature from '0' to '50' = "))
m = int(input("Enter the Wind Speed between '3' to '120' = "))
res = wind(s,m)
