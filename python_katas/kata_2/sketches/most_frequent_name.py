def most_frequent_name(file_path):
    """
    2 Kata
    This function gets a path to a file containing names (name in each line)
    The function should return the most frequent name in the file
    You can assume file_path exists in the file system
    :param file_path: str - absolute or relative file to read names from
    :return: str - the mose frequent name. If there are many, return one of them
    """
    f = open(file_path)
    names_list = []
    for line in f.readlines():
        names_list.append(line.strip())
    f.close()
    most_frequent_name = max(set(names_list), key=names_list.count)
    return most_frequent_name



if __name__ == '__main__':

    print('\nmost_frequent_name:\n--------------------')
    print(most_frequent_name('names.txt'))
