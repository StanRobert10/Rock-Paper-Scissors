import random
from ArtWork import rock, paper, scissors
choice = [rock, paper, scissors]

player_chose = int(input("What do you want to chose? 1(Rock), 2(Paper), 3(Scissors) "))
computer_chose = random.randint(0, 2)
player_chose -= 1

print(f"You chose:\n{choice[player_chose]}")
print(f"The Computer chose:\n{choice[computer_chose]}")

if player_chose == computer_chose:
    print("Is Draw!")

if player_chose == 0 and computer_chose == 1:
    print("The Computer Won!")
if player_chose == 0 and computer_chose == 2:
    print("You Won!")
if player_chose == 1 and computer_chose == 0:
    print("You Won!")
if player_chose == 1 and computer_chose == 2:
    print("The Computer Won!")
if player_chose == 2 and computer_chose == 0:
    print("The Computer Won!")
if player_chose == 2 and computer_chose == 1:
    print("You Won!")
