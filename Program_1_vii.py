print("-------FLOOR DIVISION--------")
a = int(input(" Enter first number : "))
b = int(input(" Enter second number : "))
while(b==0):
    print("Division by zero not allowed")
    b = int(input(" Enter second number : "))

c = a // b
print("Quotient = ",c)