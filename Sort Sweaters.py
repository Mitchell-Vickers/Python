# sweater codes, sort codes by size idecated by last two digets

sweaterCodes = [12309, 32109, 54204, 35410, 87508, 50404, 94307, 94306, 54205, 12303, 32111, 32110] #constant list of sweater codes
sortedCodes = list(sweaterCodes) # copy of sweater codes to be sorted 
x = len(sweaterCodes) # variable to keep code ranges below organized
sizeToSort = [] #list used to access the last two digets of the sweater codes 

for i in range(x):
    tempSize = (str(sortedCodes[i])[3:5]) # stores the last digets of each sweaterCode at different index values
    sizeToSort.append(int(tempSize)) #adds the last two didgets for each index value to new list, in order presented
    
for i in range(x):
    for j in range(1, x-i):
        if sizeToSort[j-1] > sizeToSort[j]: #tests if the accessed index value against the next
            (sortedCodes[j-1], sortedCodes[j]) = (sortedCodes[j], sortedCodes[j-1]) # swapping list elements to sort in accending order
            (sizeToSort[j-1], sizeToSort[j]) = (sizeToSort[j], sizeToSort[j-1]) # swapping second list to keep the valuse and indexes the same


print("The unsorted list of codes is:")
print(sweaterCodes)
print()
print("The sorted list of codes is:")
print(sortedCodes)
