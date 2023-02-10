from math import pi, sqrt

g = 9.80665#m/s^2
L = float(input("enter lenght of pendulum: "))

f = (1 / (2*pi)) * (sqrt(g / L))
T = 1 / f

print("frequency is: %f" % f)
print("period is: %f" % T)
