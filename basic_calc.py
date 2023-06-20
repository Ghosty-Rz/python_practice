# veeeery basic calculator

num1 = float(input("Enter a number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter another number: "))

if op == "+" :
    result = (num1) + (num2)
if op == "-" :
    result = (num1) - (num2)
if op == "/" :
    result = (num1) / (num2)
if op == "*" :
    result = num1 * num2

print("the result is : " + str(result))


