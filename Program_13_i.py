#PATTERN 1
rows = 4
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)