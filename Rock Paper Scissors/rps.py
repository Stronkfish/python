import random
progress = 0
rounds = int(input("\n\nRounds: "))
rps = ["rock", "paper", "scissors"]

pointsu = 0
pointsc = 0

while rounds > progress: 
    computer = random.choice(rps)
    progress += 1
    user = input("\n\nRock Paper or Scissors? ")

    if user.upper() == computer.upper():
        print(f"Both players selected {user.title()}. It's a tie!")

    elif user.upper() == "ROCK":
        if computer == "scissors":
            print("Rock smashes Scissors! You Win!")
            pointsu += 1
        else:
            print("Paper covers Rock! You Lose.")
            pointsc += 1

    elif user.upper() == "PAPER":
        if computer == "rock":
            print("Paper covers Rock! You Win!")
            pointsu += 1
        else:
            print("Scissors cuts Paper! You Lose.")
            pointsc += 1
    elif user.upper() == "SCISSORS":

        if computer == "paper":
            print("Scissors cuts Paper! You Win!")
            pointsu += 1
        else:
            print("Rock smashes Scissors! You Lose.")
            pointsc += 1
    else:
        break
if pointsu > pointsc:
    print(f"\n\nUser Score: {pointsu}\nComputer Score: {pointsc}\nYou Won Overall!\n")
if pointsu < pointsc:
    print(f"\n\nUser Score: {pointsu}\nComputer Score: {pointsc}\nYou Lost Overall.\n")
if pointsu == pointsc:
    print(f"\n\nUser Score: {pointsu}\nComputer Score: {pointsc}\nYou Tied Overall.\n")
