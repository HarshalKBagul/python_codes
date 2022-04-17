#Triangle Quest 

# You are given a positive integer N.
# Your task is to print a palindromic triangle of size N.

# For example, a palindromic triangle of size 5 is:

# You can't take more than two lines. The first line (a for-statement) 
# is already written for you.
# You have to complete the code using exactly one print statement.

for i in range(1,int(input())+1):
    print(((10**i-1)//9)**2)