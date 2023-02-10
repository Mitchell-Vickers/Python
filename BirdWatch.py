
#this program is used to record bird sightings and calculates their average
#sightings and returns the bird(s) that are seen the most

def main():
    birds = []
    frequency = []
    initializeList(birds,frequency)
    print("Average number of sightings is %d" % findAvgFreq(frequency))
    print()
    findHighFreq(birds,frequency)
    
    
    # creates lists for birds and frequency
    # @param species is list of birds
    # @param freq is list of frequencies  
def initializeList(species,freq):
    newBirdSighting = '0'
    while newBirdSighting != 'end' :
        newBirdSighting = str(input("Enter the bird's name or end to terminate: "))
        if newBirdSighting != 'end' :
            species.append(newBirdSighting)
            newBirdFrequency = int(input("Enter the frequency of sighting: "))
            freq.append(newBirdFrequency)
    
# finds average frequency of sightings
# @param List of frequencies 
def findAvgFreq(List):
    aveFrequency = sum(List) / len(List)
    return aveFrequency
   
    
# find and prints the birds that are seen the most. i.e if two
#birds are seen at the same highest frequency it will print both
# @param species is list of birds
# @param freq is list of frequencies
def findHighFreq(species,freq):
    print("The following birds were seen most frequently:")
    highOccurance = max(freq)
    for i in range(len(freq)) :
        if freq[i] == highOccurance:
            print(species[i])
        
    

    


main()
    