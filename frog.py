import random

Depth = int(input("Enter the depth of the well as an integer: ")) #User input for Depth of well
Height = 0 #Variable used to keep track of how far the frog climbed
Try = 0 #Variable used to keep track of trys, each loop increases 'Try' by 1
while (Height < Depth): # Height = Depth when the frog makes it out so loop continues till Height =< Depth
    Slip = int(random.randint(0,1)) #Slip is the variable which holds a random int between 0 and 1
    Try += 1 # increments the amount of tries each loop
    if (Slip == 1): #determines what to do if the frog slips i.e Slip = 1
        print("Oops! Slippery patch on jump number", (Try),"!") #Tells user whenever frog slips
        if Height < 3: #statement to prevent Height from going below 0, i.e slipping at 2m returns frog to 0m instead of -1m
            Height = 0 
        else: Height -= 3 #Decreases height when height is greater than 2, i.e not at risk of retuning negative value
    elif (Slip == 0): #increases height climbed when frog doesnt slip
        Height += 5
print("It took the frog", Try, "tries to come out of the",Depth, "metres deep well.") #output with number of trys aswell as the inputed depth

            
    