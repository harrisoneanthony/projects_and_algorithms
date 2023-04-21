nums = [1, 2, 5, 8, 3, 0, 7]
res = list(filter(lambda x: x<5, nums))
# print(res)

def fib(x):
    if x == 0 or x == 1:
        return 1
    else: 
        return fib(x-1) + fib(x-2)
# print(fib(4))

def my_func(x, y=7, *args, **kwargs):
    print(kwargs)

# my_func(2, 3, 4, 5, 6, a=7, b=8)

nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
# print(len(list(nums)))

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)
		
# print(power(2, 3))

a = (lambda x: x*(x+1))(6)
# print(a



nums = [1, 2, 8, 3, 7]
res = list(filter(lambda x: x%2==0, nums))
# print(res)

def func(**kwargs):
    print(kwargs["zero"])

# func(a = 0, zero = 8)

class A:
    def method(self):
        print(1)

class B(A):
    def method(self):
        print(2)

B().method()

#magic methods
'''
__sub__ for -

__mul__ for *

__truediv__ for /

__floordiv__ for //

__mod__ for %

__pow__ for **

__and__ for &

__xor__ for ^

__or__ for |
'''