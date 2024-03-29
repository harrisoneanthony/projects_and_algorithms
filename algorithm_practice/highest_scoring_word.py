'''DESCRIPTION:
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.'''

def high(x):
    val_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
    }
    score = 0
    highest_score = 0
    winning_word=''
    for word in x.split():
        for letter in word:
            if letter in val_dict:
                score += val_dict[letter]
        if score > highest_score:
            highest_score = score
            winning_word = word
        score=0
    return winning_word

print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))
print(high('aa b'))
print(high('b aa'))
print(high('bb d'))
print(high('d bb'))
print(high('aaa b'))