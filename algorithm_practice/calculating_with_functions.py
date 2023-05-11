'''This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
'''
import math

def zero(op=None):
    if op is None:
        return 0
    else:
        return op(0)

def one(op=None):
    if op is None:
        return 1
    else:
        return op(1)

def two(op=None):
    if op is None:
        return 2
    else:
        return op(2)

def three(op=None):
    if op is None:
        return 3
    else:
        return op(3)

def four(op=None):
    if op is None:
        return 4
    else:
        return op(4)

def five(op=None):
    if op is None:
        return 5
    else:
        return op(5)

def six(op=None):
    if op is None:
        return 6
    else:
        return op(6)

def seven(op=None):
    if op is None:
        return 7
    else:
        return op(7)

def eight(op=None):
    if op is None:
        return 8
    else:
        return op(8)

def nine(op=None):
    if op is None:
        return 9
    else:
        return op(9)

def plus(num):
    def inner(x):
        return x + num
    return inner

def minus(num):
    def inner(x):
        return x - num
    return inner

def times(num):
    def inner(x):
        return x * num
    return inner

def divided_by(num):
    def inner(x):
        return x // num
    return inner


def plus(num): 
    return lambda x: x + num
    #your code here
def minus(num): 
    return lambda x: x - num
    #your code here
def times(num): 
    return lambda x: x * num
    #your code here
def divided_by(num): 
    return lambda x: math.floor(x / num)
    #your code here