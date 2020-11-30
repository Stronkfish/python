import random
att = 0
num1 = int(input("Stronkfish Brand Guess the Number Game\n\nMinimum Number: "))
num2 = int(input("Maximum Number: "))
attw = int(input("Number of Attempts Allowed: "))
num = random.randint(num1, num2)
print(f"I am thinking of a number between {num1} and {num2}. You have {attw} Attempts to Guess it.")
while att < attw:
    guess = int(input("\nGuess the number: "))
    att = att + 1
    if guess < num:
        print(f"\nToo Low!\nAttempts Remaining: {attw - att}")
    if guess > num:
        print(f"\nToo High!\nAttempts Remaining: {attw - att}")
    if guess == num:
        break
if guess == num:
    print(f"\nCorrect!\nTotal Attempts: {att}")
if guess != num:
    print(f"\nZero Attempts Remaining!\nThe Number I was thinking of is {num}")
