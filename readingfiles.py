# read the file
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
#print(employee_file.readlines()[1])
#append the file - a
# employee_file = open("employees.txt", "a")
employee_file.close()
