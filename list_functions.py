#List

#input:
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

#output
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]


if __name__=='__main__':
    n=int(input("Enter the number of commands you have to perform:"))
    l1=[]
    for i in range(n):
        cmd=input().split()
        if cmd[0]=='insert':
            l1.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0]=='print':
            print(l1)
        elif cmd[0]=='remove':
            l1.remove(int(cmd[1]))
        elif cmd[0]=='append':
            l1.append(int(cmd[1]))
        elif cmd[0]=='sort':
            l1.sort()
        elif cmd[0]=='pop':
            l1.pop()
        elif cmd[0]=='reverse':
            l1.reverse()