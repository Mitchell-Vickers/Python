#This program finds the days in a month based on the year.The program
#first converts the month number to the month name through a series of
#if statements wich also corresponds to the number of days in that month.
#for febuary it checks if its a leap year to decide 28 or 29 days

month = int(input("Enter a month as an integer (1-12): "))
year = int(input("Enter a year: "))
days = 0

if month == 1:
    month = "January"
    days = 31
    
elif month == 2:
    month = "Febuary"
    if (year % 4 == 0) and (year % 100 != 0):  #A year is a leap year if evenly divisible by 4 and not by 100
        days = 29
    elif (year % 4 == 0) and (year % 400 == 0): # unless it is also devisible by 400
        days = 29
    else:     #if the year passes the last two if statements its not a leap year
        days = 28 
        
elif month == 3:
    month = "March"
    days = 31
    
elif month == 4:
    month = "April"
    days =  30
    
elif month == 5:
    month = "May"
    days = 31
    
elif month == 6:
    month = "June"
    days = 30
elif month == 7:
    month = "July"
    days = 31
    
elif month == 8:
    month = "August"
    days = 31
    
elif month == 9:
    month = "September"
    days = 30
    
elif month == 10:
    month = "October"
    days = 31
    
elif month == 11:
    month = "November"
    days = 30
    
elif month == 12:
    month = "December"
    days = 31

#output for the days in the month of the year

print("There are %d days in %s of %d" % (days,month,year))