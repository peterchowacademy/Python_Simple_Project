num1 = float(input("Enter your first number: "))
op = input("Enter operator")
num2 = float(input("Enter your first number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid operator")