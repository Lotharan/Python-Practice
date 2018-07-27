#This is a number guessing game

# 1.	generate the random number, don't show to user
# 2.	Prompt user to start guessing
# 3.	check user input vs the random generated number
# 4.	Provide negative response 
# 5.	tell user to guess again
# 6.	if correct provide positive response
# 7.	congratulate user
# 8.	prompt to play again

import random #this module allows for the use of the randint() module

def num_gen():  #generates the random number
    user_num = random.randint(1,100)
    return user_num

def get_started(): #prompt user to start guessing
    guessing = True
    user_num = num_gen()
    print(user_num)
    num_guesses = 0
    while guessing:
        start_guessing = input('Guess a number between 1 and 100').strip() #saves user input
        # print(start_guessing)
        if start_guessing == str(user_num): #if input matches, tells them
            num_guesses +=1                         #they were right, increments counter
            print("That's right!  You guessed the number in",num_guesses, "tries")
            guessing = False
        elif start_guessing > str(user_num):
            print("The number is too high...")
            num_guesses +=1
        elif start_guessing < str(user_num):
            print("The number is too low...")
            num_guesses +=1

get_started()

again = input('Play Again: (Y/N)')
if again.lower() == 'y':
    get_started()
else: 
    sys.exit(0)



