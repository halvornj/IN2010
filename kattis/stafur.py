import re

def matcher(char):
    vowels = ["a","o","e","i","u"]
    if char in vowels:
        return "Jebb"
    if re.compile('[a-z]').match(char)is not None:
        return"Neibb"
    return"kannski"

char = input().lower()
print(matcher(char))