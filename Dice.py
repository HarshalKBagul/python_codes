import random
from secrets import choice
from tkinter import N

def dice(first,last):
    while True:
        print("dice are rolling....")
        number=random.randint(first,last)
        print("The Dice making by Harshal Bagul is Showing number")
        print(f"The Number is : {number}")
        choice=input("Do you want to Roll agian ? (y/n)")
        if choice.lower()=='n':
            break

dice(1,6)