'''The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.'''

# def count(s):
#     result = {}
#     for c in s:
#         if c in result:
#             result[c] +=1
#         else:
#             result[c] = 1
#     return result

def count(string):
    return {i: string.count(i) for i in string}

print(count('aba'))
print(count(''))