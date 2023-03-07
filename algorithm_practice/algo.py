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

print(sort_num([1,2,3,10,5]))
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

print(my_friends(["Ryan", "Kieran", "Jason", "Yous"]))




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

print(round_to_fives(0))
print(round_to_fives(2))
print(round_to_fives(3))
print(round_to_fives(12))
print(round_to_fives(21))
print(round_to_fives(30))
print(round_to_fives(-2))
print(round_to_fives(-5))