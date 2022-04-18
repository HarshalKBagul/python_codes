#rock paper scissors

import random
from secrets import choice

choice=["rock","paper","scissor"]

computer=random.choice(choice)
player=None

while player not in choice:
    player=input("rock , paper , scissor: ?").lower()


if player==computer:
    print("player:",player)
    print("computer:",computer)
    print("Tie")

elif player=="rock":
    if computer=="paper":
        print("player:",player)
        print("computer:",computer)
        print("You Lose")
    if computer=="scissor":
        print("player:",player)
        print("computer:",computer)
        print("You Win")

elif player=="paper":
    if computer=="scissor":
        print("player:",player)
        print("computer:",computer)
        print("You Lose")
    if computer=="rock":
        print("player:",player)
        print("computer:",computer)
        print("You Win")

elif player=="scissor":
    if computer=="paper":
        print("player:",player)
        print("computer:",computer)
        print("You Win")
    if computer=="rock":
        print("player:",player)
        print("computer:",computer)
        print("You Lose")