#FIBONACCI SERIES WHILE LOOP
a = 0
b = 1
print(a)
print(b)
c=0
while(c<8):
    c=a+b
    a=b
    b=c
    print(c)