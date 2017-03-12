
def find_from(string, subs, start = None, end = None):
    """
    Returns a tuple of the lowest index where a substring in the iterable "subs" was found, and the substring.
    If multiple substrings are found, it will return the first one.
    If nothing is found, it will return (-1, None)
    """
    string = string[start:end]

    last_index = len(string)
    substring = None

    for s in subs:
        i = string.find(s)
        if i != -1 and i < last_index:
            last_index = i
            substring = s
    
    if last_index == len(string):
        return (-1, None)
    
    return (last_index, substring)
