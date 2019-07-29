# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:57:47 2019

@author: Stephen Wharton
"""


import random
games = ''
print("A random integer guessing game")

# Ask how many games to play
while games == '':
    try:
        games = int(input("How many games would you like to play? "))
    except:
        print("Try again using integers")
        continue
        
for game in range(0,games):
    # Initialise variables
    target = random.randint(1,25)
    guess = 0
    attempts = 1
    print("\nGame ",game+1, "of",games)
    
    while target != guess:
        try:
            guess = int(input("Choose an integer between 1 and 25: "))
            if guess<1 or guess>25:
                raise
        except:
            print("What is confusing you about the words 'choose', 'integer' and 'between'")
            continue
            
        if guess != target:
            attempts += 1
            
            if guess > target:
                print("Your guess is too high")
            else:
                print("Your guess is too low")
                
        else:
            print("\nCorrect.  It took you this many attempts:- ", attempts)

print("\nAll done. Goodbye and have a pleasant diurnal period.")
