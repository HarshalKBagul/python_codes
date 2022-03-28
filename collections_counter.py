#Collections.Counter()
#A counter is a container that stores elements as dictionary keys, 
#and their counts are stored as dictionary values.

n=int(input())
stock=list(map(int,input().split(' ')))

#print(stock)
from collections import Counter
Dict=Counter(stock)
x=int(input())
p=0
# print(Dict)
for i in range(x):
    size,price=map(int,input().split(' '))
    if Dict[size]:
        Dict[size]=Dict[size]-1
        p=p+price
print(p)