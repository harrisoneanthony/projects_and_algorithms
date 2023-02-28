# for i in range(5, 0, -1):
#     print(i)

# def countdown(num):
#     if num == 0:
#         return ""
#     print(num)
#     countdown(num-1)

# countdown(5)

def sigma(num):
    if num == 1:
        return num
    return num + sigma(num-1)
print(sigma(5))