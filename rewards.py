################################################################
#This program randomly assigns 1 or 0 to three variables which #
#represent a coin flip.You are then awarded points based on the#
#combination they appear in from first to third                #
################################################################

from random import randint

T = 0 # Tails, T is represented by 0
H = 1 # Heads, H is represented by 1

################################################
#Assigning random integers from T to H (0 to 1)#
################################################

first = randint(T,H) 
second = randint(T,H)
third = randint(T,H)

#######################################################################
#Converting values of first, second and third to corresponding strings#
#if Heads(1) assign string 'H' else value must be Tails(0) assign 'T' #
#######################################################################

if first == H: 
    first = 'H'
else:
    first = 'T'
    
if second == H:
    second = 'H'
else:
    second = 'T'

if third == H:
    third = 'H'
else:
    third = 'T'

###############################
#Output assigned letter values#
###############################

print("The three random coins are: ",first,second,third)

#######################
#Compute Total Rewards#
#######################


totalRewards = 0


if first == 'H':        #if first coin is heads you earn 3 points
    totalRewards += 3
else:                   #otheriwise you get one
    totalRewards += 1
    
if second == 'H' and first == 'H': #if both second and first coin are heads you get 4 points
    totalRewards += 4
else:                              #otheriwise you get one
    totalRewards += 1
    
if third == 'H' or second == 'H': #if either the third or second coin is heads
    if (third != second):
        totalRewards += 5  #and theyre not both heads you get 5 points  
    else:
        totalRewards += 1  #otheriwise you get one (else for nested if statement)
else:
    totalRewards += 1      #otheriwise you get one (else for main if statement)

################################
#ouput for points(totalRewards)#
################################

print("You have earned %s points." % totalRewards)