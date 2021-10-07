from english_words import english_words_lower_set

number_to_letter = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

def find_possible_words_rec(keys, letters):
    if not keys:
        return [letters]
    res = []
    for i in number_to_letter[keys[0]]:
        res += find_possible_words_rec(keys[1:], letters + [i])
    return res

def find_possible_words(keys):
    keys = [int(l) for l in keys if l.isdigit()]
    digits = [a for a in keys if a in number_to_letter]
    possible_words = find_possible_words_rec(digits, [])
    possible_words = [''.join(i) for i in possible_words]
    words = [i for i in possible_words if i in english_words_lower_set]
    return words
    
print(find_possible_words("42"))