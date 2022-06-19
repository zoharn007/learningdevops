ISO_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


def valid_dag(edges):
    """
    5 Kata

    Given a DAG (https://en.wikipedia.org/wiki/Directed_acyclic_graph) in the form:
    [('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'd'), ('c', 'd'), ('c', 'e')]

    where a, b, c, d, e are vertices and ('a', 'b') etc... are edges
    This function determine whether the graph is a valid DAG

    :param edges: list of tuples of string 'a', 'b'....
    :return: bool - True if and only if it is a valid DAG
    """
    return None