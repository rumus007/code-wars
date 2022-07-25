"""
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.


All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""

def valid_braces(string):
    # define empty stack
    stack = []
    for paren in string:
        # loop the string
        if paren == '(' or paren == '{' or paren == '[':
            # if any opening braces push the string in the stack
            stack.append(paren)
        else:
            if len(stack) == 0:
                # if closing braces check if stack is empty if empty then return false
                return False
            else:
                # if stack is not empty check if closing braces match that of last stack entry
                top = stack[-1]
                if (top == '(' and paren == ')') or (top == '{' and paren == '}') or (top == '[' and paren == ']'):
                    stack.pop()

    if len(stack) == 0:
        # if stack is empty then valid
        return True
    else:
        # if stack is not empty then invalid
        return False

print(valid_braces("]"))
print(valid_braces("()}[]"))
print(valid_braces("(){}[]"))
print(valid_braces("{{(())}}[]"))