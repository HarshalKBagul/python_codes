#If we want to add a single element to an existing set, we can use the .add() 
#operation.
#It adds the element to the set and returns 'None'.

#Rupal has a huge collection of country stamps. She decided to count the 
#total number of distinct country stamps in her collection. She asked for 
#your help. You pick the stamps one by one from a stack of N country stamps.

#Find the total number of distinct country stamps

n=int(input())
c=[]
for i in range(n):
    x=input()
    c.append(x)
print(c)
s=set(c)
print(len(list(s)))
# c1=list(s)
# print(len(c1))