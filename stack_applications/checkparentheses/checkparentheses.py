from stack import Stack

def checkParentheses(input_string):
    """Check if input_string has correctly formatted parentheses.
    If parentheses are correct, return True, else return False.

    Example behaviour:
    ================= ==============================
    input_string      checkParentheses(input_string)
    ================= ==============================
    ()                True
    (()({}))          True
    {aaa(vv)f[gg]df}  True
    a                 True
    (                 False
    (]                False
    aa(b]b)ee         False
    ({)}              False
    ================= ==============================
    """

    stack = Stack()

    for i in input_string:
        if i == '(' or i == '{' or i == '[':
            stack.push(i)
        if i == ')' or i == '}' or i == ']':
            if stack.is_empty():
                return False
            if not isMatchingPair(stack.pop(),i):
                return False

    if stack.is_empty():
        return True
    else:
        return False

def isMatchingPair(character1, character2):

   if character1 == '(' and character2 == ')':
        return True
   if character1 == '{' and character2 == '}':
        return True
   if character1 == '[' and character2 == ']':
        return True
   else:
        return False



