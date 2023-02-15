'''Arrays To Do 1'''


'''Shuffle
In JavaScript, the Array object has numerous useful methods. It does not, however, contain a method that will randomize the order of an array’s elements. Let’s create shuffle(arr), to efficiently shuffle a given array’s values. Work in-place, naturally. Do you need to return anything from your function?'''
import random

def shuffle(lst):
    new_lst = []
    for i in range(len(lst)):
        rand_index = random.randint(0, len(lst)-1)
        new_lst.append(lst[rand_index])
        lst.pop(rand_index)
    return new_lst
# print(shuffle([1,2,3,4,5]))


'''Skyline Heights
Lovely Burbank has a breathtaking view of the Los Angeles skyline. Let’s say you are given an array with heights of consecutive buildings, starting closest to you and extending away. Array [-1,7,3] would represent three buildings: first is actually out of view below street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level. Return array containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in array functions such as unshift().'''

def skyline(input):
    visible = []
    prev_height = -1
    for i in input:
        if i > prev_height:
            visible.append(i)
        prev_height = i
    return visible

# print(skyline([-1,1,1,7,3]))
# print(skyline([0,4]))

'''Zip It
Create a standalone function that accepts two arrays and combines their values sequentially into a new array. Extra values from either array should be included afterward. Given [4,15,100] and [10,20,30,40], return new array containing [4,10,15,20,30,40,100].'''
def zip_it(arr_1, arr_2):
    arr_3=[]
    for i in arr_1:
        arr_3.append(i)
    for i in arr_2:
        arr_3.append(i)
    results = sorted(arr_3)
    return results
    

# print(zip_it([4,15,100],[10,20,30,40]))

'''Credit Card Validation (Bonus)
The Luhn formula is sometimes used to validate credit card numbers. Create the function isCreditCardValid(digitArr) that accepts an array of digits on the card (13-19 depending on the card), and returns a boolean whether the card digits satisfy the Luhn formula, as follows:

Set aside the last digit; do not include it in these calculations (until step 5);
Starting from the back, multiply the digits in odd positions (last, third-to-last, etc.) by 2;
If any results are larger than 9, subtract 9 from them;
Add all numbers (not just our odds) together;
Now add the last digit back in the sum should be a multiple of 10.
For example, when given digit array [5,2,2,8,2], after step 1) it becomes [5,2,2,8], then after step 2) it is [5,4,2,16]. Post-3) we have [5,4,2,7], then following 4) it becomes 18. After step 5) our value is 20, so ultimately we return true. If the final digit were any non-multiple-of-10, we would instead return false.'''

def isCreditCardValid(digitArr):
    last_digit = digitArr.pop()
    reversed_digits = digitArr[::-1]
    for i in range(0,len(reversed_digits),2):
        if reversed_digits[i]*2 > 9:
            new_num = reversed_digits[i] *2 - 9
            reversed_digits[i] = new_num
        else:
            new_num = reversed_digits[i] *2
            reversed_digits[i] = new_num
    reversed_digits.append(last_digit)        
    new_sum = sum(reversed_digits)
    if new_sum % 10 == 0:
        return True
    else:
        return False

print(isCreditCardValid([5,2,2,8,2]))
print(isCreditCardValid([5,2,2,8,1]))