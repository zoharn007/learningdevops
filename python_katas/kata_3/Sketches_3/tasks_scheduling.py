ISO_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


def tasks_scheduling(tasks):
    """
    5 Kata

    Consider a list of n tasks (tuples), each has starting and ending time (datetime object), as following:
    [(s_1, e_1), (s_2, e_2), ..., (s_n, e_n)]
    where s_* and e_* are Python datetime objects

    Only one task can be performed every time.
    This function returns the index of tasks to perform such the total completed tasks is as large as possible

    :param: tasks: list of tuple (start, end) while start and end are datetime objects
    :return: list of tasks indexes to perform
    """
    return None