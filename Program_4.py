#EVEN OR ODD
try:
    num = int(input("Enter a Number : "))
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
except ValueError:
    print("Invalid input")