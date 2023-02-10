#Train profits

# Assumptions
# kid ticket = $120.50, Adult Ticket = $320

#input
# number of passenger cars
#       Adults in that car
#       kids in that car
# loop for N cars

#output
#total passengers
#percentage of money made from adult tickets 
#percentage of money make for kid tickets

CHILD_RATE = 120.50
ADULT_RATE = 320

Children = 0
Adults = 0
N = int(input("enter number of passenger cars:"))

for X in range(1,N+1,1):
    print("For Car %s" % X)
    Children = Children + int(input("    enter number of kids: "))
    Adults = Adults + int(input("    enter number of Adults : "))

kidRevenue = Children * CHILD_RATE
adultRevenue = Adults * ADULT_RATE
totalRevenue = kidRevenue + adultRevenue

kidPercentage = ((kidRevenue/totalRevenue)*100)
adultPercentage = ((adultRevenue/totalRevenue)*100)
print()
print("Total Passengers", (Adults + Children))
print('revenue percentage from kids: %s%s' % (round(kidPercentage,2),"%"))
print('revenue percentage from adults: %s%s' % (round(adultPercentage,2),"%"))
    

