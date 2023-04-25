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

# B().method()

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

'''
Python also provides magic methods for comparisons.

__lt__ for <

__le__ for <=

__eq__ for ==

__ne__ for !=

__gt__ for >

__ge__ for >=
'''

'''
There are several magic methods for making classes act like containers.

__len__ for len()

__getitem__ for indexing

__setitem__ for assigning to indexed values

__delitem__ for deleting indexed values

__iter__ for iteration over objects (e.g., in for loops)

__contains__ for in
'''

'''class Test:
    __egg = 7

    def get_egg(self):
        return Test.__egg

t = Test()
print(t.get_egg())

-OR-

class Test:
    __egg = 7

t = Test()
print(t._Test__egg)'''


'''
Exceptions 
Different exceptions are raised for different reasons. 

Common exceptions:

ImportError: an import fails;

IndexError: a list is indexed with an out-of-range number;

NameError: an unknown variable is used;

SyntaxError: the code can't be parsed properly; 

TypeError: a function is called on a value of an inappropriate type;

ValueError: a function is called on a value of the correct type, but with an inappropriate value.'''