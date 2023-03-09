# Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

# For example:

def sort_num(nums):
    if nums == None:
        return []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

# print(sort_num([1,2,3,10,5]))
# sort_num([1,2,3,10,5]) # should return [1,2,3,5,10]
# sort_num(None) # should return []



# Make a program that filters a list of strings and returns a list with only your friends name in it.

# # If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

# i.e.

# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# Note: keep the original order of the names in the output.

def my_friends(input):
    friends_list=[]
    for i in input:
        if len(i) == 4:
            friends_list.append(i)
    return friends_list

# print(my_friends(["Ryan", "Kieran", "Jason", "Yous"]))




'''Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?

Examples:

input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.
Input may be any positive or negative integer (including 0).

You can assume that all inputs are valid integers.'''
import math

def round_to_fives(input):
    if input % 5 == 0:
        return input
    multiple = input/5
    return 5 * (math.ceil(multiple))

# def round_to_fives(input):
    # return input + (5 - input) % 5

# print(round_to_fives(0))
# print(round_to_fives(2))
# print(round_to_fives(3))
# print(round_to_fives(12))
# print(round_to_fives(21))
# print(round_to_fives(30))
# print(round_to_fives(-2))
# print(round_to_fives(-5))

'''In some scripting languages like PHP, there exists a logical operator (e.g. &&, ||, and, or, etc.) called the "Exclusive Or" (hence the name of this Kata). The exclusive or evaluates two booleans. It then returns true if exactly one of the two expressions are true, false otherwise. For example:

false xor false == false // since both are false
true xor false == true // exactly one of the two expressions are true
false xor true == true // exactly one of the two expressions are true
true xor true == false // Both are true.  "xor" only returns true if EXACTLY one of the two expressions evaluate to true.
Task
Since we cannot define keywords in Javascript (well, at least I don't know how to do it), your task is to define a function xor(a, b) where a and b are the two expressions to be evaluated. Your xor function should have the behaviour described above, returning true if exactly one of the two expressions evaluate to true, false otherwise.'''

def xor(a,b):
    return a != b

# print(xor(True, True))
# print(xor(False, True))
# print(xor(True, False))
# print(xor(False, False))



'''Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.
a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.
The four operators are "add", "subtract", "divide", "multiply".
A few examples:(Input1, Input2, Input3 --> Output)

5, 2, "add"      --> 7
5, 2, "subtract" --> 3
5, 2, "multiply" --> 10
5, 2, "divide"   --> 2.5'''

def arithmetic_operator(a,b,operator):
    if operator == "add":
        return a+b
    if operator == "subtract":
        return a-b
    if operator == "multiply":
        return a*b
    if operator == "divide":
        return a/b

def arithmetic_operator(a, b, operator):
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }[operator]

# print(arithmetic_operator(5,2,"add"))
# print(arithmetic_operator(5,2,"subtract"))
# print(arithmetic_operator(5,2,"multiply"))
# print(arithmetic_operator(5,2,"divide"))



# '''Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health. Health can't be less than 0.'''

def combat(health, damage):
    if health - damage < 0:
        return 0
    else:
        return health-damage
    
def combat(health, damage):
    return max(0, health-damage)

# print(combat(100, 5))
# print(combat(83, 16))
# print(combat(20, 30))



'''Unique in order:
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]'''


def unique_in_order(sequence):
    if not sequence:
        return []
    result =[sequence[0]]
    prev=sequence[0]
    for i in range(len(sequence)):
        if sequence[i] != prev:
            result.append(sequence[i])
        prev = sequence[i]
    return result
# print(unique_in_order('AAAABBBCCDAABBB'))
# print(unique_in_order('ABBCcAD'))
# print(unique_in_order([1,2,2,3,3]))



""" Your order, please

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"""

def your_order(input):
    sentence= input.split()
    result=[''] * len(sentence)
    for i in sentence:
        for x in i:
            try:
                a = int(x)
                result[a-1]=i
            except ValueError:
                pass
    return " ".join(result)

print(your_order("is2 Thi1s T4est 3a"))
print(your_order("4of Fo1r pe6ople g3ood th5e the2"))