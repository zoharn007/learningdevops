def merge_sorted_lists(l1, l2):
    """
    1 Kata

    This function gets two sorted lists (each one of them is sorted)
    and returns a single sorted list combining both of them.

    Try to be as efficient as you can (hint - don't use Python's built in sort() or sorted() functions)

    :param l1: list of integers
    :param l2: list of integers
    :return: list: sorted list combining l1 and l2
    """

    def orginazied_list(l_1):
        organized_listed = l_1
        for i in range(len(organized_listed)):
            for j in range(i + 1, len(organized_listed)):
                if organized_listed[i] > organized_listed[j]:
                    organized_listed[i], organized_listed[j] = organized_listed[j], organized_listed[i]
        return organized_listed

    my_list = list(set(l1 + l2))
    orginazied_list(my_list)

    return my_list


if __name__ == '__main__':
    print('\nmerge_sorted_lists:\n--------------------')
    print(merge_sorted_lists([1, 4, 77, 9, 13343], [-7, 0, 7, 23]))
    print(merge_sorted_lists([1, 4, 77, 9, 13343], [-7, 1, 7, 23]))
    print(merge_sorted_lists([-1.56774564156465465156161], [-1.55555555555555555555555, 2.5]))
