# Check whether the quadratic equation has real roots or imaginary roots. Display the roots. 
import math
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))

D=b**2 - 4*a*c

if D>0:
    root1=(-b+math.sqrt(D))/(2*a)
    root2=(-b-math.sqrt(D))/(2*a)
    print("Both Roots are real.")
    print("Roots: ",root1,",",root2)
elif D==0:
    root=-b/(2*a)
    print("Both Roots are real and Equal.")
    print("Roots: ",root,",",root)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-D) / (2*a)
    print("The equation has imaginary roots:")
    print("Root 1:", real_part, "+", imaginary_part, "i")
    print("Root 2:", real_part, "-", imaginary_part, "i")
    