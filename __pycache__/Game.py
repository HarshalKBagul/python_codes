
#Problem Statement
#Nutan and Tusla are both students at Newton School. They are both among the best students in the class. In order to know who is better among them, a game was organised. The game consisted of L rounds, where L is an odd integer. The student winning more rounds than the other was declared the winner.

#You would be given a string of odd length L in which each character is 'N' or 'T'. If the ith character is 'N', then the ith round was won by Nutan, else if the character is 'T' it was won by Tusla. Print "Nutan'' if Nutan has won more rounds than Tusla, else print "Tusla'' if Tusla has won more rounds than Nutan.

#Note: You have to print everything without quotes.
#Input
#The first line of the input contains a single integer L — the number of rounds (1 ≤ L ≤ 100 and L is odd).
#The second line contains a string S of length L. Each character of S is either 'N' or 'T'.
#Output
#Print "Nutan" or "Tusla" according to the input.
#Example
# Sample Input:
# 3
# NNT

# Sample Output:
# Nutan

# Explanation:
# Nutan has won two games while Tusla has only won a single game, so the overall winner is Nutan.

l=int(input())
S=input()
n=0
t=0

for i in S:
    if i=='N':
        n=n+1
    else:
        t=t+1

if n>t:
    print("Nutan")
else:
    print("Tusla")