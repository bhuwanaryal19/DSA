'''
A program to check whether the given parantheses is valid or not.

Ex:
 (), {()}, [{()}], {[{}()]} -> valid
 ((), []{, {, []([] -> invalid
'''

from stack import Stack

def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False

def is_valid(parantheses):
    s = Stack()
    balanced  = True
    for param in parantheses:
        if param in '({[':
            s.push(param)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not is_match(top, param):
                    balanced = False

    return balanced and s.is_empty()

# assertions to check our function is working correctly.
assert is_valid('') == True
assert is_valid('({[]})') == True
assert is_valid("(((({}))))") == True
assert is_valid("[][]]") == False
assert is_valid("[][]]]") == False
assert is_valid("{[{}()]}") == True

print('Done')