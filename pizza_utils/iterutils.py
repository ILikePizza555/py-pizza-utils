import itertools


def sliding(iterable, size, fillvalue=None):
    """
    Returns an iterator the slides over the given iterator in chunks of the 
    given size
    """
    a = [itertools.islice(iterable, i, None) for i in range(size)]
    return itertools.zip_longest(*a, fillvalue=fillvalue)


def map_nested(v, f):
    """
    Maps a function to all values (and keys if dictionaries exist in the data 
    structure) of a given iterable. This function generates a new data 
    structure with the mapping applied.
    """

    if isinstance(v, list):
        return [map_nested(item, f) for item in v]
    elif isinstance(v, tuple):
        return tuple(map_nested(item, f) for item in v)
    elif isinstance(v, dict):
        return {map_nested(key, f): map_nested(value, f) for key, value in v.items()}

    return f(v)
