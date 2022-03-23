# The Minion Game

str=input()
kevin=0
stuart=0

for i in range(len(str)):
    if str[i]=='A' or str[i]=='E' or str[i]=='I' or str[i]=='O' or str[i]=='U':
        kevin=kevin+len(str)-i
    else:
        stuart=stuart+len(str)-i
            
if kevin==stuart:
    print("Draw")
elif kevin>stuart:
    print('kevin{}'.format(kevin))
else:
    print('stuart {}'.format(stuart))
        