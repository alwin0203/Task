def checkAlphabet(x):
    if len(x) > 1:
        return 0
    else:
        if c >= 'a' and c <= 'z':
            return 1
        elif c >= 'A' and c <= 'z':
            return 1
        else:
            return 2

