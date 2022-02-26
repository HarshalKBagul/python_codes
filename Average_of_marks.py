# finding the average of marks

#The provided code stub will read in a dictionary 
# containing key/value pairs of name:[marks] for a 
# list of students. Print the average of the marks 
# array for the student name provided, showing 2 
# places after the decimal.

if __name__=='__main__':
    n=int(input("Enter the number of inputs you have to give:"))
    student_marks={}
    for _ in range(n):
        name,*line=input().split()
        score=list(map(float,line))
        student_marks[name]=score
    averge_marks=input("Enter the name of student whoes Averge marks you want:")
    s=0
    for i in student_marks.get(averge_marks):
        s=s+i
    print("{0:.2f}".format(s/3))