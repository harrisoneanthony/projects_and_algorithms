
'''1. Multiples of Three - but Not All
Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.'''

def multiples_of_three(input):
    array =[]
    for i in range(input,0):
        if i % 3 == 0:
            array.append(i)
        if i == -3 or i == -6:
            array.remove(i)
    return array

# print(multiples_of_three(-300))

'''2. Printing Integers with While
Print integers from 2000 to 5280, using a WHILE.'''

def printing_integers_while():
    array =[]
    for i in range(2001):
        while i < 5280:
            array.append(i)
            i+=1
    return array

# print(printing_integers_while())

'''3. Counting, the Dojo Way
Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".'''

def counting(input):
    array = []
    for i in range(1,input):
        if i % 10 == 0:
            array.append("Dojo")
        elif i % 5 == 0:
            array.append("Coding")
        else:
            array.append(i)
    return array

# print(counting(100))

'''4. Flexible Countdown
Given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines).'''

def flexible_count(lowNum, highNum, multi):
    array=[]
    for i in range(highNum,lowNum, -multi):
        print(i)
        array.append(i)
    return array

print(flexible_count(2,9,3))