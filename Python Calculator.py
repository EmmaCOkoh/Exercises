# Python calculator

operator = input("Enter an operator ( + - * /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


if operator == "+":
    print(f"The sum is: {num1 + num2}")
elif operator == "-":
    print(f"The subtraction is : {num1 - num2}")
elif operator == "*":
    print(f"The multiplication is : {round(num1 * num2, 2)}")
elif operator == "/":
    print(f"The division is : {round(num1 / num2, 3)}")
else:
    print(f"{operator} is not a valid operator")