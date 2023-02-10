# This Program converts Martian change into its lightest coin Maruvian
# where 1 Maruvian = 2 Caruvian = 4 Taruvian = 24 Paruvians by coverting
# each coin type to Paruvians and then to as many maruvians as possible
# in order to evenly split amongst friends 

maruvianConversionFactor = 24 # Paruvians
caruianConversionFactor = 12 # Paruvians
taruvianConversionFactor = 6 # Paruvians

#Input for  owned currency and number of friends
ownedMaruvians = int(input("Please enter the number of Maruvians: "))
ownedCaruvians = int(input("Please enter the number of Caruvians: "))
ownedTaruvians = int(input("Please enter the number of Taruvians: "))
ownedParuvians = int(input("Please enter the number of Paruvians: "))
numFriends = int(input("Please enter the number of friends: "))

#Caruvian to Paruvian Conversion
ownedParuvians += (ownedCaruvians * caruianConversionFactor)
ownedCaruvians = 0

#Taruvian to Paruvian Conversion
ownedParuvians += (ownedTaruvians * taruvianConversionFactor)
ownedTaruvians = 0

#Paruvian to Marvian Conversion - Computes remaining Paruvians as well 
ownedMaruvians += (ownedParuvians // maruvianConversionFactor)
ownedParuvians = ownedParuvians % maruvianConversionFactor

#Outputs the total Maruvians owned after conversions
print("Marvin has %s Maruvian(s) in total." % (ownedMaruvians))

#Computes the amount of Maruvians everyone gets
sharedMaruvians = ownedMaruvians // (numFriends + 1)

#updates total maruvians remaining
ownedMaruvians -= (sharedMaruvians * (numFriends + 1))

#Outputs the results 
print("He gives %s Maruvian(s) to himself and to each of his %s friends." % (sharedMaruvians,numFriends))
print("Marvin puts %s Maruvian(s) and %s Paruvian(s) back in the jar." % (ownedMaruvians,ownedParuvians))


      
