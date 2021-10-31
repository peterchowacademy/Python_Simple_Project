# import modules
#
# print(modules.roll_dice(10))

from student import Student

student1 = Student("Peter", "Finance", 4.0, False)
student2  = Student("Pam", "Chemistry", 3.0, True)
print(student1.name)
# run the class function:
print(student2.on_honor_roll())