# Find the Runner-up Score

#Given the participants' score sheet for your University Sports Day, 
#you are required to find the runner-up score. You are given  scores.
#Store them in a list and find the score of the runner-up.

if __name__=='__main__':
    n=int(input("Enter The number of input:"))
    l1=input("Enter all Scores:").split()
    l2=list(l1)
    s=set(l2)
    l3=list(s)
    l3.sort()
    print(l3[-2])
