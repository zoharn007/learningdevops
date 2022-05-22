
def list_flatten(test_list):
    """
    2 Kata

    This function gets a list of combination of integers or nested lists
    e.g.
    [1, [], [1, 2, [4, 0, [5], 6], [5, 4], 34, 0, [3]]

    The functions should return a flatten list (including all nested lists):
    [1, 1, 2, 4, 0, 5, 6, 5, 4, 34, 0, 3]

    :param lst: list of integers of another list
    :return: flatten list
    """
    if isinstance(test_list, list):
        if len(test_list) == 0:
            return []
        first, rest = test_list[0], test_list[1:]
        return list_flatten(first) + list_flatten(rest)
    else:
        return [test_list]
############################################################
"""# def flatten(S):
#    if S == []:
#        return S
#    if isinstance(S[0], list):
#        return flatten(S[0]) + flatten(S[1:])
#    print(S)
#    return S[:1] + flatten(S[1:])
#"""
