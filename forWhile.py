limit = 5
c = 0
d = 0
x = 0
while (x < limit):
    isThis = int(input("Enter the input value: "))
    if isThis > limit:
        c += 1
    else:
        d += 1
    x += 1
print("Value of c is ", c)
print("Value of d is ", d)