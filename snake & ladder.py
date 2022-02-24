from ast import Break
import random

ladder={2:23,8:34,20:77,32:68,41:79,74:88,82:100,85:95}
snake={29:9,38:15,47:5,53:33,62:37,86:54,92:70,97:25}

player1=0
player2=0

def step(player):
    Dice=random.randint(1,6)
    player=player+Dice
    if player in snake():
        print("opps")
        player=snake(player)
    elif player in ladder():
        print("Wow")
        player=ladder(player)
    else:
        print(player)

while True:
    A=input("First Player \"A\" To throw a dice") 
    player1=step(player1)
    if player1>=100:
        print("Player 1 wins")
        Break
    B=input("Second Player \"B\" To throw a dice")
    player2=step(player2)
    if player2>=100:
        print("Player 2 wins")
        Break
        

