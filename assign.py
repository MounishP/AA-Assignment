"""
find the roots of the eq'n ->      ax^2+bx+c=0
take inputs for a,b,c
find roots
categorise the roots -> real, imaginary
"""
import math

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
if a != 0:
    if (b**2 - 4 * a * c) >= 0:
        print("roots are real")
        x1 = (-b + math.sqrt(b * b - 4 * a * c))/(2*a)
        x2 = -b - math.sqrt(b * b - 4 * a * c)/(2*a)
        print("roots are:", x1, x2)
    else:
        print("roots are imaginary")
else:
    print("a can't be 0")