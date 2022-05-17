# Import the following modules
import shutil
from datetime import date
import os
import sys

# When there is need, just change the directory
os.chdir(sys.path[0])


# Function for performing the
# backup of the files and folders
def take_backup(src_file_name,
                dst_file_name=None,
                src_dir='',
                dst_dir=''):
    try:

        # Extract the today's date
        today = date.today()
        date_format = today.strftime("%d_%b_%Y_")

        # Make the source directory,
        # where we wanna backup our files
        src_dir = src_dir + src_file_name

        # If user not enter any source file,
        # then just give the error message...
        if not src_file_name:
            print("Please give atleast the Source File Name")
            exit()

        try:

            # If user provides all the inputs
            if src_file_name and dst_file_name and src_dir and dst_dir:
                src_dir = src_dir + src_file_name
                dst_dir = dst_dir + dst_file_name

            # When User Enter Either
            # 'None' or empty String ('')
            elif dst_file_name is None or not dst_file_name:
                dst_file_name = src_file_name
                dst_dir = dst_dir + date_format + dst_file_name

            # When user Enter an empty
            # string with one or more spaces (' ')
            elif dst_file_name.isspace():
                dst_file_name = src_file_name
                dst_dir = dst_dir + date_format + dst_file_name

            # When user Enter an a
            # name for the backup copy
            else:
                dst_dir = dst_dir + date_format + dst_file_name

            # Now, just copy the files
            # from source to destination
            shutil.copy2(src_dir, dst_dir)

            print("Backup Successful!")
        except FileNotFoundError:
            print("File does not exists!,\
			please give the complete path")

    # When we need to backup the folders only...
    except PermissionError:
        dst_dir = dst_dir + date_format + dst_file_name

        # Copy the whole folder
        # from source to destination
        shutil.copytree(src_file_name, dst_dir)


# Call the function
take_backup("GFG.txt")




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
