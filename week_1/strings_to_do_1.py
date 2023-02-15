'''Strings To Do 1
Remove Blanks
Create a function that, given a string, returns all of that string's contents, but without blanks. 

If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic".'''

def remove_blanks(input):
    return "".join(input.split())
print(remove_blanks(" Pl ayTha tF u nkyM usi c "))

'''Get Digits
Create a JavaScript function that given a string, returns the integer made from the string's digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680.'''

def get_digits(input):
    return ''.join(filter(str.isdigit, input))

print(get_digits("0s1a3y5w7h9a2t4?6!8?0"))


'''Acronyms
Create a function that, given a string, returns the string's acronym (first letters only, capitalized). 

Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". 

Given "Live from New York, it's Saturday Night!", return "LFNYISN".'''

def acronmys(input):
    split_str = input.split()
    final_arr =[]
    for i in split_str:
        final_arr.append(i[0].upper())
    return "".join(final_arr)

print(acronmys(" there's no free lunch - gotta pay yer way. "))
print(acronmys("Live from New York, it's Saturday Night!"))


'''Zip Arrays into Dictionary
Dictionaries are sometimes called maps because a key (string) maps to a value. Given two arrays, create an associative array (map) containing keys of the first, and values of the second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}.'''

def zip_arrays_into_dictionary(arr_1, arr_2):
    d = {}
    for key in arr_1:
        for val in arr_2:
            d[key] = val
    return d

print(zip_arrays_into_dictionary(['abc', 3, 'yo'],[42, 'wassap',True]))

def create_associative_arry(arr_1,arr_2):
    associative_array = {}
    for i in range(len(arr_1)):
        associative_array[arr_1[i]] = arr_2[i]
    return associative_array

print(create_associative_arry(['abc', 3, 'yo'],[42, 'wassap',True]))

# def array_dict(arr_1, arr_2):
#     combined_dict = map(lambda i: (arr_1[i], arr_2[i]), range(len(arr_2))[::2])
#     return dict(combined_dict)

# print(array_dict(['abc', 3, 'yo'],[42, 'wassap',True]))

'''Invert Hash
Dictionaries are also called hashes (we'll learn why later). Build invertHash(assocArr) to convert hash keys to values, and values to keys. 

Example: given {"name": "Zaphod", "charm": "high", "morals": "dicey"}, return object {"Zaphod": "name", "high":"charm", "dicey": "morals"}.'''

def invert_hash(input):
    associative_array = {}
    for key, val in input.items():
        associative_array[val] = key
    return associative_array

print(invert_hash({"name": "Zaphod", "charm": "high", "morals": "dicey"}))