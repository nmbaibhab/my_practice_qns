from student_class import student

student1=student("sipu",5,36)
print(student1.name)

#overwriting details
student1.name=input()
student1.std=5
student1.roll=30
print(student1.name)
print(student1.section())