"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')   # elloHay orldway !
"""
import string


def pig_it(text):
    texts = text.split()
    to_return = []
    for t in texts:
        if(t in string.punctuation):
            to_return.append(t)
        else:
            to_return.append(t[1:] + t[0] + 'ay')
    return " ".join(to_return)

print(pig_it('Pig latin is cool !'))