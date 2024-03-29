'''
Simple Fun #183: Direction In Grid

DESCRIPTION:
Task
You're standing at the top left corner of an n x m grid and facing towards the right.

Then you start walking one square at a time in the direction you are facing.

If you reach the border of the grid or if the next square you are about to visit has already been visited, you turn right.

You stop when all the squares in the grid are visited. What direction will you be facing when you stop?

You can see the example of your long walk in the image below. The numbers denote the order in which you visit the cells.



Given two integers n and m, denoting the number of rows and columns respectively, find out the direction you will be facing at the end.

Output "L" for left, "R" for right, "U" for up, and "D" for down.

Example:
For n = 3, m = 3, the output should be "R".

This example refers to the picture given in the description. At the end of your walk you will be standing in the middle of the grid facing right.

Input/Output
[input] integer n
number of rows.

1 <= n <= 1000

[input] integer m
number of columns.

1 <= m <= 1000

[output] a string
The final direction.'''

def direction_in_grid(rows,cols):
    if rows == cols:
        if rows % 2 != 0:
            return "R"
        else:
            return "L"
    if rows > cols:
        if cols % 2 == 0:
            return"U"
        else:
            return "D"
    else:
        if rows % 2 == 0:
            return "L"
        else:
            return "R"
        

print(direction_in_grid(1,1))
print(direction_in_grid(2,2))
print(direction_in_grid(2,3))
print(direction_in_grid(2,4))
print(direction_in_grid(3,1))
print(direction_in_grid(3,2))
print(direction_in_grid(3,3))
print(direction_in_grid(3,4))
print(direction_in_grid(3,5))

'''def direction_in_grid(n, m):
    return "LR"[n%2] if m >= n else "UD"[m%2]'''

'''The function first checks if the value of m is greater than or equal to n. If it is, the direction of movement is horizontal, and the function returns the character "L" or "R" based on whether n is even or odd. Specifically, it returns "L" if n is even, and "R" if n is odd. This is achieved by using the modulo operator % to determine the remainder when n is divided by 2, and then indexing the string "LR" with the result.

If m is less than n, the direction of movement is vertical, and the function returns the character "U" or "D" based on whether m is even or odd. This is achieved in a similar way to the horizontal case, by indexing the string "UD" with the result of m modulo 2. Specifically, it returns "U" if m is even, and "D" if m is odd.'''