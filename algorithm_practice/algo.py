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

