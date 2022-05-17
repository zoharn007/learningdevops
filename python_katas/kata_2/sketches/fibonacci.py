def fibonacci_fixme(n):
    """
    2 Kata
    A Fibonacci sequence is the integer sequence of 1, 1, 2, 3, 5, 8, 13....
    The first two terms are 1 and 1. All other terms are obtained by adding the preceding two terms.
    This function should return the n'th element of fibonacci sequence. As following:
    fibonacci_fixme(1) -> 1
    fibonacci_fixme(2) -> 1
    fibonacci_fixme(3) -> 2
    fibonacci_fixme(4) -> 3
    fibonacci_fixme(5) -> 5
    But it doesn't (it has some bad lines in it...)
    You should (1) correct the for statement and (2) swap two lines, so that the correct fibonacci element will be returned
    """
    a = 0
    b = 1
    for i in range(1, n):
        tmp = a + b
        a = b
        b = tmp

    return b


if __name__ == '__main__':

    print('\nfibonacci_fixme:\n--------------------')
    print(fibonacci_fixme(6))
