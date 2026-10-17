# a =lambda a,b:a*b
# print(a(5,3))

students=[("peter", 200),("john", 25),("james", 30)]
                                       
sorted_students=sorted(students,key=lambda x:x[1])
print(sorted_students)