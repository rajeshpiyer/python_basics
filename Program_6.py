#ODD OR EVEN IN A RANGE
a = int(input("Enter the lower limit : "))
b = int(input("Enter the upper limit : "))
choice = int(input("Choose a sequence : 1 for Odd : 2 for Even : "))
if a<b:
    if a%2==0:
        if choice == 1:
            a+=1
        while(a<=b):
            print(a)
            a+=2
    else:
        if choice == 2:
            a+=1
        while(a<b):
            print(a)
            a+=2
else:
    print("Invalid Range")