import random

Accepted = 0 #Initial Value to be incremented as number of residence accepted increases
Response = 'yes' #Initial response set to 'yes' to start loop, updated to yes or no as user wishes at end
while (Response == 'yes'): # Loop keeps processing applicants and increasing the number of Accepted when requirements are met
    ID = input("Enter the applicant ID: ") # input for applicant ID
    Program = input("Enter desired residency program: ") #input for applicants desired residency program
    print("") # prints a space to seperate input and output
    
    I1 = random.randint(1,10) #\
    I2 = random.randint(1,10) #|
    I3 = random.randint(1,10) #|
    I4 = random.randint(1,10) #> Assigning random interviewer scores, I#, Where I is Interviewer 
    I5 = random.randint(1,10) #|
    I6 = random.randint(1,10) #|
    I7 = random.randint(1,10) #|
    I8 = random.randint(1,10) #/
    
    Average = (I1+I2+I3+I4+I5+I6+I7+I8)/8 # Calculating Average Interviewer Score
    
    print("Interviewer Scores:",I1,I2,I3,I4,I5,I6,I7,I8) #prints interviewer scores
    print("Average:", Average) #prints average of interviewer scores
    
    if (Average >= 7): # Compares grade to required grade to be accepted into desired residency
        print("Applicant", ID , "is accepted in the", Program, "residency program")
        Accepted += 1  # Increments the number of accepted applicants by 1
        
    elif (Average >= 5 and Average < 7): # Compares grade to required grade to be accepted into an available residency
        print("Applicant", ID , "will be matched with an available residency spot.")
        Accepted += 1  # Increments the number of accepted applicants by 1
        
    else: # Lets user know that the grades for this applicant werent high enought to be accepted into any residency
        print("Applicant", ID , "is not accepted into the residency program at this time.")
        print(" ")
        Response = input("Do you want to process another applicant? (yes or no) ") #Updates the Response value, yes continues loop, no ends it
        
print("The total number of residents accepted is: ",Accepted) # Prints total applicants accepted for user to know
