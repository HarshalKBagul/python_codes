# The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in 
# combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly 
# and efficiently in pure Python


from itertools import combinations

n=input()
s=list(input().split(' '))
k=int(input())
c=0

for i in combinations(s,k):
    if 'a' in i:
        c=c+1
        
print(c/len(list(combinations(s,k))))