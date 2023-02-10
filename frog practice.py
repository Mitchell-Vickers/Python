from random import randint 

depth = int(input("enter well depth: "))

height = 0
jump = 0

while height < depth:
    slip = randint(0,1)
    print("slip?",slip)
    if slip == 1:
        if height < 3:
            height = 0
            jump = jump + 1
        else:
            height = height - 3
            jump = jump + 1
        print("slippery patch on jump %s" % jump)
    else:
        height = height + 5
        jump = jump + 1
        

    
print("frog made it out on jump %s" % jump)
        

    
        
               
    