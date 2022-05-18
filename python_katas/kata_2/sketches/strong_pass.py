def strong_pass(password):
    """
    1 Kata

    A password is considered strong if it satisfies the following criteria:
    1) Its length is at least 6.
    2) It contains at least one digit.
    3) It contains at least one lowercase English character.
    4) It contains at least one uppercase English character.
    5) It contains at least one special character. The special characters are: !@#$%^&*()-+

    This function returns True if the given password is strong enough
    """
    import re
    lowercase_flag = False
    uppercase_flag = False
    special_char_flag = re.compile('[!@#$%^&*()-+]')
    if special_char_flag.search(password) is None:
        special_character_flag = False
    else:
        special_character_flag = True
    digit_flag = False
    password = password
    if len(password) < 6:
        return False
    else:
        for i in range(len(password)):
            if password[i].islower():
                lowercase_flag = True
            if password[i].isupper():
                uppercase_flag = True
            if password[i].isdigit():
                digit_flag = True
        if lowercase_flag and uppercase_flag and digit_flag and special_character_flag:
            return True
        else:
            return False


if __name__ == '__main__':

    print('\nstrong_pass:\n--------------------')
    print(strong_pass('##$FgC7^^5a'))
