# this program is used to keep track of packages and where their destination for a company
# while making sure the delivery truck does not get over loaded.

# Initial number of packages to be delivered to each zone, updated as they get entered

northZone = 0
eastZone = 0
southZone = 0
westZone = 0

# variable used to determine if following loop continues i.e, if the truck is full

estimatedWeight = 0

# User input for the weight limit of the current delivery truck being loaded

weightLimit = int(input("Please enter the weight limit of the truck: "))

print() #separator for weightLimit and sorting loop inputs

# loop which continues until a packege if loaded would put the truck overweight

while (estimatedWeight <= weightLimit): #
    
    packageWeight = int(input("Please enter the weight of a package: ")) # input for the weight of each package
    estimatedWeight += packageWeight # updating the weight of the truck IF last package was put on the truck
    
    if estimatedWeight <= weightLimit: # checks if estimate isnt over the capacity before loading the package onto the truck
       
        packageID = int(input("Please enter the package ID number: ")) # user inputted tracking number
        packageZone  = str(input("Please enter the zone: ")) # user inputted delivery zone
        
        print()
        
      # the following code corrects common spelling errors for each zone and updates total packages for that zone
      
        if(packageZone == "North" or packageZone == "north" or packageZone ==  "N" or packageZone == "n"):
            packageZone = "North"
            northZone += 1 
        elif(packageZone == "East" or packageZone == "east" or packageZone == "E" or packageZone == "e"):
            packageZone = "East"
            eastZone += 1
        elif(packageZone == "South" or packageZone == "south" or packageZone == "S" or packageZone == "s"):
            packageZone = "South"
            southZone += 1
        elif(packageZone == "West" or packageZone == "west" or packageZone == "W" or packageZone == "w"):
            packageZone = "West"
            westZone += 1
        
        # output confirming if package made it on the truck along with its details
        
        print("The following package is on the truck:")
        print("Pkg No. = %d , Zone = %s , Pkg Wgt = %.1f" % (packageID,packageZone,packageWeight))
       
        print()
    else:          # required print statements to keep formatting correct when package gets rejected
        print() 
        
# output for the packages per delivery zone

print("%d packages are on the truck for East zone." % eastZone)
print("%d packages are on the truck for West zone." % westZone)
print("%d packages are on the truck for North zone." % northZone)
print("%d packages are on the truck for South zone." % southZone)

print()

# calculation and output for the total packages put on the truck 

packages = northZone + eastZone + southZone + westZone
print("%d packages are loaded on the truck" % packages)
      