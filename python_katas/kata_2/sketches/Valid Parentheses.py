class Solution:
    """Here we use stack validation and a dictionary!
    We need a Stack to store the last valid left part of the parentheses,
     the left parentheses are also taken as the key,
    and their values would be its right parentheses.
    So if we store the left parentheses inside the stack, and if we find a valid right part, pop it out of the stack.
    Think about the case ‘{[]}’, it is not hard to figure out,
     we need a Stack to store the last valid left part of parentheses, when next char is the valid right part,
     pop out the left part.

Another validation is to check if the length of the string is even,
if it is odd, then it's obviously not a valid parenthesis (or) balanced parentheses!
so a valid parentheses string’s length should always be even, we can add a check at the beginning.
The worst-case scenario is when someone starts off the input as a ‘((((((((((‘ and so on."""

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        dict = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for iin s:
            if i in dict.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if i!= dict[a]:
                    return False
        return stack == []

    if __name__ == '__main__':
        print('\nvalid_parentheses:\n--------------------')
        print(valid_parentheses('[[{()}](){}]'))

        print('\nfibonacci_fixme:\n--------------------')
        print(fibonacci_fixme(6))

        print('\nmost_frequent_name:\n--------------------')
        print(most_frequent_name('names.txt'))

        print('\nfiles_backup:\n--------------------')
        print(files_backup('python_katas/kata_2'))

        print('\nreplace_in_file:\n--------------------')
        print(replace_in_file('mnist-predictor.yaml', '{{IMG_NAME}}', 'mnist-pred:0.0.1'))

        print('\njson_configs_merge:\n--------------------')
        print(json_configs_merge('default.json', 'local.json'))

        print('\nmonotonic_array:\n--------------------')
        print(monotonic_array([1, 2, 3, 6, 8, 9, 0]))

        print('\nmatrix_avg:\n--------------------')
        print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]], rows=[0, 2]))
        print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

        print('\nmerge_sorted_lists:\n--------------------')
        print(merge_sorted_lists([1, 4, 77, 9, 13343], [-7, 0, 7, 23]))

        print('\nlongest_common_substring:\n--------------------')
        print(longest_common_substring('abcdefg', 'bgtcdesd'))

        print('\nlongest_common_prefix:\n--------------------')
        print(longest_common_prefix('abcd', 'ttty'))

        print('\nrotate_matrix:\n--------------------')
        print(rotate_matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))

        print('\nis_valid_email:\n--------------------')
        print(is_valid_email('israel.israeli@gmail.com'))

        print('\npascal_triangle:\n--------------------')
        print(pascal_triangle(4))

        print('\nlist_flatten:\n--------------------')
        print(list_flatten([1, 2, [3, 4, [4, 5], 7], 8]))

        print('\nstr_compression:\n--------------------')
        print(str_compression('aaaabdddddhgf'))

        print('\nstrong_pass:\n--------------------')
        print(strong_pass('##$FgC7^^5a'))
