positive_feedback = ["smart", "brilliant", "studious"]
negative_feedback = ["not"]
report = ["this student is studious", "the student is smart","the student is not smart"]
# student_id = [1, 2]
student_points = {}
for j in range(len(report)):
    student = j+1
    student_points.setdefault(student, 0)
    if negative_feedback[0] in report[j]:
        student_points[student] =1
       
    else:
        for k in positive_feedback:
            if k in report[j]:
              
                student_points[student] =3
                
print(student_points)
print(list(student_points.keys()))