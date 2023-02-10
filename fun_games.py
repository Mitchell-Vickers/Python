#
# fun_games.py presents the user two options for games to play
# and takes inputs from the user for each game
#


from random import randint

def main() :

    game = displayMenu(1,2)
## range of gameFirst and gameLast i.e 2 games is 1,2 while
## 3 games is 1,3 presenting options 1,2 and 3
# @param gameFirst is the first Game you can choose
# @param gameLast is the last game choice
def displayMenu(gameFirst, gameLast) :
    play = 'y'
    while play == 'y' or play == 'Y' :    
        print("choose one of the following games to play")
        print("1. Guess the Number")
        print("2. Aim For The Target")
        gameChoice = int(input("Enter your Choice of Game as 1 or 2: "))
        print()
        while gameChoice < 1 or gameChoice > 2 :
            gameChoice = int(input("Invalid Entry, Enter your Choice of Game as 1 or 2: "))
    
        if gameChoice == 1 :
            guessTheNumber(1, 50)
        else :
            aimForTarget(1,200)
        print()
        play = str(input("Do you wish to play again? enter y or n: "))
    if play == 'n' or play == 'N' :
       
        print("Goodby. Hope you enjoyed Playing")
           

## plays the game guessTheNumber and computes outcome
# @param low is the lowest number the user can pick
# @param high is the highest number the user can pick
def guessTheNumber(low, high) :
    print("Let us play guess the number")
    print("I am thinking of a number between 1 and 50 (inclusive)")
    print("try to guess the number and i will give you hints along the way")
    print("you have at most 5 tries to guess the right number")
    print()
    userChoice = int(input("Enter a value between %s and %s: " % (low, high)))
    while userChoice < low or userChoice > high :
        userChoice = int(input("Enter a value between %s and %s: " % (low, high)))
    computerChoice = randint(low,high)
    maxTries = 5
    tries = 1
    while tries < maxTries and userChoice != computerChoice :
        if userChoice < computerChoice :
            print("Too low! Guess a number higher than %d" % userChoice)
            print()
            userChoice = int(input("Enter a value between %s and %s: " % (low, high)))           
        elif userChoice > computerChoice:
            print("Too high! Guess a number lower than %d" % userChoice) 
            print()
            userChoice = int(input("Enter a value between %s and %s: " % (low, high)))
        tries = tries + 1
    if userChoice == computerChoice :
        print("Congradulations!!!! You win in %d tries" % tries)
    else:
        if userChoice > computerChoice:
            print("Too high! Guess a number lower than %d" % userChoice)
        else:
            print("Too low! Guess a number higher than %d" % userChoice)
        print()     
        print("Game over. You used up all %d tries" % maxTries)
        print("The number was %d - better luck next time" % computerChoice)
    return userChoice   


## plays the game aimForTarget computing the computers circle
## choice and the user choice then calls upon getPoints to show score
# @param low is the lowest number the user can pick
# @param high is the highest number the user can pick
def aimForTarget(low, high) :
    playerOne = str(input("Player 1 enter your first name: "))
    playerOneNumber = int(input("%s please enter a number between %d and %d: " % (playerOne, low, high)))
    playerTwo  = str(input("Player 2 enter your first name: "))
    playerTwoNumber = int(input("%s please enter a number between %d and %d: " % (playerTwo, low, high)))
    rndPlayerOneCircle = randint(1,4)
    rndPlayerTwoCircle = randint(1,4)    
    plrOnePts = getPoints(playerOneNumber, rndPlayerOneCircle)
    plrTwoPts = getPoints(playerTwoNumber, rndPlayerTwoCircle)
    print("points for %s are %d" % (playerOne, plrOnePts))
    print("Random circle for player 1 was %d" % rndPlayerOneCircle)
    print("points for %s are %d" % (playerTwo, plrTwoPts))
    print("Random circle for player 2 was %d" % rndPlayerTwoCircle)
    if plrOnePts > plrTwoPts :
        print("%s Wins!" % playerOne)
    elif plrOnePts == plrTwoPts :
        print("Its a tie!")
    else:
        print("%s Wins!" % playerTwo)

## calculates the points for function aimForTarget
# @param userNum is the number the user picked for aimForTarget(low,high)
# @param rndCircleNum is the circle number between 1 and 4
def getPoints(userNum, rndCircleNum):
    userCircleNum = 0 
    
    if userNum < 50 :
        userCircleNum = 1
        userPoints = 100
    elif userNum > 50 and userNum <= 100 :
        userCircleNum = 2
        userPoints = 50
    elif userNum > 100 and userNum <= 150 :
        userCircleNum = 3
        userPoints = 65
    else :
        userCircleNum = 4 
        userPoints = 75
        
    if rndCircleNum == 1 :
        circlePoints = 100
    elif rndCircleNum == 1 :
        circlePoints = 50
    elif rndCircleNum == 1 :
        circlePoints = 65
    else :
        circlePoints = 75
    
    if userCircleNum == rndCircleNum :
        Points = float(circlePoints)
    elif userCircleNum > rndCircleNum :
        points = float(abs((userPoints - circlePoints) / 2))
    else:
        points = float(circlePoints / 2)
    
    return points
    
    


main()   