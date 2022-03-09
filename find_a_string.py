# Find a string

#In this challenge, the user enters a string and a substring. You have to print the number 
#of times that the substring occurs in the given string. String traversal will take place from 
#left to right, not from right to left.

string=input()
sub_string=input()
ml=len(string)
sl=len(sub_string)
c=0
for i in range(ml-sl+1):
    if string[i:i+sl]==sub_string:
        c=c+1
print(c)