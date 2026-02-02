# Print the grade sheet of a student for the given range of cgpa. Scan marks of five 
# subjects and calculate the percentage. 
# CGPA=percentage/10 
# CGPA range: 
# 0 to 3.4 -> F 
# 3.5 to 5.0->C+ 
# 5.1 to 6->B 
# 6.1 to 7-> B+ 
# 7.1 to 8-> A 
# 8.1 to 9->A+ 
 
# 9.1 to 10-> O (Outstanding) 
# Sample Gradesheet 
# Name: Rohit Sharma 
# Roll Number: R17234512   SAPID: 50005673 
# Sem: 1      Course: B.Tech. CSE AI&ML 
 
# Subject name: Marks 
# PDS:   70 
# Python:  80 
# Chemistry:  90 
# English:  60 
# Physics:  50 
# Percentage: 70% 
# CGPA:7.0 
# Grade: 

name=input("Enter Student name: ")
roll_no=input("Enter Student Roll number: ")
sap_id=int(input("Enter Student's SAPID: "))
sem=int(input("Enter Semester: "))
Course=input("Enter Course: ")
m1=float(input("Enter marks of PDS: "))
m2=float(input("Enter marks of Python: "))
m3=float(input("Enter marks of Chemistry: "))
m4=float(input("Enter marks of English: "))
m5=float(input("Enter marks of Physics: "))
percentage=((m1+m2+m3+m4+m5)/500)*100
cgpa=percentage/10
if cgpa>=9.1 and cgpa<=10:
    grade= "O"
elif cgpa>=8.1 and cgpa<=9.0:
    grade= "A+"
elif cgpa>=7.1 and cgpa<=8.0:
    grade= "A"
elif cgpa>=6.1 and cgpa<=7.0:
    grade= "B+"
elif cgpa>=5.1 and cgpa<=6.0:
    grade= "B"
elif cgpa>=3.5 and cgpa<=5.0:
    grade= "C+"
elif cgpa>=0 and cgpa<=3.4:
    grade= "F"
print("\n..........................GradeSheet..........................")
print('Name: ',name)
print("Roll Number: ",roll_no,"           SAPID: ",sap_id)
print("Sem: ",sem,"            Course: ",Course)
print("Subject name:   Marks:")
print("PDS:            ",m1)
print("Python:         ",m2)
print("Chemistry:      ",m2)
print("English:        ",m2)
print("Physics:        ",m2)
print("Percentage: ",percentage)
print("CGPA: ",cgpa)
print("Grade: ",grade)
