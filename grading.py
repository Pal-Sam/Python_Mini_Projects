student_score={
    "Palguni":99,
    "Hermoine":85,
    "Jack":60,
    "Jill": 90,
    "Megan":10
}
student_grade={}

for i in student_score:
    if student_score[i]>89:
        student_grade[i]='A'
    elif student_score[i]>70:
        student_grade[i]='B'
    elif student_score[i]>50:
        student_grade[i]='C' 
    else:
        student_grade[i]='F'

print(student_grade)
