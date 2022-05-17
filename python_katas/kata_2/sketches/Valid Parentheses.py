def valid_parentheses(s):
    """
    3 Kata
    This function gets a string containing just the characters '(', ')', '{', '}', '[' and ']',
    and determines if the input string is valid.
    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
    e.g.
    s = '[[{()}](){}]'  -> True
    s = '[{]}'          -> False
    """
    x = len(s)
    while "()" or "{}" or "[]" in s and x != 0:
        s = s.replace("()", "")
        s = s.replace("{}", "")
        s = s.replace("[]", "")
        if x == 0:
            break
        x -= 1

    if len(s) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print('\nvalid_parentheses:\n--------------------')
    print(valid_parentheses('[[{()}](){}]'))
