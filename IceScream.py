#This program calculates the retail cost of icecream bars based
#upon the whole sale cost and the retailers markup on small and
#large boxes

#Bars per Box
smallBox = 5
largeBox = 20

#Bar cost by month
juneCost = 0.50
julyCost = 1.00
augustCost = 0.75

#Input for Bars being ordered each month
juneOrder = int(input("Enter the number of bars ordered in June: "))
julyOrder = int(input("Enter the number of bars ordered in July: "))
augustOrder = int(input("Enter the number of bars ordered in August: "))

#Used to calulate how many bars are in half the order
halfOrder = 2

#The following 3 parts calulate how many small and large boxes are 
#obtainable when half of each order is used for small boxes and the
#other half is used for large boxes

juneSmall = juneOrder / halfOrder // smallBox
juneLarge = juneOrder / halfOrder // largeBox

julySmall = julyOrder / halfOrder // smallBox
julyLarge = julyOrder / halfOrder // largeBox

augustSmall = augustOrder / halfOrder // smallBox
augustLarge = augustOrder / halfOrder // largeBox

#calculates how many of each box were put together
smallBoxes = int(juneSmall + julySmall + augustSmall)
largeBoxes = int(juneLarge + julyLarge + augustLarge)

#outputs the number of small and large boxes put together
print("Number of Small Boxes packed: ", smallBoxes)
print("Number of Large Boxes packed: ", largeBoxes)

#calculates the average cost per bar over the three months
totalBars = juneOrder + julyOrder + augustOrder
totalCost = (juneOrder * juneCost) + (julyOrder * julyCost) + (augustOrder * augustCost)
averageCost =  totalCost / totalBars

#Retail Markup factors
smallMarkup = 1.9
largeMarkup = 1.8

#Calculates the price of the boxes based on the cost of
#bars they condain and a corresponding markup fee
smallPrice = averageCost * smallBox * smallMarkup
largePrice = averageCost * largeBox * largeMarkup

#rounds and prints the cost of each box
print("Selling Price Per Small Box: $%.2f" % (smallPrice))
print("Selling Price Per Large Box: $%.2f" % (largePrice))