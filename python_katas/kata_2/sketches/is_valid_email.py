def is_valid_email(mail_str):
    """
    3 Kata

    This function returns True if the given mail is in the form:
    (username)@(domainname)

    Where
    * (username) must start with digit or an English character, and can contains only 0-9 a-z A-Z . or _
    * (domainname) is a real, existed domain - one that resolves to an actual ip address

    Hint: use socket.gethostbyname() to resolve a DNS in Python code

    :param mail_str: mail to check
    :return: bool: True if it's a valid mail (otherwise either False is returned or the program can crash)
    """

    # Python program to validate an Email
    # import re module
    import re
    # re module provides support for regular expressions
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # Make a regular expression for validating an Email
    # Define a function for validating an Email

    def check(email):

        # pass the regular expression
        # and the string into the full_match() method

        if re.fullmatch(regex, email):
            return ("TRUE")

        else:
            return ("False")

    return check(mail_str)

if __name__ == '__main__':
    print('\nis_valid_email:\n--------------------')
    print(is_valid_email('israel.israeli@gmail.com'))