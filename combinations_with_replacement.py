# This tool returns r length subsequences of elements from the input iterable allowing individual 
# elements to be repeated more than once.

# Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the 
# combination tuples will be produced in sorted order.

# Task

# You are given a string S.
# Your task is to print all possible size K replacement combinations of the string in lexicographic sorted order.

from itertools import combinations_with_replacement

s,k=input().split()
for i in list(combinations_with_replacement(sorted(s),int(k))):
    print(''.join(i))