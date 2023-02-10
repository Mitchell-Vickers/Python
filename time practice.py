# input = some time in seconds ex 86399
# output = in hr/min/sec ex 23:59:59

Input = int(input("enter time in seconds"))
seconds  = int(Input % 60)
Input = Input - seconds
minInSeconds = (Input % 3600)
Input = Input - minInSeconds
minutes = int(minInSeconds / 60)
hours = int((Input / 60)/60)
print("%02d:%02d:%02d" % (hours,minutes,seconds))


        
