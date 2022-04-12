#word order

# Task:
# You are given n words. Some words may repeat. For each word, output its number of occurrences. 
# The output order should correspond with the input order of appearance of the word. See the 
# sample input/output for clarification.

# Note: Each input line ends with a "\n" character.
    
# input:
# The first line contains the integer,n .
# The next n lines each contain a word. 

# output:
# Output 2 lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct 
# word according to their appearance in the input

from collections import Counter

n=int(input())
l1=[]

for _ in range(n):
    l1.append(input())

x=Counter(l1)
print(len(x))
print(*x.values())