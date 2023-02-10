#This program takes a user input as a string and replaces the vowels
#a,e,i,o,u with an asterisk and prints out the word with the vowels replaced

#User input for the string to be modified

word = str(input("Please enter a word (zzz to exit): ")) 

# loop which ends when the sentinel value "zzz" is entered as input

while (word != "zzz"):
    
    noVowels = "" # variable used to build new word with the vowels replaced as asteriskes
    
    # Nested loop which indexes (word) adding the non-vowels as is to the new word (noVowels)
    # and adds the vowels as an asterisk i.e word = water , noVowels = w + * + t + * + r = w*t*r
    
    for i in range (0,len(word),1):
        
        if (word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u"):
            noVowels += "*" 
        else:
            noVowels += word[i]
    
    # output for the original and modified words
    
    print("The original word is: %s" % word)
    print("The word without vowels is: %s" % noVowels)
    print()
    
    #updating (word) to continue or end the loop which ends the program
    
    word = str(input("Please enter a word (zzz to exit): "))