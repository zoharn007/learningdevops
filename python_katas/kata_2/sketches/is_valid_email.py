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

    import socket
    mail_check = mail_str.split("@", 1)
    username = mail_check[0]
    hostName = mail_check[1]

    def username_check(username):
        for i in username[::]:
            if not i.isalpha() and not i.isnumeric():
                return False
            else:
                pass
        return True

    def hostName_check(hostName):
        try:
            ipAddress = socket.gethostbyname(hostName)
            #w = ("IP address of the host name {} is: {}".format(hostName, ipAddress)
        except Exception as Eror:
            return False
        return True

    run = "hostName_check(hostName)"
    if username_check(username) and hostName_check(hostName):
        return True
    else:
        return False


if __name__ == '__main__':
    print('\nis_valid_email:\n--------------------')
    print(is_valid_email('israel.israeli@gmail.com'))

