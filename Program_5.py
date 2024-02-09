#SCORE GRADING
score = int(input("Enter the score : "))
if score>100:
    print("Invalid Score!")
else:
    if score>=90:
        print("Grade is A+")
    elif score>=80:
        print("Grade is A")
    elif score>=70:
        print("Grade is B+")
    elif score>=60:
        print("Grade is B")
    elif score>=50:
        print("Grade is C+")
    else:
        print("FAILED!!")
