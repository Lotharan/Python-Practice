#This program will be a dice rolling simulator, assuming d20

import random #random module to be able to use the randint() method below

def roll(sides):
    num_rolled = random.randint(1,sides)
    return num_rolled

def roll_the_bones(): #this is the main function
    sides = 20
    rolling = True
    while rolling:
        roll_again = input('Roll the bones? Enter=Yarp, N=Narp')
        if roll_again.lower() != 'n':
            num_rolled = roll(sides)
            print('You rolled a',num_rolled )
        else:
            rolling = False
    
    print('The Bones tell you nothing.')

roll_the_bones() 
#This is where the program begins, using the function(s) defined above
