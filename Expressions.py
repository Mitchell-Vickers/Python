# this program solves the calculation for the sum 'n' number of fractions whos
# numerator and denominator increase by 1 after each addition starting at 1/2 i.e

# 1/2 + 2/3 + 3/4 ... n/n+1

n = int(input("Enter a value for n: ")) # user inputted intiger for n

val1 = 1 #starting numerator
val2 = 2 #starting denominator
total = 0 #variable later used to store sum of the fractions

# loop to compute the sum of n number of fractions

for i in range(n):
    total += val1 / val2
    val1 += 1
    val2 += 1

#output for the sum of n terms

print("The sum of %d terms is %.2f." % (n,total))