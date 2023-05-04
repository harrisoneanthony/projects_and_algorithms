def nb_dig(n, d):
    count = 0
    for i in range(n + 1):
        # Square the number and convert to string
        square_str = str(i**2)
        # Count the number of occurrences of the digit in the square string
        count += square_str.count(str(d))
    return count

# def nb_dig(n, d):
#     return sum(str(i*i).count(str(d)) for i in range(n+1))

print(nb_dig(10,1))

