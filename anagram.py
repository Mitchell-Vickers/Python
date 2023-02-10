
##
# Program computes wether or not two user inputted strings are anagrams
#

def main():
  playAgain = "yes"
  while playAgain == 'Yes' or playAgain == 'yes' :
    firstWord = str(input("enter the first word: "))
    secondWord = str(input("enter the second word: "))
    isAnagram(firstWord, secondWord)
    print()
    response = str(input("Do you wish to check for more anagram words? (yes or no): "))

## function which Computes wether or now two words are anagrams
# @param wordOne is the first word user inputs
# @param wordTwo is the second word user inputs
def isAnagram(wordOne, wordTwo):
    wordOne = (wordOne.lower())
    wordTwo = (wordTwo.lower())
    sortedWordOne = sorted(wordOne)
    sortedWordTwo = sorted(wordTwo)
    if sortedWordOne == sortedWordTwo :
        print("the two words %s and %s are anagrams" % (wordOne, wordTwo))
    elif len(wordOne) != len(wordTwo) :
        print("the two words %s and %s are not the same length, hence cannot be annograms" % (wordOne, wordTwo))    
    else:
        print("the two words %s and %s are not anagrams" % (wordOne, wordTwo))
main()
