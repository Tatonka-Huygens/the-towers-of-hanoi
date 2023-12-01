
def myConcat(L):
    current = ''
    for x in L:
        current = current + x
    return current


def snake_string(s):
    result = []
    # Outputs the first row, i.e., s[1], s[5], s[9], ...
    for i in range(1, len(s), 4):
        result.append(s[i])
    # Outputs the second row, i.e., s[0], s[2], s[4], ...
    for i in range(0, len(s), 2):
        result.append(s[i])
    # Outputs the third row, i.e., s[3], s[7], s[11], ...
    for i in range(3, len(s), 4):
        result.append(s[i])
    return ''.join(result)


def snake_string_pythonic(s):
    print(myConcat(['    ' + x + '         ' for x in s[1::4]]))
    print(myConcat([x + '      ' for x in s[::2]]))
    print(myConcat(['          ' + x + '   ' for x in s[3::4]]))
    return #s[1::4] + s[::2] + s[3::4]
