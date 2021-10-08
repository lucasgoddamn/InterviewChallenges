import random
import string

def find_longest_substring_palindrom(s):
    if s == "":
        return "That String is empty"
    longest_substring = ""
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i:-j] == ''.join(reversed(s[i:-j])) and len(s[i:-j]) > len(longest_substring):
                longest_substring = s[i:-j]
    return longest_substring

test = "ababbbbbbbeabbadd"
print(find_longest_substring_palindrom(test))

for i in range(100):
    s = ''.join(random.choice("abc")
                for _ in range(random.randint(5, 50)))
    print(s)
    print(find_longest_substring_palindrom(s))







