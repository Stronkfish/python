import random # Random Gen Plugin (1)
att = 0 # Attempts Taken (2)
num1 = int(input("Stronkfish Brand Guess the Number Game\n\nMinimum Number: ")) # Spec (3-5)
num2 = int(input("Maximum Number: "))
attw = int(input("Number of Attempts Allowed: "))
num = random.randint(num1, num2) # Gen (6)
print(f"I am thinking of a number between {num1} and {num2}. You have {attw} Attempts to Guess it.") # Number Range, Attempt Count Confirmation (7)
while att < attw: # Number Guessing (8-16)
    guess = int(input("\nGuess the number: "))
    att += 1
    if guess < num:
        print(f"\nToo Low!\nAttempts Remaining: {attw - att}")
    if guess > num:
        print(f"\nToo High!\nAttempts Remaining: {attw - att}")
    if guess == num:
        break
if guess == num: # Correct Answer, Total Attempts used (17-18)
    print(f"\nCorrect!\nTotal Attempts: {att}")
if guess != num: # Incorrect Answer, ran out of Attempts (19-20)
    print(f"\nZero Attempts Remaining!\nThe Number I was thinking of is {num}")
