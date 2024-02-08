#Building a basic calculator

num1 = float(input("Enter the first number: "))
opera = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))

if opera == "+":
  print(num1 + num2)
elif opera == "-":
  print(num1 - num2)
elif opera == "*":
  print(num1 * num2)
elif opera == "/":
  print(num1 / num2)
else:
  print("invalid operator")
  