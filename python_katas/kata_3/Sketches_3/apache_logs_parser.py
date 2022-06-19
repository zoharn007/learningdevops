ISO_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


def apache_logs_parser(apache_single_log):
    """
    3 Kata

    Parses apache log (see format here https://httpd.apache.org/docs/2.4/logs.html)
    e.g.
    [Fri Sep 09 10:42:29.902022 2011] [core:error] [pid 35708:tid 4328636416] [client 72.15.99.187] File does not exist: /usr/local/apache2/htdocs/favicon.ico

    the parsed log data should be:
    date (datetime object), level (str), pid (int), thread_id (int), client_ip (str), log (str)

    Hint: use regex

    :param apache_single_log: str
    :return: parsed log data as tuple
    """
    date, level, pid, tid, client_ip, log = ..., ..., ..., ..., ..., ...
    return date, level, pid, tid, client_ip, log
