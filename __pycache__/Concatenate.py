#Concatenate

#Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:

#Task

#You are given two integer arrays of size NXP and MXP (N &M  are rows, and P is the column). 
#Your task is to concatenate the arrays along axis 0.

import numpy

N,M,P=map(int,input().split())
P1=[]
P2=[]
for i in range(N):
    a=list(map(int,input().split()))
    P1.append(a)
for j in range(M):
    b=list(map(int,input().split()))
    P2.append(b)

print(numpy.concatenate((P1,P2),axis=0))