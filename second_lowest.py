# second lowest # Nested list

#Given the names and grades for each student in a class of N
#students, store them in a nested list and print the name(s) of any
#student(s) having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, 
# order their names alphabetically and print each name on a new line.

if __name__=='__main__':
    dict={}
    for i in range(int(input())):
        name=input()
        score=float(input())
        dict[name]=score

    v=dict.values()
    second=(sorted(list(set(v)))[1])
    second_lowest=[]
    for key,value in dict.items():
        if (value==second):
            second_lowest.append(key)
    second_lowest.sort()
    for name in second_lowest:
        print(name)
