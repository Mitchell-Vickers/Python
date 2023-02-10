##
# This program decodes a 10 character a-z string using the following scheme:
# Q = 0, Z = 1, ABC = 2, DEF = 3, GHI = 4, JKL = 5, MNO = 6, PRS = 7, TUV = 8, WXY = 9
#
def main():
   code = str(input("Please enter the code (or Done to terminate): ")) #user input for code
   code = code.upper() #formatting code to uppercase
   
   while code != "DONE": # loop until user inputs done as the code (not case sensitive)
      # Check if the code is valid
      if isCorrect(code):
         print()
         # Get the decoded number and format it before printing
         printNum(code,decodeCode(code))
      else:
         print("Incorrect code") #catch all for incorrect entries
         
      print() # update loop conditional value
      code = str(input("Please enter the code (or Done to terminate): "))
      code = code.upper()     
  
## Checks if the entered string is in the right form a-z and 10 charcater long
# @param code is the string to be evaluated
# @return True or False 
#
def isCorrect(code):
   correctLength = 10
   lowASCII = 65
   highASCII = 90
   if len(code) == correctLength:
      for i in range(len(code)):
         if ord(code[i]) not in range(lowASCII,highASCII):
            return False
         else:
            return True
   else:
      return False

## Decodes string and creates new string for decoded string
# @param code is the string to be decoded
# @return decoded which is the decoded number 
#
def decodeCode(code):
   decoded = ""
   for i in range(len(code)):
      if code[i] == "Q":
         decoded += "0"
      elif code[i] == "Z":
         decoded += "1"
      elif code[i] == "A" or code[i] == "B" or code[i] == "C":
         decoded += "2"
      elif code[i] == "D" or code[i] == "E" or code[i] == "F":
         decoded += "3"
      elif code[i] == "G" or code[i] == "H" or code[i] == "I":
         decoded += "4"  
      elif code[i] == "J" or code[i] == "K" or code[i] == "L":
         decoded += "5"
      elif code[i] == "M" or code[i] == "N" or code[i] == "O":
         decoded += "6"
      elif code[i] == "P" or code[i] == "R" or code[i] == "S":
         decoded += "7"
      elif code[i] == "T" or code[i] == "U" or code[i] == "V":
         decoded += "8"
      elif code[i] == "W" or code[i] == "X" or code[i] == "Y":
         decoded += "9"  
   return decoded      

## prints the user inputted code and the decoded code, formats decoded number as ###-###-####
# @param code is the user inputted code
# @param decoded is the decoded number
# @return output
#
def printNum(code,decoded):
   print("The code for phone number is: ", code)
   print("The decoded number is: ", decoded[:3] + "-" + decoded[3:6] + "-" + decoded[6:])

main()