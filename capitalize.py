#Capitalize
#You are asked to ensure that the first and last names of
#people begin with a capital letter in their passports. 
#For example, alison heck should be capitalised correctly as Alison Heck.

import string

def solve(s):
    l=s.split(" ")
    s=''
    for i in l:
        s=s+i.capitalize()+' '
    return s
