# Given a numereical test score bet. 0 to 100, print out the letter grade equivalent according to these rules:
# A 90-100
# B 80-89
# C 70-79
# U <70

score = int(input("Enter the test score: "))
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 0 <= score < 70:
    print("Grade: U")
else:
    print("Invalid score")

