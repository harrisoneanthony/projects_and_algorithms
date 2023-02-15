'''Second-to-Last
Return the second-to-last element of an array. Given [42,true,4,"Kate",7], return "Kate". If array is too short, return null.'''

def secondtolast(input):
    if len(input) > 1:
        return input[-2]

# print(secondtolast([42, True, 4, "kate", 7]))
# print(secondtolast([42, True]))

'''Double Trouble
Create a function that changes a given array to list each original element twice, retaining original order. Convert [4,"Ulysses",42,false] to [4,4,"Ulysses","Ulysses",42,42,false,false].'''

def double(lst):
    result =[]
    for i in lst:
        result.extend([i]*2)
    return result

print(double([4,"Ulysses",42,False]))