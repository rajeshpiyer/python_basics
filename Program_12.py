#FIBONACCI SERIES FOR LOOP
a = 0
b = 1
print(a)
print(b)
for i in range(1, 6):
    c=a+b
    a=b
    b=c
    print(c)
