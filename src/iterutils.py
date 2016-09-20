import itertools

def sliding(iterable, size, fillvalue=None):
    """
    Returns an iterator the slides over the given iterator in chunks of the given size
    """
    a = [itertools.islice(iterable, i, None) for i in range(size)]
    return itertools.zip_longest(*a, fillvalue=fillvalue)