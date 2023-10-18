def dssize(arg):
    """Compute the size of a data structure,
I didn't see this in Python"""

    temp = 0

    for _ in arg:
        temp += 1

    return temp


def get_keys(arg):
    """Returns a list of keys in the dictionary (Not working)"""
    temp = []
    for x in arg:
        if x[0] != "\t" and x != "\n":
            temp.append(x[:-1])

    return temp


def generate_str(arg):
    temp = ""
    for _ in range(arg):
        temp += " "

    return temp


def probability(arg0, arg1):
    return float(arg0)/arg1


def analyze_str(arg0, arg1):
    s1 = dssize(arg0)
    s2 = dssize(arg1)

    str1 = arg0
    str2 = arg1

    if s1 > s2:
        str2 += generate_str(s1 - s2)
    elif s1 < s2:
        str1 += generate_str(s2 - s1)

    # Or str2, same size ...
    return probability(match_nr(str1, str2), dssize(str1)) >= 0.5


def match_nr(arg0, arg1):
    sz = dssize(arg0)
    c = 0

    temp = 0

    while True:
        if c == sz:
            break

        if arg0[c] == arg1[c]:
            temp += 1

        c += 1

    return temp
