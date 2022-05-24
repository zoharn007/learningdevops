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

x = '1@yneaaaaaat.co.il'
w = x.split("@", 1)
first = w[0]
hostName = w[1]
flag_1 = True

for i in first[::]:
    if flag_1 == False:
        break
    if i.isalpha() or i.isnumeric():
        flag_1 = True
    else:
        flag_1 = False

if flag_1:
    try:
        ipAddress = socket.gethostbyname(hostName)
        print("IP address of the host name {} is: {}".format(hostName, ipAddress))
    except Exception as e:
        print(e)
else:
    print("False")



if __name__ == '__main__':
    print('\nis_valid_email:\n--------------------')
    print(is_valid_email('israel.israeli@gmail.com'))