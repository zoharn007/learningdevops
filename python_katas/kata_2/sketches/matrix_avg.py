l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

lists = [l1, l2, l3]
for y in range(max_y):
    for x in range(max_x):
        for index, value in enumerate(lists):
            if [x, y] in value:
                print("l{}".format(value), end=" ")
                break
    print()


#def matrix_avg(mat, rows=None):
#    """
#    2 Kata
#
#    This function gets a 3*3 matrix (list of 3 lists) and returns the average of all elements
#    The 'rows' optional argument (with None as default) indicating which rows should be included in the average calculation
#
#    :param mat: 3*3 matrix
#    :param rows: list of unique integers in the range [0, 2] and length of maximum 3
#    :return: int - the average values
#    """


#if __name__ == '__main__':
#    print('\nmatrix_avg:\n--------------------')
#    print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]], rows=[0, 2]))
#    print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
