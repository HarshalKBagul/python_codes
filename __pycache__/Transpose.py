#You are given a NXM integer array matrix with space separated elements (N = rows and  M= columns).
#Your task is to print the transpose and flatten results.

import numpy as np

n,m=map(int,input().split())
list1=[]
for i in range(n):
    a=list(map(int,input().split()))
    list1.append(a)
arr=np.array(list1)
print(np.transpose(arr))
print(arr.flatten())
