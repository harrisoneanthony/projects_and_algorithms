'''Build a function that will take the length of each side of a triangle and return if it's either an Equilateral, an Isosceles, a Scalene or an invalid triangle.

equilateral -> a=b=c

isoceles -> perimeter 2l + b
        area 1/2bh

scalene -> a != b != c

invalid

It has to return a string with the type of triangle.
For example:

type_of_triangle(2, 2, 1) --> "Isosceles"'''
import math

def type_of_triangle(a, b, c):
    if not isinstance(a,int) or not isinstance(b,int) or not isinstance(c,int):
        return "Not a valid triangle"
    if a + b <= c or a + c <= b or b + c <=a:
        return "Not a valid triangle"
    if a == b & b == c:
        return "Equilateral"
    elif a==b or b==c or a==c:
        return "Isosceles"
    else:
        return "Scalene"

print(type_of_triangle(1,1,1))
print(type_of_triangle(3,2,4))
print(type_of_triangle(2,2,1))
print(type_of_triangle('.',5,82))
