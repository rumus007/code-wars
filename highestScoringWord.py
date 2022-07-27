"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""


def high(x):
    wordArray = x.split(" ")
    highest = {"sum": 0, "word": ""}
    for i, text in enumerate(wordArray):
        sum_value = sum([ord(character) - 96 for character in text])
        if sum_value > highest["sum"]:
            highest["sum"] = sum_value
            highest["word"] = text
    return highest["word"]


print(high("man i need a taxi up to ubud"))
print(high("what time are we climbing up the volcano"))
