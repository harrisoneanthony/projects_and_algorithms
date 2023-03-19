

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

