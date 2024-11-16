grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

aeron_=grades[0]
bilbo_=grades[1]
johnny_=grades[2]
khendric_=grades[3]
steve_=grades[4]
aeron_=sum(aeron_)/len(aeron_)
bilbo_=sum(bilbo_)/len(bilbo_)
khendric_=sum(khendric_)/len(khendric_)
johnny_=sum(johnny_)/len(johnny_)
steve_=sum(steve_)/len(steve_)
students_=students
list_students_ = list(students_)
list_students_.sort()
list_grades_=[aeron_,bilbo_,johnny_,khendric_,steve_]
list_grades_list_students_ = {obj : state for obj,state in zip(list_students_,list_grades_)}
print(list_grades_list_students_)









