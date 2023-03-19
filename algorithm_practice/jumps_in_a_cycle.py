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
