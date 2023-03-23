'''Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).'''

def is_triangle(a,b,c):
    return a+b> c and a+c>b and b+c>a

def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c

print(is_triangle(1,2,2))
print(is_triangle(7,2,2))
print(is_triangle(1,2,3))
print(is_triangle(5,1,2))
