def monotonic_array(lst):
    """
    1 Kata

    This function returns True/False if the given list is monotonically increased or decreased

    :param lst: list of numbers (int, floats)
    :return: bool: indicating for monotonicity
    """
    return (all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) or
            all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1)))

if __name__ == '__main__':
    print('\nmonotonic_array:\n--------------------')
    print(monotonic_array([10, 7, 3, 2, 1, 0, 2]))
