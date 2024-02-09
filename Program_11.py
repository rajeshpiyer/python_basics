#SUM OF ODD NUMBERS
a = int(input("Enter the lower limit : "))
b = int(input("Enter the upper limit : "))
if a%2 == 0:
    a+=1
sum=0
while(a<=b):
    sum+=a
    a+=2
print("Sum of Odd Numbers is : ",sum)