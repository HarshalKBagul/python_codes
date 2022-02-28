# You are given a string and your task is to swap cases. In other words, 
# convert all lowercase letters to uppercase letters and vice versa.

# input:HackerRank.com presents "Pythonist 2".
# output:hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(s):
    x=""
    for c in s:
        if c.isupper():
            c=c.lower()
        else:
            c=c.upper()
        x+="".join(c)
    return x
