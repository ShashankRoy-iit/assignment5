student = {'Alice':95,'Mohan':99,'Sohan':98,'Ram':92}
a = input("Enter the student's name: ")

if a in student:
    print(a,"'s marks: ",student.get(a))
else:
    print("Student not found.")