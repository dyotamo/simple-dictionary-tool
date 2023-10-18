def get_keys(fd):
    """Returns a list of keys in the dictionary (Not working)"""
    temp = []
    for x in fd:
        if x[0] != "\t" and x != "\n":
            temp.append(x[:-1])

    return temp


def probability(arg0, arg1):
    return float(arg0)/arg1


def analyze_str(key, key_to_match):
    s1 = len(key)
    s2 = len(key_to_match)

    # Fill spaces
    if s1 > s2:
        key_to_match += (" " * (s1 - s2))
    elif s1 < s2:
        key += (" " * (s2 - s1))

    # Or key_to_match, same size ...
    matches = match_nr(key, key_to_match)
    return probability(matches, len(key)) >= 0.50


def match_nr(arg0, arg1):
    """ Counts how many matches two strings of the same size have """
    sz = len(arg0)
    c = 0

    temp = 0

    while True:
        if c == sz:
            break

        if arg0[c] == arg1[c]:
            temp += 1

        c += 1

    return temp
