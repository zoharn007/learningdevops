def replace_in_file(file_path, text, replace_text):
    """
    2 Kata

    This function gets a path of text file, it replaces all occurrences of 'text' by 'replace_text'.
    The function saves the replaces content on the same path (overwrites the file's content)

    You MUST check that file_path exists in the file system before you try to open it

    :param file_path: relative or absolute path to a text file
    :param text: text to search
    :param replace_text: text to replace with
    :return: None
    """
    import os.path
    file_path = f"c://Users/znagar/PycharmProjects/learningdevops/{file_path}"
    file_exists = os.path.exists(file_path)
    if file_exists:
        # Read in the file
        with open(file_path, 'r') as file:
            file_data = file.read()

            # Replace the target string
            if text in file_data:
                file_data = file_data.replace(text, replace_text)
            else:
                None

        # Write the file out again
        with open(file_path, 'w') as file:
            file.write(file_data)
    else:
        print("File doesn't exist")


if __name__ == '__main__':
    print('\nreplace_in_file:\n--------------------')
    print(replace_in_file('mnist-predictor.yaml', '{{IMG_NAME}}', 'mnist-pred:0.0.1'))
