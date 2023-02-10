#Program takes integers as input for the variables
#a, p, m1 and m2 in order to compute the value of G

from math import pi

a = int(input("Enter an integer for a: "))
p = int(input("Enter an integer for p: "))
m1 = int(input("Enter an integer for m1: "))
m2 = int(input("Enter an integer for m2: "))

#Computes the value of G
G = (4 * (pi ** 2) * (a ** 3)) / ((p ** 2) * (m1 + m2))

#Prints value of G to two decimal places 
print("Value of G = %.2f" % G)