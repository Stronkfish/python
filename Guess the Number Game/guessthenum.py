# Random Integer Plugin.
import random

# Attempts Taken.
att = 0

# Minimum Number for the Game.
minimum = int(input("Stronkfish Brand Guess the Number Game\n\nMinimum Number: ")) 

# Maximum Number for the Game.
maximum = int(input("Maximum Number: "))

# Number of Attempts Allowed for the Game.
att_allowed = int(input("Number of Attempts Allowed: "))

# Generates the Number to Guess, within the Minimum and Maximum Number.
num = random.randint(minimum, maximum)

# Provides the Details for the Game - Minimum Number, Maximum Number, Attempts Allowed.
print(f"I am thinking of a number between {minimum} and {maximum}. You have {att_allowed} Attempts to Guess it.")

# Starts the Game. While the attempts counter is below the allowed attempts, the Game will continue until the Number is Guessed.
while att < att_allowed:
    
    # User Input to Guess the Number.
    guess = int(input("\nGuess the number: "))
    
    # Adding to the Attempt Counter for each Guess.
    att += 1
    
    # The Guess is too Low, displays total Attempts Remaining.
    if guess < num:
        print(f"\nToo Low!\nAttempts Remaining: {att_allowed - att}")
        
    # The Guess is too High, displays total Attempts Remaining.
    if guess > num:
        print(f"\nToo High!\nAttempts Remaining: {att_allowed - att}")
        
    # The Guess is Correct, breaks the Guess Loop.
    if guess == num:
        break
        
# Guessed the Number with the Total Attempts taken.
if guess == num:
    print(f"\nCorrect!\nTotal Attempts: {att}")
    
# Failed to Guess the Number, Zero Attempts Remaining, and the Correct Number.
if guess != num:
    print(f"\nZero Attempts Remaining!\nThe Number I was thinking of is {num}")
