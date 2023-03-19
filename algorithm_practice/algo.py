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

# print(your_order("is2 Thi1s T4est 3a"))
# print(your_order("4of Fo1r pe6ople g3ood th5e the2"))


# jumps in a cycle

def get_jumps(cycle_list, k):
    l = a = len(cycle_list)
    while a != k:
        if a > k:
            a = a - k
        else:
            k = k - a
    return l/k
# print(get_jumps([1,5,7,8,9], 1))
# print(get_jumps([1,5,7,8,9], 2))


# Kooka Counter
'''A family of kookaburras are in my backyard.

I can't see them all, but I can hear them!

How many kookaburras are there?

Hint
The trick to counting kookaburras is to listen carefully

The males sound like HaHaHa...

The females sound like hahaha...

And they always alternate male/female

Examples
ha = female => 1
Ha = male => 1
Haha = male + female => 2
haHa = female + male => 2
hahahahaha = female => 1
hahahahahaHaHaHa = female + male => 2
HaHaHahahaHaHa = male + female + male => 3'''

def kooka_counter(laughing):
    if not laughing:
        return 0
    count = 1
    last_h = laughing[0]
    for i in range(0,len(laughing),2):
        if last_h != laughing[i]:
            count +=1
            last_h = laughing[i]
    return count

# print(kooka_counter('ha'))
# print(kooka_counter('Ha'))
# print(kooka_counter('Haha'))
# print(kooka_counter('haHa'))
# print(kooka_counter('hahahaha'))
# print(kooka_counter('hahahahaHaHaHa'))
# print(kooka_counter('HaHaHaHaHaHa'))



# Cantor's Pairing function
'''Georg Cantor's in one of his proofs used following sequence:

1/1 1/2 1/3 1/4 1/5 ... 
2/1 2/2 2/3 2/4 ...
3/1 3/2 3/3 ... 
4/1 4/2 ... 
5/1 ... 
There are many ways to order those expressions. In this kata we'll use this approach:



So sequence is:

1/1, 1/2, 2/1, 3/1, 2/2, 1/3, 1/4 ...
Your task is to return nth element of this sequence.

Input: n - positive integer (max 268435455)

Output: string - nth expression of sequence - 'a/b' where a and b are integers.'''


def cantor(n : int) -> str:
    if n == 1:
        return '1/1'
    else:
        k = 1
        while n > k:
            n -= k
            k += 1
            print(n,k)
        if k % 2 == 0:
            return str(n) + '/' + str(k-n+1)
        else:
            return str(k-n+1) + '/' + str(n)

# print(cantor(1))
# print(cantor(2))
# print(cantor(3))
# print(cantor(4))
# print(cantor(5))
print(cantor(7))

